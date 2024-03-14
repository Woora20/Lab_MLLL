import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def load_data(file_path):
    with open(file_path, "rb") as fh:
        loaded_data = pickle.load(fh)
    return loaded_data

data = load_data("P3_data.pkl")
xs, ys = data['X'], data['Y']

def DPolyPredict(x):
    degree = 7
    x_train, x_test, y_train, y_test = train_test_split(xs, ys, test_size=0.30)

    model = make_pipeline(PolynomialFeatures(degree=degree), LinearRegression())
    model.fit(x_train.reshape(-1, 1), y_train)
    x = np.array(x).reshape(-1, 1)
    y_pred = model.predict(x)

    return y_pred.flatten()

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    
    plt.plot(xs, ys, 'k.')
    xp = np.linspace(0, 3, 200)
    yp = DPolyPredict(xp)
    plt.plot(xp, yp, 'r--')
    plt.show()
