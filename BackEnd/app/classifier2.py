from gbk.gbk import GBK as Model
from topics import topics
from crawler import Crawler
import json


spider = Crawler('https://www.trinidadexpress.com',"",['p'],['time'],['h1','headline'])
test="https://www.trinidadexpress.com/news/local/five-people-were-murdered-on-sunday-night/article_6aacbbf6-650e-11e9-8bf0-bb495be7670d.html"
result =  spider.get_article_data(test)
# result =  spider.get_article_data("https://www.trinidadexpress.com/news/local/film-festival-calls-for-caribbean-film-market-projects/article_a055767f-c135-5a9a-86b7-193686bf9b6a.html")
result = json.loads(result)
document = result['CONTENT']
print(document+"\n\n")


document ='''
FIVE people, including a woman, have been shot dead overnight in four separate incidents in Tunapuna, Santa Cruz, La Horquetta and Laventille. Three of the people have so far been identified while police are yet to reveal the identities of the other two. In the first incident, police said Khelon "Kokey" McLeod, was shot dead at the savannah at Achong Trace, Tunapuna. Around the same time, Fabian Thomas was gunned down in Santa Cruz. A man and a woman, both of whom were standing along Morgan Lane, off Pashley Street, Laventille, were shot and killed around midnight. Their identities are yet to be released. And sometime around 2 a.m. Patrick Aaron was shot dead at Phase 4 LaHorquetta. Meanwhile, one man who was listed in critical condition at hospital after being shot together with three other people at the corner of Duncan and Charlotte Streets, Port of Spain, on Saturday night succumbed to his injuries yesterday evening. He has been identified as Israel Cox, 23. In that incident, Jevon Assing, 35, of Duncan Street, Port of Spain, Akeem Grant, 26 and Aria Haynes, 29, were also shot. Assing was pronounced dead at the scene. The latest incidents have taken the country's murder toll for the year so far to 157.
'''

# document ='''
# Evidence is growing that Cunupia doubles man Barry Choon killed his family before he committed suicide in Toco more than a week ago.

# Police found the weapon in the vehicle used to slit the throats of his pregnant wife, Shalini Sookdeo-Choon, and his daughter Sarah, before he likely turned it on himself.

# The weapon – a box cutter – was found on Choon’s lap where he sat in the driver’s seat of the family’s car, police said.

# Police said that an autopsy found that Shalini Sookdeo-Choon was five months pregnant with her third child at the time of her killing on April 12.

#  Barry Choon
# Sookdeo-Choon would have given birth in August.

# She had the couple’s second child last year – a boy – Jacob, seven months old.

# The infant was next to her in the back seat when the bodies found in the car parked at Hambug Trace.

# Choon, his wife and seven year old daughter Sarah, pathologist found, died by cut throat injuries.

# Jacob had been smothered to death.





# '''

document = "boy and girl died bandits"

def Average(lst,num): 
    if(sum(lst) >0):
        return sum(lst) / len(lst) +(num-len(lst))
    else:
        return 0
def getTopicCustom(topic,num):
    largest = 0
    key = ""
    arr = []
    for k,v in topic.items():
        arr.append(v)
    avg = Average(arr,num)    
    for k,v in topic.items():
        if v <=avg:
            largest = v
            key = k
        
    return key, largest


    

model = Model()
model.load("articlemodel.json")

# model.setpenaltyborder(1)
# print(model.penaltyborder)/


# result = (model.predict('Conflicts and War and Peace',document))
# print (result)
# key,value = getTopic(result,"")
# print("Conflicts and War and Peace ==>TAG_RETURNED: {} {}\n".format(key,value))



def getTopic(topic,category):
    largest = 0
    key = ""
    for k,v in topic.items():
        # if v < largest:
            largest += v
            key = category
    # print (key)
    # print (largest)
    return key, largest


def get_total(cat):
    featuresum = 0
    for k,v in cat.items():
        featuresum += v
    return featuresum
for k,v in topics.items():
    featuresum = 0
    result = model.predict(k,document)
    featuresum = get_total(result)
    print(result)
    print("TAG_RETURNED: {} {}\n".format(k,featuresum))
    # print(len(topics[k]))
    # key,value = getTopic(result,k)
    # print("TAG_RETURNED: {} {}\n".format(key,value))

result = model.model["Conflicts and War and Peace"]['protest']
result = model.model["Religion and Belief"]['church']
# result = model.model["Weather"]['weather']
# result = model.model["Crime"]['crime']
# result = model.model["Crime"]['crime']
with open('test.json', 'w') as modelobj:
            json.dump(result, modelobj,sort_keys=True, indent=4)
            
            
#Have to find the average
# have to rtest with spa/ham dataset
# have to cater for topics that were completely ignored..check len of topic list



'''
{'award': 95.31378645225116, 'animal': 59.5255598369938, 'prize': 24.602873109984536}
TAG_RETURNED: Human Interest 179.4422193992295

{'award': 94.54337354049049, 'animal': 59.52555983699381, 'prize': 24.60287310998454}
TAG_RETURNED: Human Interest 178.67180648746884


{'animal': 10.623796725578984, 'award': 172.32827422764646, 'prize': 3.517784058875461}
TAG_RETURNED: Human Interest 186.4698550121009

'''