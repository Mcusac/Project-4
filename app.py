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
    
    try:
        year = float(request.form["inputYear"])

        mileage = float(request.form["inputMileage"])

        engine = float(request.form["inputEngine"])
    except:
        return render_template('search.html')
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
    make_Dodge = 0
    make_Triumph = 0
    make_Mazda = 0
    make_Datsun = 0
    make_Cadillac = 0
    make_Lexus = 0
    make_Audi = 0
    make_MG = 0
    make_AlfaRomeo = 0
    make_Nissan = 0
    make_Lotus = 0
    make_Buick = 0
    make_Acura = 0
    make_AstonMartin = 0
    make_Shelby = 0
    make_Volvo = 0
    make_InternationalHarvester = 0
    make_GMC = 0
    make_Austin_Healey = 0
    make_Oldsmobile = 0
    make_Saab = 0
    make_Bentley = 0
    make_Mini = 0
    make_Fiat = 0
    make_Lincoln = 0

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
    elif make == "Dodge":
        make_Dodge = 1
    elif make == "Triumph":
        make_Triumph = 1
    elif make == "Mazda":
        make_Mazda = 1
    elif make == "Datsun":
        make_Datsun = 1
    elif make == "Cadillac":
        make_Cadillac = 1
    elif make == "Lexus":
        make_Lexus = 1
    elif make == "Audi":
        make_Audi = 1
    elif make == "MG":
        make_MG = 1
    elif make == "Alfa Romero":
        make_AlfaRomeo = 1
    elif make == "Nissan":
        make_Nissan = 1
    elif make == "Lotus":
        make_Lotus = 1
    elif make == "Buick":
        make_Buick = 1
    elif make == "Acura":
        make_Acura = 1
    elif make == "Aston Martin":
        make_AstonMartin = 1
    elif make == "Shelby":
        make_Shelby = 1
    elif make == "Volvo":
        make_Volvo = 1
    elif make == "International Harvester":
        make_InternationalHarvester = 1
    elif make == "GMC":
        make_GMC = 1
    elif make == "Austin_Healey":
        make_Austin_Healey = 1
    elif make == "Oldsmobile":
        make_Oldsmobile = 1
    elif make == "Saab":
        make_Saab = 1
    elif make == "Bentley":
        make_Bentley = 1
    elif make == "Mini":
        make_Mini = 1
    elif make == "Fiat":
        make_Fiat = 1
    elif make == "Lincoln":
        make_Lincoln = 1

    car_fax = request.form["inputCarfax"]

    if car_fax == 'No':
        car_fax_report_Carfax = 1
    else:
        car_fax_report_Carfax = 0

    prediction = 0

    X = [[year, 
        mileage, 
        engine,
        make_Acura,
        make_AlfaRomeo,
        make_AstonMartin,
        make_Audi,
        make_Austin_Healey,
        make_BMW,
        make_Bentley,
        make_Buick,
        make_Cadillac,
        make_Chevrolet,
        make_Datsun,
        make_Dodge,
        make_Ferrari,
        make_Fiat,
        make_Ford,
        make_GMC,
        make_Honda,
        make_InternationalHarvester,
        make_Jaguar,
        make_Jeep, 
        make_Land_Rover,
        make_Lexus,
        make_Lincoln,
        make_Lotus,
        make_MG,
        make_Mazda,
        make_Mercedes_Benz,
        make_Mini,
        make_Nissan,
        make_Oldsmobile,
        make_Pontiac,
        make_Porsche,
        make_Saab,
        make_Shelby,
        make_Toyota,
        make_Triumph,
        make_Volkswagen,
        make_Volvo,
        make_Other,
        car_fax_report_Carfax]]

    
    print(X)

    filename1 = 'models/ExtraTrees.h5'
    loaded_model1 = pickle.load(open(filename1, 'rb'))

    filename2 = 'models/RandomForest.h5'
    loaded_model2 = pickle.load(open(filename2, 'rb'))

    print(loaded_model1.predict(X))
    print(loaded_model2.predict(X))


    prediction1 = loaded_model1.predict(X)
    prediction2 = loaded_model2.predict(X)

    # prediction = (prediction1 + prediction2)/2
    prediction = prediction2
    prediction = prediction[0]

    prediction = round(prediction, 0)

    return render_template("search.html", prediction = prediction)



    
if __name__ == '__main__':
    app.run(debug=True)

