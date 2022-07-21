import torch
from torch import nn, optim
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self, n_features):
        super(Model, self).__init__()
        self.layer1 = nn.Linear(n_features, 6)
        self.layer2 = nn.Linear(6, 15)
        self.layer3 = nn.Linear(15, 4)
    
    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        x = F.softmax(self.layer3(x), dim=1)
        
        return x