from numpy import *
import operator
def knn(k,testdata,traindata,labels):
    traindatasize=traindata.shape[0] #get row
    # tile can creat new array in some regulation
    # tile（a,(c,b))
    #tile(testdata,(traindatasize,1)) creat same length array as traindata
    dif=tile(testdata,(traindatasize,1))-traindata # get diff
    dif=dif**2 #get square
    sumdif=dif.sum(axis=1)# axis=1 sum row axis=0 sum column
    distance=sumdif**0.5
    indexdistance=distance.argsort()#from less to more return index
    count={}
    for i in range(0,k): #get k distance
        vote=labels[indexdistance[i]] # get labels
        count[vote]=count.get(vote,0)+1 # find the key and +1
    sortcount=sorted(count.items(),key=operator.itemgetter(1),reverse=True)#
    return sortcount[0][0]





