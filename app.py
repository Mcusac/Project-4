import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
<<<<<<< HEAD
from flask import Flask, jsonify
from sqlalchemy import inspect  
=======
from flask import Flask, jsonify, render_template
from sqlalchemy import inspect 
 
>>>>>>> 0672df78f6940ae81515dac18c258d403752f5ea


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
    print("test")
    return("test")

@app.route("/get_data")
<<<<<<< HEAD
def names():
=======
def data():
>>>>>>> 0672df78f6940ae81515dac18c258d403752f5ea
    session = Session(engine)
    
    results = session.query(new_table.year, new_table.make, new_table.model, new_table.final_price, new_table.mileage, new_table.engine, new_table.zipcode).all()
#  list of tuples, turning it a list of list to be jsonified
    results = [list(r) for r in results]
    
    print(results)
 

    return jsonify(results)

    session.close()    

<<<<<<< HEAD
=======
# page route 
@app.route("/data")
def data_table():
    

    return render_template("data.html")

    return("test")

    
>>>>>>> 0672df78f6940ae81515dac18c258d403752f5ea
if __name__ == '__main__':
    app.run(debug=True)




<<<<<<< HEAD


# # # Save reference to the table
# # Passenger = Base.classes.passenger

# #################################################
# # Flask Routes
# #################################################

# @app.route("/")
# def welcome():
#     """List all available api routes."""
#     return (
#         f"Available Routes:<br/>"
#         f"/api/v1.0/names<br/>"
#         f"/api/v1.0/passengers"
#     )


# @app.route("/api/v1.0/names")
# def names():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all passenger names"""
#     # Query all passengers
#     results = session.query(Passenger.name).all()

#     session.close()

#     # Convert list of tuples into normal list
#     all_names = list(np.ravel(results))

#     return jsonify(all_names)


# @app.route("/api/v1.0/passengers")
# def passengers():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of passenger data including the name, age, and sex of each passenger"""
#     # Query all passengers
#     results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

#     session.close()

#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_passengers = []
#     for name, age, sex in results:
#         passenger_dict = {}
#         passenger_dict["name"] = name
#         passenger_dict["age"] = age
#         passenger_dict["sex"] = sex
#         all_passengers.append(passenger_dict)

#     return jsonify(all_passengers)


# if __name__ == '__main__':
#     app.run(debug=True)
=======
>>>>>>> 0672df78f6940ae81515dac18c258d403752f5ea
