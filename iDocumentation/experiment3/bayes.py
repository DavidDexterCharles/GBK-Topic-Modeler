from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

newsgroups_train = fetch_20newsgroups(subset='train')
# categories = ['alt.atheism', 'talk.religion.misc',
#               'comp.graphics', 'sci.space']
# categories=['alt.atheism','soc.religion.christian','comp.graphics','sci.med']

categories =[
 'alt.atheism',
 'sci.space',
 'comp.graphics',
 'talk.religion.misc',
 
 'comp.os.ms-windows.misc',
 'comp.sys.ibm.pc.hardware',
 'comp.sys.mac.hardware',
 'comp.windows.x',
 'misc.forsale',
 'rec.autos',
 'rec.motorcycles',
 'rec.sport.baseball'#,
#  'rec.sport.hockey',
#  'sci.crypt',
#  'sci.electronics',
#  'sci.med',
#  'soc.religion.christian',
#  'talk.politics.guns',
#  'talk.politics.mideast',
#  'talk.politics.misc',
 
 
 ]


newsgroups_train = fetch_20newsgroups(subset='train',
                                      categories=categories)
newsgroups_test = fetch_20newsgroups(subset='test',
                                     categories=categories)                                      
                                      
                                      
vectorizer = TfidfVectorizer()#CountVectorizer()
# the following will be the training data
vectors = vectorizer.fit_transform(newsgroups_train.data)
vectors.shape


# this is the test data
vectors_test = vectorizer.transform(newsgroups_test.data)

clf = MultinomialNB(alpha=.01)

# the fitting is done using the TRAINING data
# Check the shapes before fitting
vectors.shape
#(2034, 34118)
newsgroups_train.target.shape
#(2034,)

# fit the model using the TRAINING data
clf.fit(vectors, newsgroups_train.target)

# the PREDICTION is done using the TEST data
pred = clf.predict(vectors_test)

# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html

print(len(pred))
count = 0
for i in range (len(pred)):
    if pred[i]==newsgroups_test.target[i]:
        count=count+1
print(count)

