import numpy as np
from sklearn.linear_model import LogisticRegression


def eDiag(x):
    # Load data
    factors = np.load('P7_x.npy')
    effect = np.load('P7_y.npy').ravel()  # Reshape y to 1d array


    # Initialize and train the model
    model = LogisticRegression()
    model.fit(factors, effect)

    # Make predictions
    predictions = model.predict(x)

    return predictions

if __name__ == '__main__':
    x = np.array([[5, 65, 4, 5, 3],
                  [4, 72, 1, 3, 3],
                  [2, 32, 2, 3, 3]])

    y = eDiag(x)
    print('Prediction:', y)

    Words = ['negative', 'positive']
    for i, yi in enumerate(y):
        print(f"Patient {i}'s result is {Words[yi]}.")

    # Evaluate the model (optional)
    # y_pred = eDiag(x_test)
    # accuracy = accuracy_score(y_test, y_pred)
    # print('Accuracy:', accuracy)
