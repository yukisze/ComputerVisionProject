# Import torch and NumPy
import torch
import numpy as np

# Set the random seed for NumPy and PyTorch both to "42"
#   This allows us to share the same "random" results.
np.random.seed(42)
torch.manual_seed(42)

# Create a NumPy array called "arr" that contains 6 random integers between 0 (inclusive) and 5 (exclusive)
arr=np.random.randint(0,5,6)
print(arr)

# Create a tensor "x" from the array above
x = torch.tensor(arr)


# Change the dtype of x from 'int32' to 'int64'
x = x.type(torch.int64)


# Reshape x into a 3x2 tensor
x = x.reshape(3,2)
print(x)

# Return the left-hand column of tensor x
print(x[:,1])

# Without changing x, return a tensor of square values of x
print(x*x)

# Create a tensor "y" with the same number of elements as x, that can be matrix-multiplied with x
y = torch.randint(10,20,[2,3])
print(y)

# Find the matrix product of x and y
print(torch.mm(x,y))

# Create a Simple linear model using torch.nn
# the model will take 1000 input and output 20 multi-class classification results.
# the model will have 3 hidden layers which include 200, 120, 60 respectively.

# initiate the model and printout the number of parameters

class model(torch.nn.Module):
    def __init__(self, input = 1000, output = 20, parameter =[200,120,60]):
        super().__init__()
        self.fc1 = torch.nn.Linear(in_features = input,out_features = parameter[0])
        self.fc2 = torch.nn.Linear(in_features = parameter[0],out_features = parameter[1])
        self.fc3 = torch.nn.Linear(in_features = parameter[1],out_features = parameter[2])
        self.fc4 = torch.nn.Linear(in_features = parameter[2],out_features = output)
    def forward(self,x):
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        x = self.fc4(x)
        return x

model_yuki=model()


for num in model_yuki.parameters():
    print(num.numel())