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
def home1():
    return render_template('index.html')

@app.route("/home")
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
    
    results = session.query(new_table.year, new_table.make, new_table.model, new_table.final_price, new_table.mileage, new_table.engine, new_table.zipcode, new_table.engine_string, new_table.car_fax_report).all()
#  list of tuples, turning it a list of list to be jsonified
    results = [list(r) for r in results]
     
    session.close() 
    return jsonify(results)

   

# page route 
@app.route("/data")
def data_table():
    
    return render_template("data.html")

@app.route("/search", methods = ["POST", 'GET'])
def search():
    check = 0
    
    try:
        year = float(request.form["inputYear"])

        mileage = float(request.form["inputMileage"])

        engine = float(request.form["inputEngine"])

        make_BMW = 0
        make_Chevrolet = 0
        make_Ferrari = 0
        make_Ford = 0
        make_Honda = 0
        make_Jaguar = 0
        make_Jeep = 0
        make_Land_Rover = 0
        make_Mercedes_Benz = 0
        make_Pontiac = 0
        make_Porsche = 0
        make_Toyota = 0
        make_Volkswagen = 0
        make_Other = 0

        make = request.form["inputMake"]

        if make == "BMW":
            make_BMW = 1
        elif make == "Chevrolet":
            make_Chevrolet = 1
        elif make == "Ferrari":
            make_Ferrari = 1
        elif make == "Ford":
            make_Ford = 1
        elif make == "Honda":
            make_Honda = 1
        elif make == "Jaguar":
            make_Jaguar = 1
        elif make == "Jeep":
            make_Jeep = 1
        elif make == "Land Rover":
            make_Land_Rover = 1
        elif make == "Mercedes-Benz":
            make_Mercedes_Benz = 1
        elif make == "Pontiac":
            make_Pontiac = 1
        elif make == "Ferrari":
            make_Porsche = 1
        elif make == "Toyota":
            make_Toyota = 1
        elif make == "Volkswagen":
            make_Volkswagen = 1
        elif make == "Other":
            make_Other = 1

        prediction = 0

        X = [[year, 
            mileage, 
            engine,
            make_BMW,
            make_Chevrolet,
            make_Ferrari,
            make_Ford,
            make_Honda,
            make_Jaguar,
            make_Jeep, 
            make_Land_Rover,
            make_Mercedes_Benz,
            make_Pontiac,
            make_Porsche,
            make_Toyota,
            make_Volkswagen,
            make_Other]]

        print(X)

        filename = './Regressor_model.h5'
        loaded_model = pickle.load(open(filename, 'rb'))

        print(loaded_model.predict(X))

        prediction = loaded_model.predict(X)

        prediction = prediction[0]

        prediction = round(prediction, 0)

        return render_template("search.html", prediction = prediction)
    except:
        return render_template('search.html')


    
if __name__ == '__main__':
    app.run(debug=True)

