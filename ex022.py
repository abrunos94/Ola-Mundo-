# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame

# Inicializa o pygame e o mixer de som
pygame.init()
pygame.mixer.init()

# Define o volume (0.0 até 1.0)
pygame.mixer.music.set_volume(1.0)

# Carrega o arquivo de áudio .wav
pygame.mixer.music.load("lofi_beat_30s.mp3")

# Reproduz a música
pygame.mixer.music.play()

# Mantém o programa aberto enquanto o som estiver tocando
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
