inputs = [
    [1, 3],  # 2*1 + 3*3 = 11
    [2, 1],  # 2*2 + 3*1 = 7
    [3, 2],  # 2*3 + 3*2 = 12
    [4, 1]   # 2*4 + 3*1 = 11
]
target = 13

weights = [0, 0]
bias = 0
learning_rate = 0.01

for epoch in range(1000):
    total_error = 0
    for x in inputs:
        output = weights[0]*x[0] + weights[1]*x[1] + bias
        error = target - output
        total_error += abs(error)

        weights[0] += learning_rate * error * x[0]
        weights[1] += learning_rate * error * x[1]
        bias += learning_rate * error

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Weights: {weights}, Bias: {bias}, Total Error: {total_error}")

    if total_error < 0.01:
        print("Converged.")
        break

# Testing
for x in inputs:
    output = weights[0]*x[0] + weights[1]*x[1] + bias
    print(f"Input: {x}, Predicted Output: {output}, Target: {target}")
