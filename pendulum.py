import cv2
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

video = cv2.VideoCapture('TrabalhoPendulo.mp4')
fps = video.get(cv2.CAP_PROP_FPS)

t_l, x_l, y_l = [], [], []
frame_count = 0

while True:
    ret, frame = video.read()
    if not ret:
        break
    
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    _, mascara = cv2.threshold(cinza, 100, 255, cv2.THRESH_BINARY_INV)
    contornos, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contornos) > 0:
        maior_contorno = max(contornos, key=cv2.contourArea)
        M = cv2.moments(maior_contorno)

        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            
            t_l.append(frame_count / fps)
            x_l.append(cx)
            y_l.append(cy)

    frame_count += 1

video.release()

tabela = pd.DataFrame({
    'Tempo (s)': t_l,
    'X (px)': x_l,
    'Y (px)': y_l
})

tabela.to_csv('tabela_pendulo.csv', sep='\t', index=False)

def oscilador(t, A, b, w, phi, offset):
    return A * np.exp(-b * t) * np.cos(w * t + phi) + offset

t_array = np.array(t_l)
x_array = np.array(x_l)

A_chute = (np.max(x_array) - np.min(x_array)) / 2
offset_chute = np.mean(x_array)
chute_inicial = [A_chute, 0.1, 5.0, 0.0, offset_chute]

parametros, _ = curve_fit(oscilador, t_array, x_array, p0=chute_inicial)
A, b, w, phi, offset = parametros

Q = w / (2 * b)

print(f"Amplitude (A): {A:.2f} pixels")
print(f"Constante (b): {b:.4f}")
print(f"Frequência Angular (w): {w:.4f} rad/s")
print(f"Constante de Fase (phi): {phi:.4f} rad")
print(f"Fator de Qualidade (Q): {Q:.2f}")

plt.figure(figsize=(10, 5))
plt.scatter(t_array, x_array, color='red', s=10, label='Dados do Vídeo')
plt.plot(t_array, oscilador(t_array, A, b, w, phi, offset), color='blue', linewidth=2, label='Ajuste Matemático')

plt.title('Oscilador Harmônico Amortecido - Pêndulo')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição X (pixels)')
plt.legend()
plt.grid(True)
plt.show()