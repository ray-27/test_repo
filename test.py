
# if torch.cuda.is_available():
#     DEVICE = "cuda"
# elif torch.backends.mps.is_available():
#     DEVICE = "mps"
# else: DEVICE = "cpu"
# print(f'device model is running on : {DEVICE}')

import test_repo.fun as f

def train(a):

    print("yeah this is test")
    f.pri(a)

train(5)