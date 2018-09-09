import numpy as np
import matplotlib.pyplot as plt

#无监督学习 无标签
def LoadDataSet(filename):    #将文件数据存入内存
    with open(filename) as fr:
        rowdata = fr.readlines()
        length = len(rowdata)
        dataset = np.zeros((length,2))
        index = 0
        for line in rowdata:
            line = line.strip()
            curline = line.split('\t')
            dataset[index,:] = curline #type of dataset is array
            index += 1
        return dataset

def ArrayDistance(VecA,VecB):
    return np.sqrt(np.sum(np.power((VecA-VecB),2)))

def SetCluster(dataset,k):      #随机生成k个簇
    Dimension = dataset.shape[1]
    print(Dimension)
    cluster = np.mat(np.zeros((k,Dimension))) #create cluster
    for i in range(Dimension):
        datarange = float(max(dataset[:,i]) - min(dataset[:,i])) #最大值与最小值的差距
        cluster[:,i] =  datarange * np.random.rand(k,1) + min(dataset[:,i])
    return cluster

def KMeans(dataset,k):  #k为簇的个数
    datalength = len(dataset)
    cluster = SetCluster(dataset,k)
    SampleToCluster = np.mat(np.zeros((datalength,2)))
    clusterIsChange = True
    while clusterIsChange:
        clusterIsChange = False
        for i in range(datalength):
            mindis = np.inf ; minindex = -1
            for j in range(k):
                distance = ArrayDistance(dataset[i,:],cluster[j,:])
                if mindis > distance: mindis = distance; minindex = j
            if(SampleToCluster[i,0] != minindex): clusterIsChange = True ;
            SampleToCluster[i, :] = minindex, mindis
        print(cluster)
        for i in range(k):
            ptsInClust = dataset[np.nonzero(SampleToCluster[:,0].A == i)[0]] #获取第i个簇中的所有的向量
            cluster[i,:] = np.mean(ptsInClust,axis=0) #按列求平均得到全新的第i个簇

    return cluster , SampleToCluster

a = LoadDataSet('testSet.txt')
aa , bb = KMeans(a,4)
print(aa)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(a[:,0].tolist(),a[:,1].tolist(),20,15.0*bb[:,0].reshape(1,80).A[0])
ax.scatter(aa[:,0].tolist(),aa[:,1].tolist(),marker='x',color='r')
plt.show()