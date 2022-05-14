# Customer_Churn_Analysis_Prediction

# Usecase:
To identify customers who are more likely to be churned based on the historical data provided by Telco company. Several measures will be taken on the identified customers by proactively engaging with them to improve the company's profit.

# Medium Blog:
https://parisrohan.medium.com/customer-churn-analysis-and-prediction-using-python-d14d31716869

# Tech Stack:
* Front-End: HTML, CSS
* Back-End: Flask
* IDE: Jupyter notebook, Sypder

# How to run the app
1. Create a virtual environment using following command:
   * **_conda create -n <your environment name> python=3.7_**
2. Activate the created environment
   * **_activate <your environment name>_**
3. Navigate to the directory where you wish to install the packages 
4. Install the required packages using
   * **_pip install -r requirements.txt_**
5. Run the app using
   * **_python app.py_**

# Screenshots:

**Input:**
![image](https://user-images.githubusercontent.com/49038495/168410380-687bddc9-ea16-4d7a-abc9-d0850442fa7b.png)
![image](https://user-images.githubusercontent.com/49038495/168410411-86333f9a-f3c2-4ff1-bd13-4819f9fb338b.png)
![image](https://user-images.githubusercontent.com/49038495/168410420-aae2d098-4b2d-4ef5-bc08-547f76cfce3c.png)

**Output:**
![image](https://user-images.githubusercontent.com/49038495/168410438-31115dd2-491c-4824-8858-49a66957f471.png)


# Workflow:

## 1. Data collection:
Telco Customer Churn dataset from Kaggle has been used to build a classification model. The dataset can be found from the following link:-
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

The dataset contains 7043 rows and 21 features. Each row represents a customer, each column contains the customer’s attributes described in the column Metadata. The data set includes information about:
* Customers who left within the last month — the column is called Churn — this is the target feature
* Services that each customer has signed up for — phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
* Customer account information — how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges
* Demographic info about customers — gender, age range, and if they have partners and dependents

## 2. Data preprocessing:
* Handle missing values in the 'TotalCharges' feature
* Map the values from 'SeniorCitizen' feature to 0:'No', 1:'Yes'
* Create a new feature named 'tenure_grp' by grouping the values from 'tenure' feature
![image](https://user-images.githubusercontent.com/49038495/168242758-1f5409dc-f53b-40b9-8a56-6091ce9b10e5.png)
* Map the values from 'Churn' feature to 0:'No', 1:'Yes'
* Drop 'customerID' and 'tenure' features as they are not required
* Perform one-hot encoding on the categorical features

## 3. EDA:
* This is an imbalanced dataset as the observations with NO class >> observations with YES class
![image](https://user-images.githubusercontent.com/49038495/168241992-7f87ae62-8d59-4180-8486-dcb5ccc4af25.png)
** Blog on how to handle imbalanced dataset:
https://parisrohan.medium.com/how-to-handle-an-imbalanced-dataset-9b9012f07017
* Univariate analysis on the categorical features w.r.t the target feature
![image](https://user-images.githubusercontent.com/49038495/168242368-b733f2ed-1193-460a-8ec1-b357ca95c8c9.png)
![image](https://user-images.githubusercontent.com/49038495/168242502-5a7a516a-5bb5-46ea-9aea-5d6c2c50c700.png)
![image](https://user-images.githubusercontent.com/49038495/168242653-20b45ca9-47b4-490d-b4d9-9a6f8f183ce2.png)

## 4. Model building:
* Different classification models were compared using the PyCaret library. PyCaret is an open-source, low-code machine learning library in Python that automates machine learning workflows. It was found that the AdaBoostClassifier algorithm gives the best results for this data.
![image](https://user-images.githubusercontent.com/49038495/168243313-1f84dcd6-8a04-4d8c-a595-572ee2cd2f68.png)
* Apply SMOTE technique to handle imbalanced dataset.
* Baseline model metrics
![image](https://user-images.githubusercontent.com/49038495/168243509-54b5030e-8d03-46c8-a819-04e04c1c2461.png)
* Model metrics after hyperparameter tuning
![image](https://user-images.githubusercontent.com/49038495/168243636-1740c57f-add4-46ef-b522-ae7afe84ae5d.png)


