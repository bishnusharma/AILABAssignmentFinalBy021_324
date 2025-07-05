# Data for AND Gate
inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
targets = [0, 0, 0, 1]

# Initialize weights and bias
weights = [0, 0]
bias = 0
learning_rate = 1

def activation(x):
    return 1 if x > 0 else 0

# Training
for epoch in range(10):  # maximum 10 iterations
    print(f"Epoch {epoch+1}")
    error_count = 0
    for i in range(len(inputs)):
        x = inputs[i]
        target = targets[i]
        linear_output = weights[0]*x[0] + weights[1]*x[1] + bias
        output = activation(linear_output)
        error = target - output

        # Update weights and bias
        weights[0] += learning_rate * error * x[0]
        weights[1] += learning_rate * error * x[1]
        bias += learning_rate * error

        print(f"Input: {x}, Target: {target}, Output: {output}, Error: {error}, Weights: {weights}, Bias: {bias}")

        if error != 0:
            error_count += 1
    if error_count == 0:
        print("Training complete.\n")
        break

# Testing
for x in inputs:
    linear_output = weights[0]*x[0] + weights[1]*x[1] + bias
    output = activation(linear_output)
    print(f"Input: {x}, Predicted Output: {output}")
