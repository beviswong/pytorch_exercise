import torch
import numpy as np

a = torch.randn(2, 3)
print("a type is {}".format(a.type()))
print("a type is {}".format(type(a)))

r1 = isinstance(a, torch.FloatTensor)
print("r1 is {}".format(r1))

r2 = isinstance(a, torch.cuda.DoubleTensor)
print("r2 is {}".format(r2))

b = a.cuda()
r3 = isinstance(b, torch.cuda.DoubleTensor)
print("r3 is {}".format(r3))

# dimension 0 / rank 0
c = torch.tensor(1.)
print("c is {}".format(c))
d = torch.tensor(1.3)
print("d is {}".format(d))

e = torch.Size([])
print("e is {}".format(e))

# dim1 / rank 1
f = torch.tensor([1.1, 2.2])
print("f is {}".format(f))

g = torch.FloatTensor(1)
print("g is {}".format(g))

h = torch.FloatTensor(2)
print("h is {}".format(h))

i = np.ones(2)
it = torch.from_numpy(i)
print("it = {}".format(it))
print("id of i is {}".format(id(i)))
print("id of it is {}".format(id(it)))

# dim4
j = torch.rand(2, 3, 28, 28)
print("j is {}".format(j))
print("j.shape is {}".format(j.shape))
print("j.numel is {}".format(j.numel()))
print("j.dim is {}".format(j.dim()))




