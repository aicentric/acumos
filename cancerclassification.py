# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 23:32:55 2018

@author: rhutvij
"""

from acumos.session import AcumosSession
from acumos.modeling import Model, List, create_dataframe

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

dataset = pd.read_csv('cancer_train_data.csv')
X = dataset.iloc[:, 2:33].values
y = dataset.iloc[:, 1].values

        
        


# Feature Scaling of training data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X)


classifier = RandomForestClassifier(random_state=0)
classifier.fit(X_train, y)

X_df = pd.DataFrame(X, columns=['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean','smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave_points_mean','symmetry_mean', 'fractal_dimension_mean', 'radius_se', 'texture_se','perimeter_se', 'area_se', 'smoothness_se', 'compactness_se','concavity_se', 'concave_points_se', 'symmetry_se', 'fractal_dimension_se','radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst','smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave_points_worst','symmetry_worst', 'fractal_dimension_worst'])
DataFrame = create_dataframe('DataFrame', X_df)


def classify_cancer(df: DataFrame) -> List[float]:
    X1 = np.column_stack(df)
    return classifier.predict(X1)
 
model = Model(classify=classify_cancer)
 
session = AcumosSession()
 
session.dump(model,'cancer_classify','F:/project/cancer_classification')