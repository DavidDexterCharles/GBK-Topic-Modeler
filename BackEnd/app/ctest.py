from gbk.gbk import GBK as Model
from topics import topics as TOPICS
def Average(lst,num): 
    if(sum(lst) >0):
        averagval = sum(lst) / len(lst) +(num-len(lst))
        print ("Average:{}".format(averagval))
        return averagval
    else:
        return 0
def getTopicCustom(topic,num):
    arr = []
    for k,v in topic.items():
        arr.append(v)
    avg = Average(arr,num)   
    return avg


def get_total(cat):
    featuresum = 0
    for k,v in cat.items():
       featuresum+=v
        # print(v)
    # print(featuresum)
    return featuresum


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
# Neeta Narine, girlfriend of murder victim, Eldon Roopnarine seen (inset), sighs during an interview with the Express at her Freeport home on Wednesday. 

# DEXTER PHILIP
# WHAT began as the kidnapping of a Carapichaima man and his girlfriend at the Waterloo cremation site on Tuesday night ended in his murder.

# Police were told Eldon Roopnarine was repeatedly slammed to the ground by the kidnappers, then left to die when he and his girlfriend were thrown out of the vehicle.

# Roopnarine, 37, of Ojar Maraj Avenue, Brickfield, died of head injuries caused by blunt force trauma, an autopsy found yesterday.

# His mother, Dowlatie Roopnarine, said there was nothing to take from her son except his car since he didn’t have a job or money.

# Police found the car abandoned in Brickfield a few kilometres away from where Roopnarine’s body was dumped.

# His girlfriend, Neeta Narine, was not injured, but trembled from the trauma of the ordeal when she spoke to the Express at her Freeport home yesterday.

# Narine said after the kidnappers threw them out on the road, she ran for some time to get help for Roopnarine.

# She returned hours later with police officers and found her ­boyfriend dead.

# Roopnarine’s mother wept as she told the Express she learned of her son’s death on social media.

# “I was sitting there for more than an hour. The police didn’t tell me that they found his body because I would have gone to see his body. Even if he was battered, I wanted to see him,” said the mother.

#  0425 NWS CENTRAL GRIEF 3-DEXTER.JPG
# Dowlatie Roopnarine, right, mother of murder victim Eldon Roopnarine, grieves at her Brickfield, Carapichaima home on Wednesday.

# DEXTER PHILIP
# Dowlatie Roopnarine said she had been waiting at Freeport Police Station for information on her son, when her sister informed her news of his death had been posted on social media.

# She recalled the last moments she spent with him were on ­Tuesday night, when they looked at the news on television.

# Narine called him to pick her up, and he left.

# When she did not see her son return home that night, she assumed he spent the night at ­Narine’s house.

# Terror ride

# Narine told the Express Roopnarine picked her up in his black Mazda 323 car at home and headed to the cremation site, where they were accustomed to liming.

# She said while there, they saw four men on the compound.

# “One of them [had] given him a sign like asking him for a cigarette. He was going to give him the cigarette, but then all four approached the car. I told him to drive out. But one of them pulled out the keys (from the ignition).

# “They pulled him out of the car and threw him in the trunk. They tied my hands with rope and put me in the back seat with my head down,” said Narine.

# The girlfriend said after a few minutes of driving, Roopnarine opened the trunk and jumped out on to the road.

# She said the kidnappers stopped the car and chased after him.

# “They grabbed him and flung him back in the trunk. Then a second time he jumped out. This time they grabbed him and slammed him down on the ground a few times.

# “Then they flung him back in the trunk. My head was down, but I was hearing everything,” she said.

# Narine said the kidnappers drove to an isolated, forested area where there were no street lights and threw her and Roopnarine out.

# “They tied my feet and tied a rag over my mouth, and threw me out next to him. They drove off.

# “I fought up and I loosened my hands and my feet. I lie down next to him and he wasn’t moving.

#  0425 NWS CENTARL GRIEF 4-DEXTER.JPG
# Relatives gather at the home of murder victim Eldon Roopnarine, at Brickfield, Carapichaima, home on Wednesday.

# DEXTER PHILIP
# “I was thinking he was unconscious because of how they slammed him on the ground. It was pitch black. I felt his face and something like water was pumping out his mouth and nose. I thought he would ‘catch himself’.

# “After a while, I shook him. I felt his heart (beat) and I think I was feeling something. I lie back down and waited for him to get up.

# “I was just closing my eyes and praying. I didn’t open my eyes when they threw us out. I just remain quiet. I was so traumatised,” she said.

# Get caught up with news from the news leader
# Subscribe now and get access to the Trinidad Express E-paper
# Narine said after several ­minutes with Roopnarine still unresponsive, she decided to get help.

# “My plan was to lie down there until he ‘catch himself’. But when I realised like he wasn’t getting up, I decided to run. I was barefoot. I ran until I met a dead-end, so I ran back out for about an hour or more until I saw lights.”

# Narine said she ran into the yard of a house and a resident called police.

# Officers of the Freeport Police Station picked her up at Roop­singh Road and during the pre-dawn hours they drove around searching for Roopnarine.

# Another police patrol car found Roopnarine’s vehicle abandoned at Waterloo and towed it back to the Freeport station.

# Narine was taken to the police station and she positively identified the vehicle.

# In it were a length of rope, a gas container and a crate of bottles.

#  0425 NWS CENTRAL GRIEF 1-DEXTER.JPG
# Neeta Narine, centre, grilfriend of murder victim Eldon Roopnarine, is consoled by relatives at her Freeport home on Wednesday.

# DEXTER PHILIP
# After giving police a statement about the incident, she was taken to the Chaguanas District Health Facility.

# She was discharged, then ­returned with police officers to search for Roopnarine.

# It was around 7 a.m. when one of the policemen saw his body ­lying near a pile of garbage.

# “From the time I watched the jersey and glimpsed his face I knew it was him,” said Narine.

# She said Roopnarine was a “very nice and loving person when he was sober, when he didn’t drink or smoke”.

# His mother said Roopnarine was a father of two and loved his children.

# Responding to the scene were Supt Gill, ASP Smith, Insp Figaro, Sgts Nelson and Boxer.

# The killing took the murder toll to 161 for the year so far. There were 167 murders at April 24 last year.
# '''




model.setpenaltyborder(1)
# the point at which words supposedly related are ignored, due to the extent to which they are repeated in other term vectors
# Higher the penalty border the more words allowed, it was observed that ignoreing words above average penalty helps to penalise words that repeat
# accross vectors, however in the event that we want to classify based on grouping of term vectors(that is multiple models),
# then increaseing the penalty border is recommended so that term vectors within a particular model wont compete to much with each other

# model.setpenaltyborder(1000)

topic = [
'Art and Culture',
'Crime',
'Conflicts and War and Peace',
'Diaster and Accidents',
'Economy',
'Education',
'Environment',
'Health',
'Human Interest',
'Labor',
'Lifestyle and Leisure',
'Politics',
'Religion and Belief',
'Science and Technology',
'Society',
'Sport',
'Weather'

]

for i in range(0,len(topic)):
    result = model.predict(topic[i],document)
    
    print("Results:{}".format(result))
    # ans = get_total(result)
    ans = getTopicCustom(result,len(TOPICS[topic[i]]))
    print("{} {}".format(topic[i],ans))
    
    print("\n")

# print(model.model[topic[6]]['sport']['docamt'])

