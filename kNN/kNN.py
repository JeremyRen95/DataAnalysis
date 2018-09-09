import numpy as np

def knn_classfy(inx,Dataset,labels,k): #inx:the data need to classfied
    #get distance inx from DataSet
    DataSetSize = Dataset.shape[0]
    ErrorData = np.tile(inx,(DataSetSize,1))-Dataset #func:tile is repeat inx DataSetSize times

    sqErrorData = ErrorData**2
    sqDistance = sqErrorData.sum(axis=1)
    Distance = sqDistance**0.5
    sortindex = Distance.argsort()
    classcount = ['a','a','a']
    for i in range(k):
        classcount[i] = labels[sortindex[i]]
    return classcount[0]

data = np.array([[1,6],[1,2],[1,3]])
labels = ['james','jeremy','jim']
aa = knn_classfy([0,0],data,labels,3)
print(aa)