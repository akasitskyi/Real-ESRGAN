import torch
from .model import RealESRGAN

from PIL import Image
import numpy as np
import skimage


class Upscaler4x:
    def __init__(self):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = RealESRGAN(device)
        self.model.load_weights()

    def __call__(self, image, noise_var=0):
        img = self.model.predict(image)
        if noise_var > 0:
            npimg = skimage.util.random_noise(np.array(img), mode="gaussian", var=noise_var)
            img = Image.fromarray(np.uint8(255 * npimg))
        return img
