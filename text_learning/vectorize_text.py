#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText
from sklearn.feature_extraction.text import TfidfVectorizer


try:
    from progressbar import ProgressBar, Percentage, Bar
except ImportError:
    import pip
    pip.main(['install', 'progressbar'])


"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
# temp_counter = 0

print '[\033[91m LOADING\033[0m ] \033[94m\033[1mEmails are processing right now...\033[0m'


pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=17578).start()


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        # temp_counter += 1
        # if temp_counter < 200:
        path = os.path.join('..', path[:-1])
        # print path
        email = open(path, "r")

        ### use parseOutText to extract the text from the opened email
        stemmed_email=parseOutText(email)

        ### use str.replace() to remove any instances of the words
        ### ["sara", "shackleton", "chris", "germani"]
        expection = ["sara", "shackleton", "chris", "germani","sshacklensf","cgermannsf"]
        for unwanted_word in expection:
            stemmed_email = stemmed_email.replace(unwanted_word, "")
        # clear_email = stemmed_email.replace(expection, "")

        ### append the text to word_data

        word_data.append(stemmed_email)

        ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
        from_data.append(0 if name == "sara" else 1)
        # from_data.appedn(0) if (name = "sara") else from_data.append(1)
        
        email.close()
        pbar.update(len(word_data))

pbar.finish()
#check output             
print word_data[152]

print "emails processed"
from_sara.close()
from_chris.close()


pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )


### in Part 4, do TfIdf vectorization here
# lowercase default True
vectorizer = TfidfVectorizer(stop_words="english", lowercase = True)
vectorizer.fit_transform(word_data)
bag_of_words = vectorizer.get_feature_names()

print "[\033[95m \033[1m how many different words \033[0m ]:", len(bag_of_words)
print "[\033[95m \033[1m What is word number 34597 in Tfidf \033[0m ]:" , bag_of_words[34597]


"""
    BONUS: intro. to coloring in terminal YEY! for more hand implementation:
    
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    or install colorama library from pip. for more adv. (e.g. fore + back ground coloring)
    both of them will work on windows too if it has enabled ansi.sys
    [https://support.microsoft.com/en-us/kb/101875]
    
"""

