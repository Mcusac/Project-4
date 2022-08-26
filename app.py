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

    return("test")

@app.route("/search")
def search():
    return render_template('search.html')


    
if __name__ == '__main__':
    app.run(debug=True)

