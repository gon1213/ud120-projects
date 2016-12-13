#!/usr/bin/python

###
### in poiFlagEmail() below, write code that returns a boolean
### indicating if a given email is from a POI
###

import sys
import reader
import poi_emails

def getToFromStrings(f):
    '''
    The imported reader.py file contains functions that we've created to help
    parse e-mails from the corpus. .getAddresses() reads in the opening lines
    of an e-mail to find the To: From: and CC: strings, while the
    .parseAddresses() line takes each string and extracts the e-mail addresses
    as a list.
    '''
    f.seek(0)
    to_string, from_string, cc_string   = reader.getAddresses(f)
    to_emails   = reader.parseAddresses( to_string )
    from_emails = reader.parseAddresses( from_string )
    cc_emails   = reader.parseAddresses( cc_string )

    return to_emails, from_emails, cc_emails


### POI flag an email

def poiFlagEmail(f):
    """ given an email file f,
        return a trio of booleans for whether that email is
        to, from, or cc'ing a poi """

    to_emails, from_emails, cc_emails = getToFromStrings(f)

    ### poi_emails.poiEmails() returns a list of all POIs' email addresses.
    poi_email_list = poi_emails.poiEmails()

    to_poi = False
    from_poi = False
    cc_poi   = False

    ### to_poi and cc_poi are related functions, which flag whether
    ### the email under inspection is addressed to a POI, or if a POI is in cc
    ### you don't have to change this code at all

    ### there can be many "to" emails, but only one "from", so the
    ### "to" processing needs to be a little more complicated
    if to_emails:
        ctr = 0
        while not to_poi and ctr < len(to_emails):
            if to_emails[ctr] in poi_email_list:
                to_poi = True
            ctr += 1
    if cc_emails:
        ctr = 0
        while not to_poi and ctr < len(cc_emails):
            if cc_emails[ctr] in poi_email_list:
                cc_poi = True
            ctr += 1


    #################################
    ######## your code below ########
    ### set from_poi to True if #####
    ### the email is from a POI #####
    #################################
    if from_emails:
        for email in from_emails:
            if email in poi_email_list:
                from_poi = True
                break
    
    
    

    #################################
    return to_poi, from_poi, cc_poi





    ################################################################
    #student_main.py
    ################################################################
    #!/usr/bin/python

import os
import sys
import zipfile
from poi_flag_email import poiFlagEmail, getToFromStrings

data_dict = {}

with zipfile.ZipFile('emails.zip', "r") as z:
    z.extractall()

for email_message in os.listdir("emails"):
    if email_message == ".DS_Store":
        continue
    message = open(os.getcwd()+"/emails/"+email_message, "r")
    to_addresses, from_addresses, cc_addresses = getToFromStrings(message) 
    
    to_poi, from_poi, cc_poi = poiFlagEmail(message)
    
    for recipient in to_addresses:
        # initialize counter
        if recipient not in data_dict:
            data_dict[recipient] = {"from_poi_to_this_person":0}
        # add to count
        if from_poi:
                data_dict[recipient]["from_poi_to_this_person"] += 1

    message.close()

for item in data_dict:
    print item, data_dict[item]
    
#######################################################    
def submitData():
    return data_dict