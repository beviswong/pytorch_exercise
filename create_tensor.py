import numpy as np
import torch

a = np.array([2, 3.3])
b = torch.tensor(a)
print("b = {}".format(b))

c = np.ones([3, 3])
d = torch.from_numpy(c)

e = np.zeros([4, 4])
print("d = {}".format(d))

f = torch.FloatTensor([3.1, 3.2])
print("f = {}".format(f))

# uninitialized.
g = torch.empty(2)
print("g = {}".format(g))

h = torch.Tensor(3, 3)
i = torch.IntTensor(3, 3)
j = torch.FloatTensor(2, 2)

print("the type of tensor is {}".format(h.type()))

# If you input the shape of tensor, the created tensor is uninitialized.
# If the val is input, the created is initialized by val.

# set default type.
torch.set_default_tensor_type(torch.DoubleTensor)


a_tensor = torch.tensor([1.0, 2.0, 3.0])
print("the type of a_tensor is {}".format(a_tensor.type()))

pass
