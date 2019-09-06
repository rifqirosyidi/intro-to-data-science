from sklearn import tree

#  Height, Weight, Size (Shoes)
X = [[180, 88, 44], [170, 70, 43], [160, 60, 38], [154, 54, 37],
     [166, 57, 40], [190, 90, 47], [175, 75, 40], [159, 80, 66],
     [171, 75, 42], [181, 70, 44], [173, 73, 35]]

Y = ['male', 'female', 'female', 'female',
     'female', 'male', 'male', 'female',
     'male', 'male', 'male']

# Classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

# Predict data
prediction = clf.predict([[140, 90, 45]])
print(prediction)
