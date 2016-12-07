""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
def featureScaling(data):
    new_data=[]
    base= max(data)-min(data)
    
    for i in data:
        if base==0:
            pass
        else:
	        a=float(i-min(data))/base
	        new_data.append(a)

    return new_data

    

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)


# from sklearn.preprocessing import MinMaxScaler
# import numpy
# weight = numpy.array([[115.],[140.],[175.]])
# scaler = MinMaxScaler()
# rescale_weight = scaler.fit_transform(weight)
# print rescale_weight

from sklearn.preprocessing import MinMaxScaler
import numpy
weight = feature_1
scaler = MinMaxScaler()
rescale_weight = scaler.fit_transform(200000.)
print rescale_weight
