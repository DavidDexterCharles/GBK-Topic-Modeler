from gbk.gbk import GBK as Model
from topics import topics
from crawler import Crawler
import json

def getTopic(topic):
    largest = 0
    key = ""
    for k,v in topic.items():
        if v > largest:
            largest = v
            key = k
    # print (key)
    # print (largest)
    return key, largest

spider = Crawler('https://www.trinidadexpress.com',"",['p'],['time'],['h1','headline'])
test="https://www.trinidadexpress.com/news/local/five-people-were-murdered-on-sunday-night/article_6aacbbf6-650e-11e9-8bf0-bb495be7670d.html"
result =  spider.get_article_data(test)
# result =  spider.get_article_data("https://www.trinidadexpress.com/news/local/film-festival-calls-for-caribbean-film-market-projects/article_a055767f-c135-5a9a-86b7-193686bf9b6a.html")
result = json.loads(result)
document = result['CONTENT']
print(document+"\n\n")


# document ='''
# FIVE people, including a woman, have been shot dead overnight in four separate incidents in Tunapuna, Santa Cruz, La Horquetta and Laventille. Three of the people have so far been identified while police are yet to reveal the identities of the other two. In the first incident, police said Khelon "Kokey" McLeod, was shot dead at the savannah at Achong Trace, Tunapuna. Around the same time, Fabian Thomas was gunned down in Santa Cruz. A man and a woman, both of whom were standing along Morgan Lane, off Pashley Street, Laventille, were shot and killed around midnight. Their identities are yet to be released. And sometime around 2 a.m. Patrick Aaron was shot dead at Phase 4 LaHorquetta. Meanwhile, one man who was listed in critical condition at hospital after being shot together with three other people at the corner of Duncan and Charlotte Streets, Port of Spain, on Saturday night succumbed to his injuries yesterday evening. He has been identified as Israel Cox, 23. In that incident, Jevon Assing, 35, of Duncan Street, Port of Spain, Akeem Grant, 26 and Aria Haynes, 29, were also shot. Assing was pronounced dead at the scene. The latest incidents have taken the country's murder toll for the year so far to 157.
# '''

document ='''
Evidence is growing that Cunupia doubles man Barry Choon killed his family before he committed suicide in Toco more than a week ago.

Police found the weapon in the vehicle used to slit the throats of his pregnant wife, Shalini Sookdeo-Choon, and his daughter Sarah, before he likely turned it on himself.

The weapon – a box cutter – was found on Choon’s lap where he sat in the driver’s seat of the family’s car, police said.

Police said that an autopsy found that Shalini Sookdeo-Choon was five months pregnant with her third child at the time of her killing on April 12.

 Barry Choon
Sookdeo-Choon would have given birth in August.

She had the couple’s second child last year – a boy – Jacob, seven months old.

The infant was next to her in the back seat when the bodies found in the car parked at Hambug Trace.

Choon, his wife and seven year old daughter Sarah, pathologist found, died by cut throat injuries.

Jacob had been smothered to death.





'''

document = " death of boy"

model = Model()
model.load("articlemodel.json")



# document = "opera"
results = {}



# for topic,catigories in topics.items():
#     results[topic] = (model.predict(topic,document).copy())
#     print("{}: {}".format(topic,results[topic]))
    
results["topicmodel"] = (model.predict("topicmodel",document).copy())
# print("{}: {}".format("topicmodel",results["topicmodel"]))


key,value = getTopic(results["topicmodel"])
print("\nTAG_RETURNED: {} {}".format(key,value))


group = {}
curr = {}
lstarr = []
def Average(lst): 
    return sum(lst) / len(lst) 
for topic,catigories in topics.items():
    group[topic] = 0
    maxval = 0
    tcounter = 0
    curr[topic] = []
    sortedweights = sorted(results["topicmodel"].items(),key=lambda p:p[1])
    for t,value in sortedweights:
        if t in topics[topic] and topic!="topicmodel":
            lstarr.append(value)
            tcounter += 1
            # if value > group[topic]:
            #     tcounter += 1
            #     maxval = value
            #     group[topic] += value
            test ={}
            test[t] =value
            curr[topic].append(test)
    if tcounter:
        avgval = Average(lstarr)
        # print(lstarr)
        for i in range(0,len(lstarr)):
            if lstarr[i] <= avgval:
                group[topic] = lstarr[i]
        # print(group[topic])
        
# CREATE TABLE topicmodel(
#   id int not null auto_increment primary key,
#   categorie_id int not null,
#   keyword_id int not null,
#   KEY `keyword_id` (`keyword_id`),
#   KEY `categorie_id` (`categorie_id`)
# )ENGINE=InnoDB;

# ALTER TABLE `topicmodel`
#   ADD CONSTRAINT `topicmodel_ibfk_1` FOREIGN KEY (`keyword_id`) REFERENCES `keyword` (`id`),
#   ADD CONSTRAINT `topicmodel_ibfk_2` FOREIGN KEY (`categorie_id`) REFERENCES `categorie` (`id`);

# ALTER TABLE `topicmodel` ADD UNIQUE `unique_index`(`keyword_id`, `categorie_id`);

# CREATE TABLE keyword(
#   id int not null auto_increment primary key,
#   word varchar(355) not null,
#   ON UPDATE CASCADE
#   ON DELETE RESTRICT
# )ENGINE=InnoDB;


# 0.182353231767391+
# 0.5885880819420868+
# 0.6590622350975455+
# 0.7101445627085949+
# 0.9349654636357561+
# 1.2153244941132502


# (0.016506778548403007+ 0.05777379919998828+ 0.05991278328282056)/3








# print(curr['Sport'])    
# print(curr['Health'])
# print(curr['Crime'])
# print(curr['Environment'])
# print(curr['Art and Culture'] )
# print(curr['Religion and Belief'] )
# print(curr['Science and Technology'] )

# print("\n\n")
# print(group)


# print(model.model['topicmodel']['forest']['features'])
# print("\n\n")
# print(curr['Politics'])
# print(curr['Crime'])
# print(curr['Science and Technology'])
# print(curr['Art and Culture'])
# print(curr['Sport'])
# print(curr['Society'])
# print(curr['Crime'])
# print(curr['Lifestyle and Leisure'])
# print(results['Science and Technology'])

# print(results)