from topics import topics
import requests
import  json
option = ["insertkeywords","insertcategorie","topicmodel"]

choice = option[2]


if choice == "insertkeywords":
    headers = {'Content-Type': 'application/json'}
    apidomain = 'http://127.0.0.1:8085/api/'
    keywords = topics["topicmodel"]
    for i in range(0,len(keywords)):
        data ={}
        data["word"] = keywords[i]
        data = json.dumps(data)
        # print(data)
        print(requests.post(apidomain + 'keyword', data, headers=headers).content)

if choice == "insertcategorie":
    headers = {'Content-Type': 'application/json'}
    apidomain = 'http://127.0.0.1:8085/api/'
    keywords = topics["topicmodel"]
    for topic,catigories in topics.items():
        data ={}
        data["name"] = topic
        data = json.dumps(data)
        # print(data)
        print(requests.post(apidomain + 'categorie', data, headers=headers).content)
        
if choice == "topicmodel":
    headers = {'Content-Type': 'application/json'}
    apidomain = 'http://127.0.0.1:8085/api/'
    for topic,catigories in topics.items():
        # print (topic)
        if topic != "topicmodel":
            q = '?q={"filters":[{"name":"name","op":"eq","val":"'+topic+'"}]}'
            result_topic = requests.get("http://0.0.0.0:8085/api/categorie"+q).json()
            print (str(result_topic["objects"][0]["name"])+"=>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            keywords = topics[topic]
            for i in range(0,len(keywords)):
                q = '?search='+keywords[i]
                result_keyword = requests.get("http://0.0.0.0:8082/keywordkey"+q).json()
                print (result_keyword["objects"][0]["word"])
                data ={}
                data["categorie_id"] = result_topic["objects"][0]["id"]
                data["keyword_id"] = result_keyword["objects"][0]["id"]
                data = json.dumps(data)
                requests.post(apidomain + 'topicmodel', data, headers=headers)
    # http://0.0.0.0:8082/keywordkey?search=Crime
    # q = '?q={"filters":[{"name":"word","op":"eq","val":"'+query+'"}]}'
    # result = requests.get("http://0.0.0.0:8085/api/keywordkey"+q).content
    
    # http://gbcsystem-ice-wolf.c9users.io:8082/categoriekey?search=Art and Culture
    # q = '?q={"filters":[{"name":"name","op":"eq","val":"'+query+'"}]}'
    # result = requests.get("http://0.0.0.0:8085/api/categorie"+q).content