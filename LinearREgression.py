import numpy as np


ages = [25, 30, 35, 40, 45, 50]
experience = [1, 3, 5, 7, 9, 11]
# Target: Income
income = [25000, 28000, 35000, 37000, 40000, 42000]

# Step 2: Create feature matrix with bias (intercept) column
X = np.column_stack((np.ones(len(ages)), ages, experience))  # Shape: (6, 3)

# Step 3: Create target vector
y = np.array(income)  # Shape: (6,)

# Step 4: Apply Normal Equation
w = np.linalg.pinv(X.T @ X) @ X.T @ y


# Step 5: Display the learned weights
print(f"Intercept (b0): {w[0]:.2f}")
print(f"Weight for Age (b1): {w[1]:.2f}")
print(f"Weight for Experience (b2): {w[2]:.2f}")

# Step 6: Test prediction
test_age = 33
test_exp = 4
predicted_income = w[0] + w[1] * test_age + w[2] * test_exp
print("Predicted Income "
      ":",predicted_income)
