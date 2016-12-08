import nltk

# list of words that do not have much meaning
from nltk.corpus import stopwords

#nltk.download()
#
# download at bash 
#python -m nltk.downloader all

sw = stopwords.words("english")
print len(sw)

#find the root of the words that have similar meaning
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
stemmer.stem("responsiveness")

