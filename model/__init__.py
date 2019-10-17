from .inceptionv4 import InceptionV4
from .resnet import ResNet50, ResNet101
from .pasnet import PNASNet5Large
from .alexnet import AlexNet
from .lenet import LeNet
from .dark_53 import Darknet53
from .identityLayer import IdentityNet


models = dict(
    inceptionv4=InceptionV4,
    resnet50=ResNet50,
    resnet101=ResNet101,
    pnasnet5=PNASNet5Large,
    alexnet=AlexNet,
    lenet=LeNet,
    darknet=Darknet53,
)
