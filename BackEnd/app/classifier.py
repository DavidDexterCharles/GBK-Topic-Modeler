from gbk.gbk import GBK as Model
from topics import topics
from crawler import Crawler
import json


spider = Crawler('https://www.trinidadexpress.com',"",['p'],['time'],['h1','headline'])
test="https://www.trinidadexpress.com/news/local/big-fish-little-fish-and-an-ocean-of-lies/article_8e18b843-4905-5e8b-a397-7e5c42ed38d7.html"
result =  spider.get_article_data(test)
# result =  spider.get_article_data("https://www.trinidadexpress.com/news/local/film-festival-calls-for-caribbean-film-market-projects/article_a055767f-c135-5a9a-86b7-193686bf9b6a.html")
result = json.loads(result)
document = result['CONTENT']
print(document+"\n\n")


# document ='''
# The National Security Minister Stuart Young is also speaking up following the sensational search of the hotel room occupied by Mark Myrie (Buju Banton) on Saturday,

# Following Police Commissioner Gary Griffith’s visit with Buju before midnight Saturday, Young issued a statement today regarding the matter.

# Young said that Buju arrived in Trinidad and Tobago on April 19, and as Minister of National Security, Young granted Banton and one other Jamaican citizen/performer known as Luciano and American citizen/performer known as Wayne Wonder), Ministerial Permits to enter Trinidad and Tobago to perform at a concert today/

# “ This permission was granted after due consideration and also an appreciation of our CARICOM stance and commitments”

# '''


model = Model()
model.load("articlemodel.json")



# document = "opera"
results = {}



# for topic,catigories in topics.items():
#     results[topic] = (model.predict(topic,document).copy())
#     print("{}: {}".format(topic,results[topic]))
    
results["topicmodel"] = (model.predict("topicmodel",document).copy())
# print("{}: {}".format("topicmodel",results["topicmodel"]))

group = {}
curr = {}

for topic,catigories in topics.items():
    group[topic] = 0
    curr[topic] = []
    for t,value in results["topicmodel"].items():
        if t in topics[topic] and topic!="topicmodel":
            if value > group[topic]:
                group[topic] = value
                test ={}
                test[t] =value
                curr[topic].append(test)

    
print(curr)
print("\n\n")
print(group)
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