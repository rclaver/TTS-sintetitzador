#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Gravació d'audios breus a partir de frases curtes
'''
import pyaudio
import wave
import codecs
import random
import os

C_NONE="\033[0m"
CB_GRN="\033[1;32m"
CB_YLW="\033[1;33m"
CB_WHT="\033[1;37m"

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1       # channels, must be one for forced alignment toolkit to work
RATE = 16000       # freqüència de mostreig (sample rate)
RECORD_SECONDS = 5 # nombre de segons de temps per poder dir la frase

text_de_lectura = 'textos/frases.txt'

# recording function
def record(text, file_name):
   #os.system('clear')
   print(f"\n{CB_GRN}** Gravant **{C_NONE}")
   print(f"{CB_WHT}Llegeix en veu alta:{CB_YLW}", end=" "); print("\'{}\' ".format(text)); print(C_NONE, end="")

   p = pyaudio.PyAudio()
   stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

   frames = []
   for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
      data = stream.read(CHUNK)
      frames.append(data)

   stream.stop_stream()
   stream.close()
   p.terminate()

   wf = wave.open(file_name, 'wb')
   wf.setnchannels(CHANNELS)
   wf.setsampwidth(p.get_sample_size(FORMAT))
   wf.setframerate(RATE)
   wf.writeframes(b''.join(frames))
   wf.close()
   os.system('clear')

def main(nom, sentence_txt):
   sentence_set = codecs.open(sentence_txt, 'r', ).read().split('\n')
   random.shuffle(sentence_set)
   print(f"{CB_WHT}Si estàs preparat, prem la tecla 'Retorn'{C_NONE}")
   input()
   os.system('clear')
   for n in range(0, len(sentence_set)):
      if sentence_set[n]:
         record(str(n)+':'+'\t'+sentence_set[n], 'data/'+str(n)+'_'+nom+'.wav' )
         outxt = open('data/'+str(n)+'_'+nom+'.lab', 'w')
         outxt.write(sentence_set[n])
         outxt.close()

   print(f'\n{CB_GRN}** Fi de la gravació **{C_NONE}\n')

# inici
main('mostra', text_de_lectura)
