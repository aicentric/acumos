import cancer_classify1_pb2 as pb
import requests
 
restURL = "http://localhost:3330/classify"
from sklearn.preprocessing import StandardScaler

def classify_cancer (v1, v2, v3, v4,v5, v6, v7, v8,v9, v10, v11, v12,v13, v14, v15, v16,v17, v18, v19, v20,v21, v22, v23, v24,v25, v26, v27, v28,v29,v30):
    df = pb.DataFrame()

    df.radius_mean.append(v1)
    df.texture_mean.append(v2)
    df.perimeter_mean.append(v3)
    df.smoothness_mean.append(v5)
    df.compactness_mean.append(v6)
    df.concavity_mean.append(v7)
    df.concave_points_mean.append(v8)
    df.symmetry_mean.append(v9)
    df.fractal_dimension_mean.append(v10)
    df.radius_se.append(v11)
    df.texture_se.append(v12)
    df.perimeter_se.append(v13)
    df.area_se.append(v14)
    df.smoothness_se.append(v15)
    df.compactness_se.append(v16)
    df.concavity_se.append(v17)
    df.concave_points_se.append(v18)
    df.symmetry_se.append(v19)
    df.fractal_dimension_se.append(v20)
    df.radius_worst.append(v21)
    df.texture_worst.append(v22)
    df.perimeter_worst.append(v23)
    df.area_worst.append(v24)
    df.smoothness_worst.append(v25)
    df.compactness_worst.append(v26)
    df.concavity_worst.append(v27)
    df.concave_points_worst.append(v28)
    df.symmetry_worst.append(v29)
    df.fractal_dimension_worst.append(v30)
    df.area_mean.append(v4)

    r = requests.post(restURL, df.SerializeToString())

    of = pb.ClassifyOut()
    of.ParseFromString(r.content)

    return of.value[0]




import pandas as pd

test_dataset = pd.read_csv('cancer_test_data.csv')
Xtest = test_dataset.iloc[:, 2:33].values
ytest = test_dataset.iloc[:, 1].values

# Feature Scaling of training data

sc = StandardScaler()
X = sc.fit_transform(Xtest)
     
        


acc=0
tot=0
ypred=[]
for i in range(len(X)):
    tot+=1
    ypred=ypred+[classify_cancer(*(X[i]))]
    print('Predicted: {}, Actual: {}'
          .format(int(classify_cancer(*(X[i]))), ytest[i]))# -*- coding: utf-8 -*-
    if int(ypred[i])==ytest[i]:
       acc+=1
from sklearn.metrics import confusion_matrix
conmax = confusion_matrix(ytest, ypred)
print(conmax)
print('Accuracy='+str(acc/tot*100))


       
