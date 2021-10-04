import deepface.DeepFace
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt

detector = deepface.DeepFace.analyze("neutral.jpg")
print(detector)