import uuid
import datetime
from functools import wraps
import jwt
from flask import Flask, request, jsonify, make_response
import requests
import  json #https://simplejson.readthedocs.io/en/latest/
from werkzeug.security import generate_password_hash, check_password_hash
from models import app#, User
headers = {'Content-Type': 'application/vnd.api+json'}
apidomain = 'http://127.0.0.1:8085/api/'

#Sample PATCH/UPDATE (required to specify the id)
'''
http://127.0.0.1:8085/api/user/5
{	
    "data":{
		"type": "user",
		"id": "5",
	    "attributes": {
	       "email": "davidtest5@test.com"
	       
	    }
	}
}
'''
#Sample POST/INSERT
'''
http://127.0.0.1:8085/api/user
{	
    "data":{
		"type": "user",
	    "attributes": {
	       "email": "davidtest@test.com"
	       "name": "david"
	    }
	}
}
'''
#Sample Register
'''
http://127.0.0.1:8082/register
{
    "email": "david@test.com",
    "password": "123456"
}
'''
#Sample Login
'''
http://127.0.0.1:8082/login
{
    "email": "david@test.com",
    "password": "123456"
}
'''

def token_required(f):   #https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated


class ArticleJndController(object):
    def createarticle(self, request):
        data = json.dumps(request.get_json())
        return requests.post(apidomain + 'article', data, headers=headers).content

    def updatearticle(self, request):
        data = json.dumps(request.get_json())
        return requests.patch(apidomain + 'article', data, headers=headers).content

    def deletearticle(self, id):
        return requests.delete(apidomain + 'article/'+id, headers=headers).content
         
    def getallarticles(self):
        return requests.get(apidomain + 'article', headers=headers).content
        
    def getbyidarticle(self, id):
        return requests.get(apidomain + 'article/'+id, headers=headers).content
    
class ArticlecategorieJndController(object):
    def createarticlecategorie(self, request):
        data = json.dumps(request.get_json())
        return requests.post(apidomain + 'articlecategorie', data, headers=headers).content

    def updatearticlecategorie(self, request):
        data = json.dumps(request.get_json())
        return requests.patch(apidomain + 'articlecategorie', data, headers=headers).content

    def deletearticlecategorie(self, id):
        return requests.delete(apidomain + 'articlecategorie/'+id, headers=headers).content
         
    def getallarticlecategories(self):
        return requests.get(apidomain + 'articlecategorie', headers=headers).content
        
    def getbyidarticlecategorie(self, id):
        return requests.get(apidomain + 'articlecategorie/'+id, headers=headers).content
    
class CategorieJndController(object):
    def createcategorie(self, request):
        data = json.dumps(request.get_json())
        return requests.post(apidomain + 'categorie', data, headers=headers).content

    def updatecategorie(self, request):
        data = json.dumps(request.get_json())
        return requests.patch(apidomain + 'categorie', data, headers=headers).content

    def deletecategorie(self, id):
        return requests.delete(apidomain + 'categorie/'+id, headers=headers).content
         
    def getallcategories(self):
        return requests.get(apidomain + 'categorie', headers=headers).content
        
    def getbyidcategorie(self, id):
        return requests.get(apidomain + 'categorie/'+id, headers=headers).content
    
class GeotagJndController(object):
    def creategeotag(self, request):
        data = json.dumps(request.get_json())
        return requests.post(apidomain + 'geotag', data, headers=headers).content

    def updategeotag(self, request):
        data = json.dumps(request.get_json())
        return requests.patch(apidomain + 'geotag', data, headers=headers).content

    def deletegeotag(self, id):
        return requests.delete(apidomain + 'geotag/'+id, headers=headers).content
         
    def getallgeotags(self):
        return requests.get(apidomain + 'geotag', headers=headers).content
        
    def getbyidgeotag(self, id):
        return requests.get(apidomain + 'geotag/'+id, headers=headers).content
    
