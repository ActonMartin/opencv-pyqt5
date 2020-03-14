import numpy as np
import random


def gauss_noise(image, var=0.1):
    image = np.array(image)
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(0, var, image.shape)
    out = image + noise
    out = np.clip(out, 0, 1.0)
    out = np.uint8(out*255)
    return out