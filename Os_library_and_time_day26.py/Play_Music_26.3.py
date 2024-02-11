import pygame
import os
import time

def play():
    pygame.mixer.init()
    pygame.mixer.music.load('audio.wav')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        stop_playback = input("Press 2 anytime to stop playback and go back to the menu : ")
        if stop_playback == '2':
            pygame.mixer.music.stop()
            return

while True:
  os.system("cls")
  print("...🎧 M U S I C  P L A Y E R 🎧... ")
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  print("Press anything else to see the menu again")
  userInput = int(input())
  if userInput == 1:
    print("Playing some proper tunes!")
    play()
  elif userInput == 2:
    exit()
  else :
    continue