import numpy as np
import matplotlib.pyplot as plt

link = {'didntLike':1,'smallDoses':2,'largeDoses':3}
#reverse_link = ['didntLike','smallDoses','largeDoses']

def knn_classfy(inx,Dataset,labels,k): #inx:the data need to classfied
    #get distance inx from DataSet
    DataSetSize = Dataset.shape[0]
    ErrorData = np.tile(inx,(DataSetSize,1))-Dataset #func:tile is repeat inx DataSetSize times

    sqErrorData = ErrorData**2
    sqDistance = sqErrorData.sum(axis=1)
    Distance = sqDistance**0.5
    sortindex = Distance.argsort()
    classcount = []
    for i in range(k):
        classcount.append(labels[sortindex[i]])
    return classcount[0]

def classfier(filename):   #get data matrix and labels column
    with open(filename) as fr:
        arrayolines = fr.readlines(); #type of arrayolines is list
        lengthOfdata = len(arrayolines)
        ReturnMat = np.zeros((lengthOfdata,3));
        labels = []
        index = 0
        for line in arrayolines:
            line = line.strip() #去除头尾的空格
            arrayfromline = line.split('\t') #按照空格分离成一个新的向量
            ReturnMat[index,:] = arrayfromline[0:3] #get data matrix
            labels.append(link[arrayfromline[-1]])
            index += 1
        return ReturnMat,labels

def autoNorm(dataset):              #数据归一化
    minVals = dataset.min(0)
    maxVals = dataset.max(0)
    range = maxVals-minVals
    length = dataset.shape[0] #get the number of rows
    normDataSet = (dataset - np.tile(minVals,(length,1)))/np.tile(range,(length,1))
    return normDataSet

def dataTest():
    testper = 0.1
    dataset,labels = classfier('datingTestSet.txt')
    NumOfData = dataset.shape[0]
    NumOfTest = int(testper*NumOfData)
    NormDataSet = autoNorm(dataset)
    errorcount = 0.0
    for i in range(NumOfTest): #取前百分之十进行测试
        knn_classfy_result = knn_classfy(NormDataSet[i,:],NormDataSet[NumOfTest:NumOfData,:],labels[NumOfTest:NumOfData],3)
        print("the classifier came back with : %s,the real answer is: %s" % (knn_classfy_result,labels[i]))
        if(knn_classfy_result != labels[i]): errorcount += 1.0
    print("the total error rate id : %f",(errorcount/float(NumOfTest)))

dataTest()
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.scatter(a[:,0],a[:,1],15.0*np.array(b),15.0*np.array(b))
#plt.show()