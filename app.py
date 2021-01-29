from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

    
host = 'database-1.c6j2ix3ngibe.us-east-1.rds.amazonaws.com'
password = '19961994'
user = 'admin'
database = "database-1"
​
   
db = pymysql.connect(host=host, user=user, password=password, charset='utf8')
cursor = db.cursor()
​
    
sql = '''use homecreditprojet'''
cursor.execute(sql)
​
    
query_bureau = 'SELECT * FROM app_test'
​
    
from pandas import read_sql_query
​
    
import pandas as pd
​
    
app_test = pd.read_sql_query(query_bureau, db)
​
    
app_test.to_csv("app_test.csv", index=False)
​
    




@app.route('/')
def hello_world():
    return render_template("homecredits.html")


@app.route('/predict', methods = ['POST'])
def prediction():
    conn = sqlite3.connect(file_directory + 'HOME_CREDIT_DB.db')

    sk_id_curr = request.form.to_dict()['SK_ID_CURR']
    sk_id_curr = int(sk_id_curr)
    test_datapoint = pd.read_sql_query(f'SELECT * FROM applications WHERE SK_ID_CURR == {sk_id_curr}', conn)
    test_datapoint = test_datapoint.replace([None], np.nan)
    test_datapoint = test_datapoint.astype(application_dtypes)
    predicted_proba, predicted_class, data_for_display = test_predictor_class.predict(test_datapoint)

    if predicted_class == 1:
        prediction = 'a Potential Defaulter'
    else:
        prediction = 'not a Defaulter'
        predicted_proba = 1 - predicted_proba

    data_for_display = pd.concat([test_datapoint[['NAME_EDUCATION_TYPE', 'OCCUPATION_TYPE']], data_for_display.reset_index(drop = True)], axis = 1)
    data_for_display = data_for_display.to_html(classes = 'data', header = 'true', index = False)

    conn.close()
    gc.collect()

    return flask.render_template('result_and_inference.html', tables = [data_for_display],
            output_proba = predicted_proba, output_class = prediction, sk_id_curr = sk_id_curr)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)