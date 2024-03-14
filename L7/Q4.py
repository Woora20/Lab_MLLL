import numpy as np

# Given training and validation errors for polynomial degrees 1 to 9
degrees = np.arange(1, 10)
training_errors = np.array([3.28041, 2.84517, 2.84324, 0.06642, 0.06547, 0.01351, 0.00002, 0.00001, 0.00000])
validation_errors = np.array([0.09207, 0.23039, 0.24427, 0.06274, 0.04612, 0.13232, 0.66764, 0.65973, 0.78241])

# Q4.1: Model with the lowest validation error is likely to have better generalization
best_model_degree = degrees[np.argmin(validation_errors)]
print(f"Q4.1. The best generalization model = {best_model_degree}")

# Q4.2: Model suffering from overfitting the most
overfitting_model_degree = degrees[np.argmax(validation_errors - training_errors)]
print(f"Q4.2. The most overfitting model = {overfitting_model_degree}")

# Given training and validation errors for models A, B, C, D
models = ['A', 'B', 'C', 'D']
training_errors = np.array([925.6229, 189.6254, 189.1378, 152.3213])
validation_errors = np.array([1172.9233, 107.1493, 106.7562, 152.8397])

# Q4.3: Model with the lowest validation error is likely to have better generalization
best_model_index = np.argmin(validation_errors)
best_model = models[best_model_index]
print(f"Q4.3. The best generalization model = {best_model}")

# Q4.4: Model suffering from overfitting the most
overfitting_model_index = np.argmax(validation_errors - training_errors)
overfitting_model = models[overfitting_model_index]
print(f"Q4.4. The most overfitting model = {overfitting_model}")
