# Step 1: Data preparation
data = [
    [170, 65, 20, 'Athlete'],
    [160, 70, 25, 'Non-athlete'],
    [180, 75, 30, 'Athlete'],
    [155, 60, 22, 'Non-athlete'],
    [165, 68, 28, 'Non-athlete'],
    [175, 80, 26, 'Athlete'],
]

features = []
labels = []

for row in data:
    features.append(row[:-1])  # take first 3 values as features
    labels.append(row[-1])     # take last value as label

# Step 2: Manual Euclidean distance function
def euclidean_distance(point1, point2):
    total = 0
    for i in range(len(point1)):
        diff = point1[i] - point2[i]
        total += diff * diff
    return total ** 0.5

# Step 3: kNN implementation
def knn_predict(features, labels, query_point, k):
    distances = []
    for i in range(len(features)):
        distance = euclidean_distance(features[i], query_point)
        distances.append((distance, labels[i]))

    # Step 4: Sort distances
    distances.sort()  # sorts by first element of tuple (distance)

    # Step 5: Majority vote
    votes = {}
    for i in range(k):
        label = distances[i][1]
        if label in votes:
            votes[label] += 1
        else:
            votes[label] = 1

    # Find label with maximum votes
    max_vote = -1
    predicted_label = None
    for label in votes:
        if votes[label] > max_vote:
            max_vote = votes[label]
            predicted_label = label

    return predicted_label

# Step 6: Query
query_point = [172, 72, 24]  # Height, Weight, Age
k = 3

prediction = knn_predict(features, labels, query_point, k)
print("Predicted Label:", prediction)
