import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = load_iris()
X_labeled = iris.data
y_labeled = iris.target

# Generate a larger pool of unlabeled data (you can choose to replicate the labeled data for this example)
X_unlabeled = np.concatenate([X_labeled, X_labeled])
y_unlabeled = np.concatenate([y_labeled, np.full_like(y_labeled, -1)])  # Using -1 as placeholder for unlabeled data

# Split the labeled data into train and test sets
X_train_labeled, X_test_labeled, y_train_labeled, y_test_labeled = train_test_split(X_labeled, y_labeled, test_size=0.2, random_state=42)

# Initialize a logistic regression model with a higher max_iter value
model = LogisticRegression(max_iter=1000)

# Train the model on the small labeled dataset
model.fit(X_train_labeled, y_train_labeled)

# Use the model to predict labels for the unlabeled data
pseudo_labels = model.predict(X_unlabeled)
X_pseudo_labeled = X_unlabeled[pseudo_labels != -1]
y_pseudo_labeled = pseudo_labels[pseudo_labels != -1]

# Combine the pseudo-labeled data with the original labeled data
X_combined = np.vstack((X_labeled, X_pseudo_labeled))
y_combined = np.concatenate((y_labeled, y_pseudo_labeled))

# Retrain the model on the expanded labeled dataset
model.fit(X_combined, y_combined)

# Evaluate the model on the test set
accuracy = model.score(X_test_labeled, y_test_labeled)
print(f"Accuracy after semi-supervised learning: {accuracy}")
