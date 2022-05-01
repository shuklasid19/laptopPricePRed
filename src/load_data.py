#load the test and train files 
#train algo
#save the metrics ,params

import argparse
import pandas as pd
import os
import warnings
import sys
import numpy as np
from get_data import read_params, get_data


def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    df = df.iloc[:, 1:12]

    #we have to remove the GB part from the dataset
    df['Ram'] = df['Ram'].str.replace('GB', '')
    
    
    #same for weight 
    df['Weight'] = df['Weight'].str.replace('kg', '')

    #converting from string->integer for ram column
    df['Ram'] = df['Ram'].astype('int32')

    # converting from string-> float for the weight column
    df['Weight'] = df['Weight'].astype('float32')


    # creating a new col,touchscreen if the value is 1 that laptop is touch screen
    df['TouchScreen'] = df['ScreenResolution'].apply(lambda element:1 
                                                      if 'Touchscreen' in element else 0)


# creating a new col named IPS,does the laptop have IPS facility or not
    df['IPS'] = df['ScreenResolution'].apply(
    lambda element:1 if "IPS" in element else 0)



# we will split the text at the "x" letter and seperate the 2 parts
# from this we can observe that one of the col is Y res we need to do
# some feature engineering on the X res col

    splitdf = df['ScreenResolution'].str.split('x',n = 1,expand=True)

    df['X_res'] = splitdf[0]
    df['Y_res'] = splitdf[1]

#So basically from that whole text of the X_res col,we need to 
#extract the digits from it,but the problem is the numbers are scattered 
#in some cases,that is the reason why i am using regex,if we use this
#we will exactly get the numbers which we are looking for!,
#so firstly replace all the "," with "" and then find all numbers
#from that string as "\d+\.?\d+",\d means that integer number and \.? 
#all the numbers which come after an number and \d+ the string must end with number


    df['X_res'] = df['X_res'].str.replace(',','').str.findall(r'(\d+\.?\d+)').apply(lambda x:x[0])
    
    df['X_res'] = df['X_res'].astype('int')
    df['Y_res'] = df['Y_res'].astype('int')
    

    df['PPI'] = (((df['X_res']**2+df['Y_res']**2))**0.5/df['Inches']).astype('float')

#drop these features as we have made changes om 
    df.drop(columns=['ScreenResolution','Inches','X_res','Y_res'],inplace=True)

    df['CPU_name'] = df['Cpu'].apply(lambda text:" ".join(text.split()[:3]))

    '''
As mentioned earlier,if we get any of the intel `i3,i5 or i7` versions
we will return them as it is,but if we get any other processor
we will first check whether is that a variant of the intel? or not
if yes,then we will tag it as "Other Intel Processor" else we will
say it as `AMD Processor`

'''

    def processortype(text):
        if text=='Intel Core i7' or text=='Intel Core i5' or text=='Intel Core i3':
            return text
        else:
            if text.split()[0]=='Intel':
                return 'Other Intel Processor'
            else:
                return 'AMD Processor'
            
    df['CPU_name'] = df['CPU_name'].apply(lambda text:processortype(text))

    ## dropping the cpu column

    df.drop(columns=['Cpu'],inplace=True)

    ## 4 most common variants observed : HHD,SSD,Flash,Hybrid

# this expression will remove the decimal space for example 1.0 TB will be 1TB

    df['Memory'] = df['Memory'].astype(str).replace('\.0','',regex = True)

# replace the GB word with " "

    df['Memory'] = df['Memory'].str.replace('GB','')

# replace the TB word with "000"

    df['Memory'] = df['Memory'].str.replace('TB','000')

# split the word accross the "+" character

    newdf = df['Memory'].str.split("+",n = 1,expand = True)

    df['first'] = newdf[0]
    df['first'] = df['first'].str.strip()


    def applychanges(value):
        df['Layer1'+value] = df['first'].apply(lambda x:1 if value in x else 0)
    
    listtoapply = ['HDD','SSD','Hybrid','FlashStorage']    
    for value in listtoapply:
        applychanges(value)

    # remove all the characters just keep the numbers
    df['first'] = df['first'].str.replace(r'\D','')

    df['Second'] = newdf[1]

    
    

    def applychanges1(value):
        df['Layer2'+value] = df['Second'].apply(lambda x:1 if value in x else 0)
    
    
    listtoapply1 = ['HDD','SSD','Hybrid','FlashStorage']
    df['Second'] = df['Second'].fillna("0")
    for value in listtoapply1:
        applychanges1(value)
    # remove all the characters just keep the numbers
    df['Second'] = df['Second'].str.replace(r'\D','')
    print(df['Second'])


    df['first'] = df['first'].astype('int')
    df['Second'] = df['Second'].astype('int')

    # multiplying the elements and storing the result in subsequent columns


    df["HDD"]=(df["first"]*df["Layer1HDD"]+df["Second"]*df["Layer2HDD"])
    df["SSD"]=(df["first"]*df["Layer1SSD"]+df["Second"]*df["Layer2SSD"])
    df["Hybrid"]=(df["first"]*df["Layer1Hybrid"]+df["Second"]*df["Layer2Hybrid"])
    df["Flash_Storage"]=(df["first"]*df["Layer1FlashStorage"]+df["Second"]*df["Layer2FlashStorage"])


## dropping of uncessary columns

    df.drop(columns=['first', 'Second', 'Layer1HDD', 'Layer1SSD', 'Layer1Hybrid',
       'Layer1FlashStorage', 'Layer2HDD', 'Layer2SSD', 'Layer2Hybrid',
       'Layer2FlashStorage'],inplace=True)

    df.drop(columns=['Memory'],inplace=True)
    df.drop(columns = ['Hybrid','Flash_Storage'],inplace=True)

    df['Gpu brand'] = df['Gpu'].apply(lambda x:x.split()[0])

    # removing the "ARM" tuple

    df = df[df['Gpu brand']!='ARM']
    #drop the gpu feature
    df = df.drop(columns=['Gpu'])
  

    # club {Windows 10,Windows 7,Windows 7 S}-->Windows
# club {macOS,mac OS X}--> mac
# else return Others

    def setcategory(text):
        if text=='Windows 10' or text=='Windows 7' or text=='Windows 10 S':
            return 'Windows'
    
        elif text=='Mac OS X' or text=='macOS':
            return 'Mac'
    
        else:
            return 'Other'
    
    
    df['OpSys'] = df['OpSys'].apply(lambda x:setcategory(x))

    new_cols = [col.replace(" ", "_") for col in df.columns]
    raw_data_path = config["load_data"]["raw_dataset_csv"]


    df.to_csv(raw_data_path, sep=",", index=False, header=new_cols)
    print(df.columns)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path = parsed_args.config)
    