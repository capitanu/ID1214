from sklearn import tree
# LABELS: 0 - Arch; 1 - Manjaro; 2 - Ubuntu; 3 - Linux Mint
# FEATURES:
# Feature 1: Has used Windows in the last 12 months: 0 - False; 1 - True
# Feature 2: Has used a Linux Machine in the last 12 months: 0 - False; 1 - True
# Feature 3: Does know how to operate a computer: 0 - No; 1 - Basics; 2 - Pretty good; 3 - Expert
# Feature 4: Wants to learn more about Linux: 0 - False; 1 - True
# Feature 5: Knows how to code: 0 - False; 1 - True
# Feature 6: Knows how to install an operating system without help: 0 - False; 1 - True
# Feature 7: Has used Mac in the last 12 months: 0 - False; 1 - True
# Feature 8: Years of experience in Software Development
features = [[1,0,1,0,0,0,0,0],[1,1,2,1,1,1,0,3],[1,0,2,0,1,1,0,4],[0,0,0,0,0,0,1,0],[0,1,3,1,1,1,0,10],[0,1,2,0,1,1,0,1],[1,1,1,0,1,0,0,2],[0,1,3,1,1,1,1,12],[1,1,3,0,1,1,0,6],[0,0,1,0,0,1,1,1],[1,1,2,0,0,1,0,0],[1,0,1,1,0,1,0,0],[1,0,2,1,1,1,1,8],[1,1,2,1,1,1,1,3],[0,0,3,0,1,1,1,3],[1,0,1,1,0,0,0,2],[1,0,2,0,1,0,0,1],[1,1,2,1,1,1,0,2]]

labels = [3,1,2,3,0,1,2,0,0,1,0,1,0,1,1,3,2,2]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[1,1,2,0,1,1,0,3]]))
