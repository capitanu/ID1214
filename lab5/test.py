from sklearn import tree 
# features[1] = 1 - smooth; 0 - bumpy
# label = 1 - orange; 0 - apple
features = [[140, 1], [130,1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[150,0]]))





