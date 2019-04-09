import jndcontrollers
from models import app
from flask import request, jsonify, make_response
import requests
import maincontroller

token_required = jndcontrollers.token_required
jnd = maincontroller.MainController()


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/')
def index():
    try:
        return requests.get('https://github.com/DavidDexterCharles?tab=repositories').content#, headers=headers).content
    except:
        return "Welcome To JND(Rapid API Development with JSONERD Automation)"

@app.route('/userauth', methods=['GET'])
@token_required
def getall_users_tokenrequired(current_user):
    # if jnd.isadmin(current_user):
    return jnd.getallusers()
    # else:
        # return jsonify({'message' : 'Cannot perform that function!'})

@app.route('/register', methods=['POST'])
def register_user():
    return jnd.doregister(request)
@app.route('/login', methods=['GET', 'POST'])
def login():
    return jnd.dologin(request)



#*****************************Article***************************************

@app.route('/article', methods=['GET'])
def getall_articles():
    return jnd.getallarticles()
@app.route('/article/<id>', methods=['GET'])
def get_one_article(id):
    return jnd.getbyidarticle(id)
@app.route('/article', methods=['POST'])
def create_article():
    return jnd.createarticle(request)
@app.route('/article/<id>', methods=['PATCH'])
def update_article():
    return jnd.updatearticle(request)
@app.route('/article', methods=['DELETE'])
def delete_article(id):
    return jnd.deletearticle(request)

#*****************************Articlecategorie***************************************

@app.route('/articlecategorie', methods=['GET'])
def getall_articlecategories():
    return jnd.getallarticlecategories()
@app.route('/articlecategorie/<id>', methods=['GET'])
def get_one_articlecategorie(id):
    return jnd.getbyidarticlecategorie(id)
@app.route('/articlecategorie', methods=['POST'])
def create_articlecategorie():
    return jnd.createarticlecategorie(request)
@app.route('/articlecategorie/<id>', methods=['PATCH'])
def update_articlecategorie():
    return jnd.updatearticlecategorie(request)
@app.route('/articlecategorie', methods=['DELETE'])
def delete_articlecategorie(id):
    return jnd.deletearticlecategorie(request)

#*****************************Categorie***************************************

@app.route('/categorie', methods=['GET'])
def getall_categories():
    return jnd.getallcategories()
@app.route('/categorie/<id>', methods=['GET'])
def get_one_categorie(id):
    return jnd.getbyidcategorie(id)
@app.route('/categorie', methods=['POST'])
def create_categorie():
    return jnd.createcategorie(request)
@app.route('/categorie/<id>', methods=['PATCH'])
def update_categorie():
    return jnd.updatecategorie(request)
@app.route('/categorie', methods=['DELETE'])
def delete_categorie(id):
    return jnd.deletecategorie(request)

#*****************************Geotag***************************************

@app.route('/geotag', methods=['GET'])
def getall_geotags():
    return jnd.getallgeotags()
@app.route('/geotag/<id>', methods=['GET'])
def get_one_geotag(id):
    return jnd.getbyidgeotag(id)
@app.route('/geotag', methods=['POST'])
def create_geotag():
    return jnd.creategeotag(request)
@app.route('/geotag/<id>', methods=['PATCH'])
def update_geotag():
    return jnd.updategeotag(request)
@app.route('/geotag', methods=['DELETE'])
def delete_geotag(id):
    return jnd.deletegeotag(request)

