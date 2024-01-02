import pickle
import numpy as np
from flask import Flask,render_template,request
#create flask object
app=Flask(__name__)
'''@app.route('/')
def hello():
    """test function"""
    return "Welcome to the Flask"
@app.route('/varshitha',methods=['GET'])
def check():
    """new Function"""
    return "KITS college"
    '''
with open('House_price.pkl','rb')as f:
    model=pickle.load(f)
@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    Rooms=int(request.form['bedrooms'])
    Bathrooms=int(request.form['bathrooms'])
    Place=int(request.form['location'])
    Area=int(request.form['area'])
    Status=int(request.form['status'])
    Facing=int(request.form['facing'])
    P_Type=int(request.form['type'])
    input_data=np.array([[Place,Area,Status,Rooms,Bathrooms,Facing,P_Type]])
    prediction=model.predict(input_data)[0]
    return render_template('index.html',prediction=prediction)



app.run()
