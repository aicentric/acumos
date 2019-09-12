# acumos
Acumos cancer classification project



The Cancer Classification model is a model that is used to classify whether it is a Malignant or Benign breast cancer from the dataset available on https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29. The features represent characteristics of cell nuclei of images generated after the Fine Needle Aspiration Method.

The training dataset is used to train and onboard the model onto Acumos. There are 30 out of a total of 32 variables that are used to predict the classification into a Malignant or Benign Cancer category. The Training and test datasets are also uploaded on Acumos

Given below is the information about the attributes in the dataset

Attribute Information:

1) ID number

2) Diagnosis (M{0} = malignant, B{1} = benign)

3-32)



Ten real-valued features are computed for each cell nucleus:



a) radius (mean of distances from center to points on the perimeter)

b) texture (standard deviation of gray-scale values)

c) perimeter

d) area

e) smoothness (local variation in radius lengths)

f) compactness (perimeter^2 / area - 1.0)

g) concavity (severity of concave portions of the contour)

h) concave points (number of concave portions of the contour)

i) symmetry

j) fractal dimension ("coastline approximation" - 1)

To test and deploy the Model from Acumos download the .tar and .proto files from the model and create the Docker image and establish the connection to the port.

Rename the file to cancer.proto file and Run the protoc command:" protoc cancer_classify1.proto --python_out=. " which generates the pb2.py file. We can save this file in the same project folder as cancer_test.py and now test the model on the test dataset.

RandomForest Classifier is used to predict whether the cancer is Malignant or Benign and the accuracy of the classification of Malignant or Benign Cancers for the test data is 90.35%. The training and test data is derived from the original dataset in a 4:1 ratio

Training Dataset filename: cancer_train_data.csv

Testing Dataset filename: cancer_test_data.csv

You can watch the video: cancer classify.mp4 and the Acumos cancer_classify.pptx file uploaded in the Documents section for steps to run the model on your system

Data Taken From:

https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29

Data Creators:



1. Dr. William H. Wolberg, General Surgery Dept.

University of Wisconsin, Clinical Sciences Center

Madison, WI 53792

wolberg '@' eagle.surgery.wisc.edu



2. W. Nick Street, Computer Sciences Dept.

University of Wisconsin, 1210 West Dayton St., Madison, WI 53706

street '@' cs.wisc.edu 608-262-6619



3. Olvi L. Mangasarian, Computer Sciences Dept.

University of Wisconsin, 1210 West Dayton St., Madison, WI 53706

olvi '@' cs.wisc.edu
