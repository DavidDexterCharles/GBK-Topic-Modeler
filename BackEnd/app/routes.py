import jndcontrollers
from models import app
from flask import request, jsonify, make_response
import requests
import maincontroller
from crawler import Crawler
import json
# import asyncio, aiohttp , bs4 , re , json
# from urllib.parse import urlparse
headers = {'Content-Type': 'application/json'}
apidomain = 'http://127.0.0.1:8085/api/'

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
    


token_required = jndcontrollers.token_required
jnd = maincontroller.MainController()

# http://docs.python-requests.org/en/master/user/quickstart/




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


# https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request
@app.route('/articledata', methods=['POST'])
def get_article_data():
    # print(request.form['url'])
    # data = request.data
    
    '''
    Filter to see if the domain exists in domain table if it does then, get the id, if it does not then, 
    domain is unsupported and wont be added to the db, however best attempt classigication, would still be done.
    On submission of the url to the article table, if integrigity violated then just return the article with its categoriese
    '''
    
    #  q = '?q={"filters":[{"name":"domainname","op":"like","val":"%'+query+'%"}]}'
    # qresult = requests.get("http://0.0.0.0:8085/api/domain"+q).content
    
    data =request.get_json()
    # print(data['url'])
    if("trinidadexpress.com" in data['url']):
        spider = Crawler('https://www.trinidadexpress.com',"",['p'],['time'],['h1','headline'])
    elif("guardian.co.tt" in data['url']):
        spider = Crawler('https://www.guardian.co.tt',"",['p','bodytext'],['span','textelement-publishing date'],['h1','headline'])
    # elif("newsday.co.tt" in data['url']):
    #     spider = Crawler('https://newsday.co.tt',"",['p'],['time'],['h1'])
    elif("looptt.com" in data['url']):
        spider = Crawler('http://www.looptt.com',"",['p'],['span','date-tp-4 border-left'],['span','field field--name-title field--type-string field--label-hidden'])
    else:
        result = "Apples"
    
    result = spider.get_article_data(data['url'])
    r = requests.post(apidomain + 'article', result, headers=headers)#use internal api to post the data to database
    print(r)
    # result["domain_id"] = 1
    # elif("looptt.com" in data['url']):
    #     spider = Crawler('http://www.looptt.com',"",['p'],['i'],['h1','headline'])
    
    # print(result)
    return result


#ONLINE ARTICLES:
# https://www.guardian.co.tt/news/hidden-gem-now-an-eyesore-6.2.824227.b624882ed9
#(IGNORED) http://www.looptt.com/content/police-kill-four-chaguanas
#(BLOCKED) https://newsday.co.tt/2019/04/13/afro-trinidadian-males-at-higher-risk-of-prostate-cancer/
# https://www.trinidadexpress.com/news/local/he-killed-his-family-and-himself-but-why/article_3f35dd5c-5e53-11e9-bc81-9739ac1cf00f.html

#*****************************Topicmodel***************************************

@app.route('/topicmodel', methods=['GET'])
def getall_topicmodels():
    return jnd.getalltopicmodels()
@app.route('/topicmodel/<id>', methods=['GET'])
def get_one_topicmodel(id):
    return jnd.getbyidtopicmodel(id)
@app.route('/topicmodel', methods=['POST'])
def create_topicmodel():
    return jnd.createtopicmodel(request)
@app.route('/topicmodel/<id>', methods=['PATCH'])
def update_topicmodel():
    return jnd.updatetopicmodel(request)
@app.route('/topicmodel', methods=['DELETE'])
def delete_topicmodel(id):
    return jnd.deletetopicmodel(request)
    
#*****************************Keyword***************************************
# @app.route('/keywordkey', methods=['GET'])
# def getwordkeys():
#     return jnd.getallkeywords()

@app.route('/keywordkey', methods=['GET'])
def getwordkey():
    query = request.args.get('search')
    # return query
    if query:
        q = '?q={"filters":[{"name":"word","op":"eq","val":"'+query+'"}]}'
        result = requests.get("http://0.0.0.0:8085/api/keyword"+q).content
        return result
    else:
        return jnd.getallkeywords()
# @app.route('/keywordkey/', methods=['GET'])
# def getwordkeys_():
#     return jnd.getallkeywords()
@app.route('/categoriekey', methods=['GET'])
def getcategoriekey():
    query = request.args.get('search')
    if query:
        q = '?q={"filters":[{"name":"name","op":"eq","val":"'+query+'"}]}'
        result = requests.get("http://0.0.0.0:8085/api/categorie"+q).content
        return result
    else:
        return jnd.getallcategories()
@app.route('/keyword', methods=['GET'])
def getall_keywords():
    query = request.args.get('page')
    if query: #https://stackoverflow.com/questions/11774265/how-do-you-get-a-query-string-on-flask
        return requests.get(apidomain + 'keyword?page='+ str(query), headers=headers).content
    else:
        return jnd.getallkeywords()
@app.route('/keyword/<id>', methods=['GET'])
def get_one_keyword(id):
    return jnd.getbyidkeyword(id)
@app.route('/keyword', methods=['POST'])
def create_keyword():
    return jnd.createkeyword(request)
@app.route('/keyword/<id>', methods=['PATCH'])
def update_keyword():
    return jnd.updatekeyword(request)
@app.route('/keyword', methods=['DELETE'])
def delete_keyword(id):
    return jnd.deletekeyword(request)
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
    query = request.args.get('page')
    if query: #https://stackoverflow.com/questions/11774265/how-do-you-get-a-query-string-on-flask
        return requests.get(apidomain + 'categorie?page='+ str(query), headers=headers).content
    else:
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


#*****************************Domain***************************************
@app.route('/domaintest/<query>', methods=['GET'])
def getrestless_domains(query):
    q = '?q={"filters":[{"name":"domainname","op":"like","val":"%'+query+'%"}]}'
    result = requests.get("http://0.0.0.0:8085/api/domain"+q).content
    return result


@app.route('/domain', methods=['GET'])
def getall_domains():
    
    #     print (multi_dict.getlist(key))
    
    # jnd.RawApi(query)
    restless = jnd.restlessdomain(request)
    if not restless:
        return jnd.getalldomains()
    else:
        return restless
@app.route('/domain/<id>', methods=['GET'])
def get_one_domain(id):
    return jnd.getbyiddomain(id)
@app.route('/domain', methods=['POST'])
def create_domain():
    return jnd.createdomain(request)
@app.route('/domain/<id>', methods=['PATCH'])
def update_domain():
    return jnd.updatedomain(request)
@app.route('/domain', methods=['DELETE'])
def delete_domain(id):
    return jnd.deletedomain(request)
# @app.route('/domain_restless', methods=['GET'])
# def restlessdomain():
#     return jnd.restlessdomain(request)

# http://gbcsystem-ice-wolf.c9users.io:8082/domain?q={%22filters%22:[{%22name%22:%22domainname%22,%22op%22:%22like%22,%22val%22:%22%test%%22}]}
# http://gbcsystem-ice-wolf.c9users.io:8082/api/domain?q={%22filters%22:[{%22name%22:%22domainname%22,%22op%22:%22like%22,%22val%22:%22%asp%%22}]}