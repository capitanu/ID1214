from sklearn import tree
# LABELS: Price: 0 - < 10 000 SEK; 1 - 10 000 SEK < x < 20 000 SEK; 2 - 20 000 SEK < x < 30 000 SEK; 3 - > 30 000 SEK
# FEATURES:
# Feature 1: Number of cores
# Feature 3: VRAM size
# Feature 4: RAM size
# Feature 5: Power draw
# Feature 6: Storage size (assuming SSD)
features = [
    [6,8,16,700,500],
    [8,8,16,500,512],
    [6,4,8,300,256],
    [6,4,8,500,512],
    [8,8,16,500,512],
    [8,16,16,750,512],
    [16,24,32,850,1000],
    [8,8,16,650,512],
    [12,10,32,750,1000]
]
labels = [1,1,0,0,1,2,3,2,2]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[16,10,64,850,1500]]))
