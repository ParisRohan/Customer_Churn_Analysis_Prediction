from flask import Flask, render_template, request, jsonify
import requests
import pickle
import numpy as np
import sklearn
from flask_cors import cross_origin


app = Flask(__name__, template_folder="templates")
model = pickle.load(open('customer_churn_ada.pkl', 'rb'))
print("Model Loaded")


@app.route('/',methods=['GET'])
@cross_origin()
def Home():
    return render_template('home.html')


@app.route("/predict", methods=['GET','POST'])
@cross_origin()
def predict():     
    
    if request.method == 'POST':
 
        #MonthlyCharges  
        MonthlyCharges = float(request.form['MonthlyCharges'])

        #TotalCharges  
        TotalCharges = float(request.form['TotalCharges'])

        #Gender
        gender = request.form['gender']
        if(gender == 'Male'):
            gender_Male=1
        else:
            gender_Male=0
 
        #SeniorCitizen
        SeniorCitizen = request.form['SeniorCitizen']
        if(SeniorCitizen == 'Yes'):
            SeniorCitizen_Yes=1
        else:
            SeniorCitizen_Yes=0
 
        #Partner
        Partner = request.form['Partner']
        if(Partner == 'Yes'):
            Partner_Yes=1
        else:
            Partner_Yes=0
 
        #Dependents
        Dependents = request.form['Dependents']
        if(Dependents == 'Yes'):
            Dependents_Yes=1
        else:
            Dependents_Yes=0
 
        #PhoneService
        PhoneService = request.form['PhoneService']
        if(PhoneService == 'Yes'):
            PhoneService_Yes=1
        else:
            PhoneService_Yes=0
 
        #MultipleLines
        MultipleLines = request.form['MultipleLines']
        if(MultipleLines == 'Yes'):
            MultipleLines_Yes=1
            MultipleLines_No_phone_service=0
        elif(MultipleLines == 'No phone service'):
            MultipleLines_Yes=0
            MultipleLines_No_phone_service=1        
        else:
            MultipleLines_Yes=0
            MultipleLines_No_phone_service=0
            
        #InternetService
        InternetService = request.form['InternetService']
        if(InternetService == 'Fiber optic'):
            InternetService_Fiber_optic=1
            InternetService_No=0
        elif(InternetService == 'No'):
            InternetService_Fiber_optic=0
            InternetService_No=1        
        else:
            InternetService_Fiber_optic=0
            InternetService_No=0 
 
        #OnlineSecurity
        OnlineSecurity = request.form['OnlineSecurity']
        if(OnlineSecurity == 'No internet service'):
            OnlineSecurity_No_internet_service=1
            OnlineSecurity_Yes=0
        elif(OnlineSecurity == 'Yes'):
            OnlineSecurity_No_internet_service=0
            OnlineSecurity_Yes=1        
        else:
            OnlineSecurity_No_internet_service=0
            OnlineSecurity_Yes=0  
 
        #OnlineBackup
        OnlineBackup = request.form['OnlineBackup']
        if(OnlineBackup == 'No internet service'):
            OnlineBackup_No_internet_service=1
            OnlineBackup_Yes=0
        elif(OnlineBackup == 'Yes'):
            OnlineBackup_No_internet_service=0
            OnlineBackup_Yes=1        
        else:
            OnlineBackup_No_internet_service=0
            OnlineBackup_Yes=0   
    
        #DeviceProtection
        DeviceProtection = request.form['DeviceProtection']
        if(DeviceProtection == 'No internet service'):
            DeviceProtection_No_internet_service=1
            DeviceProtection_Yes=0
        elif(DeviceProtection == 'Yes'):
            DeviceProtection_No_internet_service=0
            DeviceProtection_Yes=1        
        else:
            DeviceProtection_No_internet_service=0
            DeviceProtection_Yes=0   

        #TechSupport
        TechSupport = request.form['TechSupport']
        if(TechSupport == 'No internet service'):
            TechSupport_No_internet_service=1
            TechSupport_Yes=0
        elif(TechSupport == 'Yes'):
            TechSupport_No_internet_service=0
            TechSupport_Yes=1        
        else:
            TechSupport_No_internet_service=0
            TechSupport_Yes=0          
 
        #StreamingTV
        StreamingTV = request.form['StreamingTV']
        if(StreamingTV == 'No internet service'):
            StreamingTV_No_internet_service=1
            StreamingTV_Yes=0
        elif(StreamingTV == 'Yes'):
            StreamingTV_No_internet_service=0
            StreamingTV_Yes=1        
        else:
            StreamingTV_No_internet_service=0
            StreamingTV_Yes=0          

        #StreamingMovies
        StreamingMovies = request.form['StreamingMovies']
        if(StreamingMovies == 'No internet service'):
            StreamingMovies_No_internet_service=1
            StreamingMovies_Yes=0
        elif(StreamingMovies == 'Yes'):
            StreamingMovies_No_internet_service=0
            StreamingMovies_Yes=1        
        else:
            StreamingMovies_No_internet_service=0
            StreamingMovies_Yes=0          

        #Contract
        Contract = request.form['Contract']
        if(Contract == 'One year'):
            Contract_One_year=1
            Contract_Two_year=0
        elif(Contract == 'Two year'):
            Contract_One_year=0
            Contract_Two_year=1        
        else:
            Contract_One_year=0
            Contract_Two_year=0          

        #PaperlessBilling
        PaperlessBilling = request.form['PaperlessBilling']
        if(PaperlessBilling == 'Yes'):
            PaperlessBilling_Yes=1
        else:
            PaperlessBilling_Yes=0

        #PaymentMethod
        PaymentMethod = request.form['PaymentMethod']
        if(PaymentMethod == 'Credit card (automatic)'):
            PaymentMethod_CCAuto=1
            PaymentMethod_EC=0
            PaymentMethod_MC=0
        elif(PaymentMethod == 'Electronic check'):
            PaymentMethod_CCAuto=0
            PaymentMethod_EC=1 
            PaymentMethod_MC=0
        elif(PaymentMethod == 'Mailed check'):
            PaymentMethod_CCAuto=0
            PaymentMethod_EC=0 
            PaymentMethod_MC=1
        else:
            PaymentMethod_CCAuto=0
            PaymentMethod_EC=0
            PaymentMethod_MC=0

        
        #tenure
        tenure = float(request.form['tenure'])
        if(0 < tenure <=12):
            tenure_grp_13to24=0
            tenure_grp_25to36=0
            tenure_grp_37to48=0
            tenure_grp_49to60=0
            tenure_grp_60above=0
        elif(12 < tenure <= 24):
            tenure_grp_13to24=1
            tenure_grp_25to36=0
            tenure_grp_37to48=0
            tenure_grp_49to60=0
            tenure_grp_60above=0        
        elif(24 < tenure <= 36):
            tenure_grp_13to24=0
            tenure_grp_25to36=1
            tenure_grp_37to48=0
            tenure_grp_49to60=0
            tenure_grp_60above=0            
        elif(36 < tenure <= 48):
            tenure_grp_13to24=0
            tenure_grp_25to36=0
            tenure_grp_37to48=1
            tenure_grp_49to60=0
            tenure_grp_60above=0        
        elif(48 < tenure <= 60):
            tenure_grp_13to24=0
            tenure_grp_25to36=0
            tenure_grp_37to48=0
            tenure_grp_49to60=1
            tenure_grp_60above=0
        else:
            tenure_grp_13to24=0
            tenure_grp_25to36=0
            tenure_grp_37to48=0
            tenure_grp_49to60=0
            tenure_grp_60above=1

            
        
        model_input=[[
                        MonthlyCharges, TotalCharges, gender_Male, SeniorCitizen_Yes, Partner_Yes, 
                        Dependents_Yes, PhoneService_Yes, MultipleLines_No_phone_service,
                        MultipleLines_Yes, InternetService_Fiber_optic, InternetService_No, 
                        OnlineSecurity_No_internet_service, OnlineSecurity_Yes, OnlineBackup_No_internet_service,
                        OnlineBackup_Yes, DeviceProtection_No_internet_service, DeviceProtection_Yes, 
                        TechSupport_No_internet_service, TechSupport_Yes, StreamingTV_No_internet_service, 
                        StreamingTV_Yes, StreamingMovies_No_internet_service, StreamingMovies_Yes,
                        Contract_One_year, Contract_Two_year, PaperlessBilling_Yes,
                        PaymentMethod_CCAuto, PaymentMethod_EC, 
                        PaymentMethod_MC, tenure_grp_13to24, tenure_grp_25to36, tenure_grp_37to48,
                        tenure_grp_49to60, tenure_grp_60above
                    ]]
            
        #np_array=np.asarray(model_input)
        #model_input=np_array.reshape(1,-1)
        
        prediction=model.predict(model_input)
        
        if(int(prediction)==1):
            return render_template('result.html',prediction_texts="YES :( ")
        else:
            return render_template('result.html', prediction_texts="NO :) ")
    else:
        return render_template('result.html')

#use this while running in local machine
if __name__=="__main__":
    app.run(debug=True)

#use this while deploying
#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8080)