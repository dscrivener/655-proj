import torch
from PIL import Image
from torchvision import transforms

class ImgModel:

    def __init__(self):
        # self.model = torch.hub.load('pytorch/vision:v0.10.0', 'squeezenet1_0', weights='SqueezeNet1_0_Weights.DEFAULT')
        self.model = torch.hub.load('pytorch/vision:v0.10.0', 'squeezenet1_1', pretrained=True)
        self.preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def process(self, img):

        # adapted from https://pytorch.org/hub/pytorch_vision_squeezenet/

        input = Image.open(img).convert('RGB')
        tensor = self.preprocess(input)
        batch = tensor.unsqueeze(0)

        with torch.no_grad():
            output = self.model(batch)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)

        with open("imagenet_classes.txt", "r") as f:
            categories = [s.strip() for s in f.readlines()]
        # return best guess
        best_prob, best_description = torch.topk(probabilities, 1)
        return "-".join([categories[best_description[0]], str(best_prob[0].item())])
