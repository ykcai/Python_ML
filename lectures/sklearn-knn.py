from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(data.iloc[:, 0:4], data['Name'])

# Predicted class
print(neigh.predict(test))
# -> ['Iris-virginica']

# 3 nearest neighbors
print(neigh.kneighbors(test)[1])
# -> [[141 139 120]]
