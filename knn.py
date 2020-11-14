import torch
import torchvision
import torchvision.transforms as transforms

transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,0.5,0.5), 
(0.5,0.5,0.5))])

trainset = torchvision.datasets.CIFAR10(root='./data', train = True, download = True, transform = transform)
#Why does it have a trainset and a trainloader? Doesn't the above already do the job?
trainloader = torch.utils.data.DataLoader(trainset, batch_size = 4, shuffle = True, num_workers = 2)
# It is loading the trainset from previous. 
testset = torchvision.datasets.CIFAR10(root = './data', train=False, download=True, transform=transform)


nn = torch.NearestNeighbor()