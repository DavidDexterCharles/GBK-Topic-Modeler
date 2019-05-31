from flask import request, jsonify, make_response
from app import app
from model import Model
mvcmodel = Model()

@app.route('/', methods=['GET'])
def test():
    return "test"

@app.route('/categoriekey', methods=['GET'])
def getcategoriekey():
    query = request.args.get('query')
    result =""
    if query:
        result = mvcmodel.getcategoriekey(query)
    else:
        result =  "All"  
    
    return result
    
@app.route('/topics', methods=['GET'])    
def getTopics():
    
    return mvcmodel.getTopics()
    
    
@app.route('/classify', methods=['GET'])    
def getCategory():
    query = request.args.get('query')
    result =""
    if query:
       result = mvcmodel.getCategory(query)
    else:
       result = "none"
    
    return result
# Add Articles to Database using model, articles are classified before addition
# Retrieve Articles from database with their labels and weights and confidence score
# Reclassify a single Article
# Relcassify all Articles
# Search articles by content,filter serch results by category
# CRUD Key Words
# CRUD topicmodel
# //update and read class vectors

# Access individual class vectors
# Access all class vectors

# System vs Application
#https://simplicable.com/new/systems-vs-applications
# Systems can have a user interface but are primarily intended to provide services to other systems and applications. Generally speaking, systems are more complex than applications.
# Applications are primarily intended to be used by people. In many cases, an application relies on systems to process data and execute transactions.