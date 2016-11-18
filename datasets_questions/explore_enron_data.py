#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


#NAME OF THE PERSON
#print [x for x, y in enron_data.items()]


#how many data point in dataset
print "Number of people in the Enron dataset: {0}".format(len(enron_data))
#how many feature in each person
print 'Number of features for each person in the Enron dataset: {0}'.format(len(enron_data.values()[0]))
print [x for x in enron_data.values()[0]]
#how many POIs are in the dataset?
# print [x for x in enron_data.items()]
poi_list= [x for x , y in enron_data.items() if y["poi"]]
print "Number of POIs : {0}".format(len(poi_list))

###Query the Dateset 1
# what is the total value of the stock belonging to James Prentice?
#print enron_data['PRENTICE JAMES']

# for x, y in enron_data.items():
#     if x == "PRENTICE JAMES":
#         print y["total_stock_value"]
# print "PRENTICE JAMES's total_stock_value: {0}".format([y["total_stock_value"] for x, y in enron_data.items() if x=="PRENTICE JAMES"])
print "PRENTICE JAMES's total_stock_value: {0}".format(enron_data["PRENTICE JAMES"]["total_stock_value"])

###Query the Dateset 2
#how many messages do we have from Wesley Colwell to POIs?
# print "messages from WESLEY COLWELL to POIs: {0}".format([y["from_this_person_to_poi"] for x, y in enron_data.items() if x=="COLWELL WESLEY"])
print "messages from WESLEY COLWELL to POIs: {0}".format(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

###Query the Dateset 3
#What's the value of stock options exercised by Jeff Skilling?
# print "Jeff skilling's value of stock options exercised: {0}".format([y["exercised_stock_options"] for x, y in enron_data.items() if x=="SKILLING JEFFREY K"])
print "Jeff skilling's value of stock options exercised: {0}".format(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

# follow the money
names = ['SKILLING JEFFREY K', 'FASTOW ANDREW S', 'LAY KENNETH L']
names_payments = {name:enron_data[name]['total_payments'] for name in names}
print sorted(names_payments.items(), key=lambda x: x[1], reverse=True)

#Dealing with Unfilled Features
index_want=['salary', 'to_messages', 'deferral_payments', 'total_payments', 'exercised_stock_options', 'bonus', 'restricted_stock', 'shared_receipt_with_poi', 'restricted_stock_deferred', 'total_stock_value', 'expenses', 'loan_advances', 'from_messages', 'other', 'from_this_person_to_poi', 'poi', 'director_fees', 'deferred_income', 'long_term_incentive', 'email_address', 'from_poi_to_this_person']

import pandas as pd
df = pd.DataFrame(enron_data)

df2=df.T
# print df2
print "people has salary data: {0}".format(len(df2["salary"][df2["salary"]!="NaN"]))

print "people has email: {0}".format(len(df2['email_address'][df2['email_address']!="NaN"]))

###missing POI1
# How many people in the E+F dataset (as it currently exists) have NaN for their total payments?
# What percentage of people in the dataset as a whole is this?

isnan = df2["total_payments"][df2["total_payments"]=="NaN"].count()
total = df2["total_payments"].count()

print 'total_payments == \'NaN\': {0} people = {1:.2f}%'.format(isnan, 100.*isnan/total)

###missing POI2
#what percentage of POIs in the dataset have "NaN" for their total payments

isnan2 = df2["poi"][(df2["total_payments"]=="NaN")&(df2["poi"]==True)].count()
total2=df2["poi"][df2["poi"]==True].count()
print 'POI total_payments == \'NaN\': {0} people = {1:.2f}%'.format(isnan2, 100.*isnan2/total2)


###missing POI4
#10 more data points which were all POI's, and put NaN for the total payments for those folks, the numbers you just calculated would change.
#What is the new number of people of the dataset? What is the new number of folks with NaN for total payments?

total4=total+10
isnan4=isnan+10
print "new number of people of the dataset: {0}; new number of folks with Nan for total payment: {1}; people % = {2:.2f}%.".format(total4,isnan4, 100.*isnan4/total4)

###missing POI5
#What is the new number of POI's in the dataset? What is the new number of POI's with NaN for total_payments?

total5=total2+10
isnan5=isnan2+10
print "new number of people of the dataset: {0}; new number of folks with Nan for total payment: {1}; people % = {2:.2f}%.".format(total5,isnan5, 100.*isnan5/total5)




