from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

    

​
    




@app.route('/')
def hello_world():
    return render_template("homecredits.html")


@app.route('/predict', methods = ['POST'])
def prediction():
    #host = 'database-1.c6j2ix3ngibe.us-east-1.rds.amazonaws.com'
#password = '19961994'
#user = 'admin'
#database = "database-1"
​
   
#db = pymysql.connect(host=host, user=user, password=password, charset='utf8')
#cursor = db.cursor()
​
    
#sql = '''use homecreditprojet'''
#cursor.execute(sql)
​
    
#query_bureau = 'SELECT * FROM app_test'
​
    
#from pandas import read_sql_query
​
    
#import pandas as pd
​
    
#app_test = pd.read_sql_query(query_bureau, db)
​
    
#app_test.to_csv("app_test.csv", index=False)
   def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('homecredits.html',pred='vous etes eligible pour un credit.\nprobabilité de credit  {}'.format(output),bhai="")
    else:
        return render_template('homecredits.html',pred='vous n etes pas eligible pour un credit\n probabilité de non credit  {}'.format(output),bhai="")
if __name__ == '__main__':
    app.run(debug=True)
