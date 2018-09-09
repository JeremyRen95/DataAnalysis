import numpy as np
import os

def img2vec(filename):
    returnmat = np.zeros((1,1024))
    with open(filename) as fr:
        for i in range(32):
            line = fr.readline()
            for j in range(32):
                returnmat[0,32*i+j] = int(line[j])
    return returnmat

def kNNDigital():
    #build testDigits matrixs
    TrainSamplenum = len(os.listdir("trainingDigits"))
    TrainMat = np.zeros((TrainSamplenum,1024))
    TrainLabels = []
    Trainnamelist = os.listdir("trainingDigits")
    for i in range(TrainSamplenum):
        labelGet = int(Trainnamelist[i].split('_')[0])
        TrainLabels.append(labelGet)
        TrainMat[i,:] = img2vec("trainingDigits/"+Trainnamelist[i])
    Testnamelist = os.listdir("testDigits")
    TestSamplenum = len(Testnamelist)
    ErrorCount = 0
    for j in range(TestSamplenum):
        Testdata = img2vec("testDigits/"+Testnamelist[j])
        TestdataRes = Testnamelist[j].split('_')[0]
        error = (np.tile(Testdata,(TrainSamplenum,1)) - TrainMat)**2
        error = error.sum(axis=1)
        sqerror = error**0.5
        ResultIndice = Trainnamelist[sqerror.argsort()[0]].split('_')[0]
        if TestdataRes != ResultIndice: ErrorCount += 1
    return float(ErrorCount/TestSamplenum)

print(kNNDigital())
#print(img2vec("testDigits/0_0.txt")[0,13:18])