from flask import request, jsonify, make_response
from app import app
from model import Model
mvcmodel = Model()


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    
    return response


@app.route('/', methods=['GET'])
def test():
    return "Welcome to GBC API"

@app.route('/categorykeywords', methods=['GET'])
def getalltopicmodels():
    # page = request.args.get('page')
    page=1;
    result = mvcmodel.getcategorykeysbypage()
    
    return result

@app.route('/classificationmodel', methods=['GET'])
def getclassificationmodel():
    result = mvcmodel.getclassificationmodel()
    
    return result

@app.route('/keyword/<id>', methods=['GET'])
def get_one_keyword(id):
    return mvcmodel.getbyidkeyword(id)
@app.route('/keyword', methods=['POST'])
def create_keyword():
    return mvcmodel.createkeyword(request)
@app.route('/keyword/<id>', methods=['PATCH'])
def update_keyword():
    return mvcmodel.updatekeyword(request)
@app.route('/keyword', methods=['DELETE'])
def delete_keyword(id):
    return mvcmodel.deletekeyword(request)

@app.route('/keywords/', methods=['GET'])
@app.route('/keywords', methods=['GET'])
def getwordkey():
    query = request.args.get('query')
    page = request.args.get('page')
    if page:
        result = mvcmodel.getKeywordByPage(page)
    else:
        if query:
            result = mvcmodel.getKeyword(query)
        else:
            result= mvcmodel.getallkeywords()
    
    return result


@app.route('/categorysearch', methods=['GET'])
def getcategorybyquery():
    query = request.args.get('query')
    result =""
    if query:
        result = mvcmodel.getcategorybyquery(query)
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
 
@app.route('/classifydata', methods=['POST'])
def get_classofdata():
    # return mvcmodel.getTopics()
    # data =request.get_json()
    # print(request.data)
    # return str(request.data)
    result =  mvcmodel.get_classofdata(request)
    # data = json.loads(result)
    # print(data['document'])
    return result
    
@app.route('/article', methods=['GET'])
def get_articlebypage():
    page = request.args.get('page')
    if page:
        result = mvcmodel.get_articlebypage(page)
    else:
        result = mvcmodel.get_articlebypage(1)
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