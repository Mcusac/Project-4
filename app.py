import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template
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
    print("test")
    return("test")

@app.route("/get_data")
def data():
    session = Session(engine)
    
    results = session.query(new_table.year, new_table.make, new_table.model, new_table.final_price, new_table.mileage, new_table.engine, new_table.zipcode).all()
#  list of tuples, turning it a list of list to be jsonified
    results = [list(r) for r in results]
    
    print(results)
 

    return jsonify(results)

    session.close()    

# page route 
@app.route("/data")
def data_table():
    

    return render_template("data.html")

    return("test")

    
if __name__ == '__main__':
    app.run(debug=True)




