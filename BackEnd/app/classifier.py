from gbk.gbk import GBK as Model
from topics import topics
from crawler import Crawler
import json


spider = Crawler('https://www.trinidadexpress.com',"",['p'],['time'],['h1','headline'])
test="https://www.trinidadexpress.com/news/local/ganja-goof/article_d9fbc45e-6494-11e9-95d8-c79addbed302.html"
result =  spider.get_article_data(test)
# result =  spider.get_article_data("https://www.trinidadexpress.com/news/local/film-festival-calls-for-caribbean-film-market-projects/article_a055767f-c135-5a9a-86b7-193686bf9b6a.html")
result = json.loads(result)
document = result['CONTENT']
print(document+"\n\n")


# document ='''
# Wikitext, also known as Wiki markup or Wikicode, consists of the syntax and keywords used by the MediaWiki software to format a page. To learn how to see this markup, and to save an edit, see: Help:Editing. ... There is a short list of markup and tips at Help:Cheatsheet.
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
            # if value > group[topic]:
                group[topic] += value
                test ={}
                test[t] =value
                curr[topic].append(test)

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