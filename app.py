import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pickle
from flask import (
    Flask, 
    jsonify, 
    render_template, 
    request, 
    redirect)
from sqlalchemy import inspect 
 



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///data.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
insp = inspect(engine) 
tables = insp.get_table_names() 
print (tables)

new_table = Base.classes.new_table_name

# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/graphs")
def graphs():
    return render_template('graphs.html')

@app.route("/get_data")
def data():
    session = Session(engine)
    
    results = session.query(new_table.year, new_table.make, new_table.model, new_table.final_price, new_table.mileage, new_table.engine, new_table.zipcode, new_table.engine_string).all()
#  list of tuples, turning it a list of list to be jsonified
    results = [list(r) for r in results]
     
    session.close() 
    return jsonify(results)

   

# page route 
@app.route("/data")
def data_table():
    

    return render_template("data.html")

@app.route("/search", methods=["POST"]) # the methods = ["POST"] causes this page to not work, but not sure why
def search():

    make = request.form["inputMake"]
    if make == "":
        make = 0
    make = float(make)

    engine = float(request.form["inputEngine"])
    if engine == "":
        engine = 5700
    engine = float(engine)

    year = float(request.form["inputYear"])
    if year == "":
        year = 2000
    year = float(year)

    mileage = float(request.form["inputMileage"])
    if mileage == "":
        mileage = 10000
    mileage = float(mileage)

    prediction = 0

    X = [[make, engine, year, mileage]]

    print(X)

    filename = './Regressor_model.h5'
    loaded_model = pickle.load(open(filename, 'rb'))

    print(loaded_model.predict(X))

    prediction = loaded_model.predict(X)[0][0]

    prediction = "${0:,.2f}".format(prediction)

    print(prediction)
    
    return render_template("search.html", prediction = prediction)


    
if __name__ == '__main__':
    app.run(debug=True)

