from re import template
from urllib import response
from flask import Flask, render_template, request , jsonify
import os
import yaml
import joblib
import pickle
import pandas as pd
import numpy as np 

webapp_root = "webapp"


static_dir = os.path.join(webapp_root, "style") 
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__ , static_folder=static_dir, 
template_folder=template_dir)



@app.route("/")
def home():
    return render_template('base.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Company = request.form['Company']
        if (Company=="Company_Apple"):
            Company_Apple = 1 
            Company_Acer = 0
            Company_Asus  = 0
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=0
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=0

        
        elif(Company=="Company_Asus"):
            Company_Apple = 0 
            Company_Acer = 0
            Company_Asus  = 1
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=0
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=0
        
        elif(Company=="Company_Chuwi"):
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 0
            Company_Chuwi = 1
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=0
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=0

        elif(Company=="Company_Dell"):
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 0
            Company_Chuwi = 0
            Company_Dell  = 1
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=0
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=0
        
        
        elif(Company=="Company_Fujitsu"):
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 0
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =1
            Company_Google=0
            Company_HP=0
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=0
        
        elif(Company=="Company_Google"): 
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 0
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=1
            Company_HP=0
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=0

        elif(Company=="Company_HP"):
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 0
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=1
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=0
        
        elif(Company=="Company_Huawei"):
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 0
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=0
            Company_Huawei=1
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=0
        
        elif(Company=="Company_LG"):    
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 0
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=0
            Company_Huawei=0
            Company_LG=1
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=0
        
        elif(Company=="Company_Lenovo"):    
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 0
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=0
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=1
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=0
        
        elif(Company=="Company_MSI"):    
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 0
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=0
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=1
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=0
        
        elif(Company=="Company_Mediacom"):    
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 0
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=0
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=1
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=0

        elif(Company=="Company_Microsoft"):    
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 0
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=0
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=1
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=0
        
        
        elif(Company=="Company_Razer"):    
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 0
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=0
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=1
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=0
        
        
        elif(Company=="Company_Samsung"):    
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 0
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=0
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=1
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=0
        
        elif(Company=="Company_Toshiba"):    
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 0
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=0
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=1
            Company_Vero=0
            Company_Xiaomi=0
        
        elif(Company=="Company_Vero"):    
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 0
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=0
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=1
            Company_Xiaomi=0
        
        elif(Company=="Company_Xiomi"):    
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 0
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=0
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=1
        
        elif(Company=="Company_Acer"):    
            Company_Apple = 0 
            Company_Asus  = 0
            Company_Acer = 1
            Company_Chuwi = 0
            Company_Dell  = 0
            Company_Fujitsu =0
            Company_Google=0
            Company_HP=0
            Company_Huawei=0
            Company_LG=0
            Company_Lenovo=0
            Company_MSI=0
            Company_Mediacom=0
            Company_Microsoft=0
            Company_Razer=0
            Company_Samsung=0
            Company_Toshiba=0
            Company_Vero=0
            Company_Xiaomi=0


        
        Type = request.form["Type"]    
        if (Type == "TypeName_Gaming"):
            TypeName_Gaming = 1
            TypeName_Netbook = 0
            TypeName_Notebook = 0
            TypeName_Ultrabook = 0
            TypeName_Workstation = 0
            TypeName_2_in_1_Convertible = 0
        
        elif(Type == "TypeName_Netbook"):
            TypeName_Gaming = 0
            TypeName_Netbook = 1
            TypeName_Notebook = 0
            TypeName_Ultrabook = 0
            TypeName_Workstation = 0
            TypeName_2_in_1_Convertible = 0
    
        elif(Type == "TypeName_Notebook"):
            TypeName_Gaming = 0
            TypeName_Netbook = 0
            TypeName_Notebook = 1
            TypeName_Ultrabook = 0
            TypeName_Workstation = 0
            TypeName_2_in_1_Convertible = 0
    
        elif(Type == "TypeName_Ultrabook"):
            TypeName_Gaming = 0
            TypeName_Netbook = 0
            TypeName_Notebook = 0
            TypeName_Ultrabook = 1
            TypeName_Workstation = 0
            TypeName_2_in_1_Convertible = 0
    
        elif(Type == "TypeName_Workstation"):
            TypeName_Gaming = 0
            TypeName_Netbook = 0
            TypeName_Notebook = 0
            TypeName_Ultrabook = 0
            TypeName_Workstation = 1
            TypeName_2_in_1_Convertible = 0

        elif(Type == "TypeName_2_in_1_Convertible"):
            TypeName_Gaming = 0
            TypeName_Netbook = 0
            TypeName_Notebook = 0
            TypeName_Ultrabook = 0
            TypeName_Workstation = 0
            TypeName_2_in_1_Convertible = 1
    
#RAM
        or_ram = request.form["Ram"]
        Ram = int(or_ram)
        

        OpSys = request.form["OpSys"]
        if(OpSys == 'Mac'):
            OpSys_Mac = 1
            OpSys_Other = 0
            OpSys_Windows = 0

        elif(OpSys == 'Other'):
            OpSys_Mac = 0
            OpSys_Other = 1
            OpSys_Windows = 0
        
        elif(OpSys == 'Windows'):
            OpSys_Mac = 0
            OpSys_Other = 0
            OpSys_Windows = 1

#weight        
        Weight = request.form['Weight']
        Weight= float(Weight)
        


#TouchScreen
        TouchScreen = request.form['TouchScreen']
        TouchScreen = float(TouchScreen)

        
        


#IPS
        IPS = request.form['IPS']
        IPS = int(IPS)
        


#screen_size
        Screen_Size = request.form['Inches']
        Screen_Size = float(Screen_Size)
        


#cpu 
        CPU = request.form['CPU']
        if (CPU == "Core i3"):
            CPU_name_Intel_Core_i3 = 1
            CPU_name_Intel_Core_i5 = 0
            CPU_name_Intel_Core_i7 = 0
            CPU_name_AMD_Processor = 0
            CPU_name_Other_Intel_Processor = 0
        
        elif (CPU == "Core i5"):
            CPU_name_Intel_Core_i3 = 0
            CPU_name_Intel_Core_i5 = 1
            CPU_name_Intel_Core_i7 = 0
            CPU_name_AMD_Processor = 0
            CPU_name_Other_Intel_Processor = 0
        
        elif (CPU == "Core i7"):
            CPU_name_Intel_Core_i3 = 0
            CPU_name_Intel_Core_i7 = 0
            CPU_name_Intel_Core_i5 = 0
            CPU_name_AMD_Processor = 0
            CPU_name_Other_Intel_Processor = 0
        
        elif (CPU == "Other"):
            CPU_name_Intel_Core_i3 = 0
            CPU_name_Intel_Core_i5 = 0
            CPU_name_Intel_Core_i7 = 0
            CPU_name_AMD_Processor = 0
            CPU_name_Other_Intel_Processor = 1
        
        
        elif (CPU == "AMD"):
            CPU_name_Intel_Core_i3 = 0
            CPU_name_Intel_Core_i5 = 0
            CPU_name_Intel_Core_i7 = 0
            CPU_name_AMD_Processor = 1
            CPU_name_Other_Intel_Processor = 0



#HDD in GB 
        HDD = request.form['Size of HDD(in GB)']
        HDD = int(HDD)


##ssd in GB
        SSD = request.form['Size of SSD(in GB)']
        SSD = int(SSD)





#GPU    

        Gpu = request.form["Gpu_brand"]
        if (Gpu == "Gpu_brand_AMD"):
            Gpu_brand_AMD = 1
            Gpu_brand_Intel =0
            Gpu_brand_Nvidia = 0
            
        elif (Gpu == "Gpu_brand_Intel"):
            Gpu_brand_AMD = 0 
            Gpu_brand_Intel =1
            Gpu_brand_Nvidia = 0
        
        elif (Gpu == "Gpu_brand_Nvidia"):
            Gpu_brand_AMD = 0 
            Gpu_brand_Intel =0
            Gpu_brand_Nvidia = 1
        
        #scree resolution
        Screen_Resolution = request.form['Screen_Resolution']
        resolution = str(Screen_Resolution)


        X_resolution = int(resolution.split('x')[0])
        Y_resolution = int(resolution.split('x')[1])

        PPI = ((X_resolution**2)+(Y_resolution**2))**0.5/(Screen_Size)


        features = [[Ram, Weight, TouchScreen, IPS, PPI, HDD, SSD,
       Company_Acer, Company_Apple, Company_Asus, Company_Chuwi,
       Company_Dell, Company_Fujitsu, Company_Google, Company_HP,
       Company_Huawei, Company_LG, Company_Lenovo, Company_MSI,
       Company_Mediacom, Company_Microsoft, Company_Razer,
       Company_Samsung, Company_Toshiba, Company_Vero, Company_Xiaomi,
       TypeName_2_in_1_Convertible, TypeName_Gaming, TypeName_Netbook,
       TypeName_Notebook, TypeName_Ultrabook, TypeName_Workstation,
       OpSys_Mac, OpSys_Other, OpSys_Windows, CPU_name_AMD_Processor,
       CPU_name_Intel_Core_i3, CPU_name_Intel_Core_i5,
       CPU_name_Intel_Core_i7, CPU_name_Other_Intel_Processor,
       Gpu_brand_AMD, Gpu_brand_Intel, Gpu_brand_Nvidia]]

        print(features)

       
        # round(prediction[0],2)  
        
        rf1 = joblib.load('rf1_final.pkl')

        pred = rf1.predict(features)

        print("Predicted price for this laptop could be between " +
             str(pred-1000)+"₹" + " to " + str(pred+1000)+"₹")




        return render_template('base.html', prediction_text="Your Laptop Price is Rs. {}".format(round(pred[0],2)))
     	    
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)

 #app.run(host="0.0.0.0", port=5000, debug=True)























        
        



          