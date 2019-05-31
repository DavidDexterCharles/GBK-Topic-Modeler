from gbk.gbk import GBK as Model
from topics import topics as TOPICS
def Average(lst,num): 
    if(sum(lst) >0):
        print(lst)
        # print(num)
        # print(len(lst))
        averagval = sum(lst) / (len(lst) +(num-len(lst)))
        # print(averagval)
        print ("Average:{}".format(averagval))
        return averagval
    else:
        return 0
def getTopicCustom(topic,num):
    arr = []
    ans = 0
    for k,v in topic.items():
        arr.append(v)
    avg = Average(arr,num)  
    for kx,vx in topic.items():
        if vx <= avg and vx > ans:
            ans = vx
    return ans


def get_total(cat):
    featuresum = 0
    for k,v in cat.items():
       featuresum+=v
        # print(v)
    # print(featuresum)
    return featuresum
    
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

def applynounfilter(thedata):
    thedata = thedata.lower()
    tokenized = nltk.word_tokenize(thedata)
    is_noun = lambda pos: pos[:2] == 'NN'
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    thedata = ' '.join(nouns)
    # print(thedata)
    return thedata

model = Model()
model.load("articlemodel.json")

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

# document ='''
# Beautiful beaches that beckon with each wave, community festival that always involve food, dance and that good old Tobago hospitality. Need another reason to pop over to Tobago? The Jazz Experience is on this weekend.

# Preparations for the event are expected to kick into even higher gear this week as excitement mounts and the countdown to one of the Caribbean’s biggest Jazz Festivals begins.

# This year’s Tobago Jazz Experience runs from 25 April to the 28 and patrons can expect the best of local and international talent.

# Fringe events, held across the island, will culminate with the flagship concert of the festival, International Night at Pigeon Point Heritage Park on April 28. Performers on the night include seven time Grammy award singer , actress, Toni Braxton (Breathe Again, Let it Flow, Un-Break My heart ) , R&B singer Jacquees (B.E.D , You and At the Club) and Michael Bolton, known for his blue-eyed soul music “Missing You Now”, “Said I love you but I lied” , “How am I supposed to live without you”. Vaughnette Bigford is also billed to perform. The South Trinidad based singer is best known for injecting her sultry and honest brand of jazz into popular songs and calypsoes from the likes of The Mighty Sparrow, Lord Shorty, Winsford Devine, Merchant and Carol Addison.
#  '''


# document ='''
# SOME PUPILS of the Williamsville Secondary School are terrorising teachers who are pleading with  the relevant authorities to immediately intervene. Teachers' vehicles are being damaged, bottles are thrown at them during assemblies and the breakfast being given to pupils are being thrown all over the assembly's hall, teachers claim. One teacher said that on October 27, pupils blocked the driveway for the third time this term using galvanise roofing sheets, blackboards and other items.  “Students intimidate teachers saying 'they will do for them', teachers are afraid for their safety on the compound,” the Express was informed in a letter. The teachers said safety officers assigned to the school and National Maintenance Training and Security Company Limited (MTS) were incapable of handling those situations. The Trinidad and Tobago Unified Teachers Association (TTUTA) industrial relations officer (south) Justin De Freitas,  told the Express that  on Thursday, he was informed  “ that students were displaying high level of indiscipline.” Earlier this year, there were several reports of violence at the school and the police and Ministry of Education had gotten involved with former minister of education Dr Tim Gopeesingh visiting the school. 
# # '''


document='''
Well there is a new association trying to raise awareness for a new sport in T&T.

The sport being introduced is known as Handball and its being introduced to schools across the country by the Team Handball Association of Trinidad and Tobago.
'''


# document ='''
# On Thursday 13th and Friday 14th October, 2016 the Trinidad and Tobago Hospitality and Tourism Institute (TTHTI) held its first Sport Tourism Masters Class at Hilton Trinidad. This initiative was forged to bring awareness to participants about the theories and concepts of Sport Tourism as well as its separation from Sport Management. The main presenter was Dr. Daniel Funk, a professor in the Sport and Recreation Management Program and Washburn Senior Research Fellow for the School of Tourism and Hospitality Management at Temple University. He also serves as a PhD program advisor at the Fox School of Business for the Tourism and Sport concentration. Presentations were also done by the president of Trinidad and Tobago Olympic Committee (TTOC), Mr. Brian Lewis and Dr. Kenneth Butcher, a veteran in the sporting industry.

# On the first day of the class Dr. Funk presented on Sport Event Tourism and Marketing Sport Event Tourism, giving insight as to what it really is and some key aspects of the topic such as Sport Event Types, Benefits, Impacts of Sport Event Tourism and ways to aspects to help Market the events. His presentation was paired with visual aids and interactive case studies with room for questions. After lunch Mr. Brian Lewis presented on Economic Impact and Benefits of Sport Tourism. Mr. Lewis's presentation was highly informative and also interactive. The participants had a very positive reaction to the information presented for to them.

# On the second day Dr. Kenneth Butcher presented with a unique and informative presentation on Development and Implementation. Dr. Funk also presented, this time on Managing the Sport Tourism Experience. Similar to the first presentation it was very interactive. After lunch a panel discussion was held with experts in the industry. The panel consisted of Dr. Daniel Funk, Mr. Brian Lewis, Dr. Kenneth Butcher, Mr. Adrian Winter – advisor to the Minister in the Ministry of Tourism, Ms. Serlan Cabralis – Lecturer of Sports Management at the University of the West Indies and mediated by Dr. Patricia Butcher – Executive Director of TTHTI. The panel addressed questions of Marketing Sport Tourism, Economic Benefits and Impacts, Development and Implementation and Experience Management posted by participants of the class.

# At the end each participant was awarded a certificate of participation and priceless insight into a thriving industry. The class had approximately 50 participants who attended from various sporting associations and ministries. With a highly receptive audience and a combination of interesting speakers, the Sport Tourism Masters Class was a very informative success.

# '''

# model.setpenaltyborder(.05)

# model.setpenaltyborder(1)
# the point at which words supposedly related are ignored, due to the extent to which they are repeated in other term vectors
# Higher the penalty border the more words allowed, it was observed that ignoreing words above average penalty helps to penalise words that repeat
# accross vectors, however in the event that we want to classify based on grouping of term vectors(that is multiple models),
# then increaseing the penalty border is recommended so that term vectors within a particular model wont compete to much with each other

# model.setpenaltyborder(.03)

topic = [
'Art and Culture',
'Crime',
# # 'Conflicts and War and Peace',
# 'Diaster and Accidents',
# 'Economy',
# 'Education',
# 'Environment',
# 'Health',
# 'Human Interest',
# 'Labor',
# # 'Lifestyle and Leisure',
# 'Politics',
# # 'Religion and Belief',
# # 'Science and Technology',
# 'Society',
# 'Sport',
#'Weather'

]
maxchoice =0
maxtopic =''
numvecs = 1
for i in range(0,len(topic)):
    result = model.predict(topic[i],applynounfilter(document))
    
    
    ans = get_total(result)
    # ans = getTopicCustom(result,len(TOPICS[topic[i]]))
    if ans>maxchoice:
        maxchoice = ans
        maxtopic =topic[i]
        numvecs = len(result)
    print("VectorSize:{} Results:{}".format(len(result),result))
    print("{} {}".format(topic[i],ans))
    
    print("\n")

print("{}: {}".format(maxtopic,maxchoice))
# print(model.model[topic[9]]['labor']['docamt'])
# print(model.model[topic[1]]['sport']['docamt'])

