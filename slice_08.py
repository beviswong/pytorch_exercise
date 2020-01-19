import torch

# indexing.
a = torch.rand(4, 3, 28, 28)
print("a[0].shape = {}".format(a[0].shape))
print("a[0, 0].shape = {}".format(a[0, 0].shape))
print("a[0, 0, 2, 4] = {}".format(a[0, 0, 2, 4]))

# select first/last N
print("a[ :2].shape = {}".format(a[ :2].shape))
print("a[:2, :1, :, :].shape = {}".format(a[:2, :1, :, :].shape))
print("a[:2, -1:, :, :].shape = {}".format(a[:2, -1:, :, :].shape))
