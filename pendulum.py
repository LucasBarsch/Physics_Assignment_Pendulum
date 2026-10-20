import cv2
import numpy as np
import pandas as pd

video = cv2.VideoCapture('pendulo.mp4')
fps = video.get(cv2.CAP_PROP_FPS)

tempo_l, x_l, y_l = [], [], []
frame_count = 0