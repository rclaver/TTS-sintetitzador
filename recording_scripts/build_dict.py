#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
proces:
   - create .lab files with record_samples.py
   - add phoneset automatically to yam file
   - create dictionary word level
'''
import sys
sys.path.append('../')
from catala_transcriber import transcribe
import glob
import codecs

outdict = codecs.open('ca.dict', 'w', encoding='utf-8')
transDict = {}

for file in glob.iglob('data/*.lab'):
   text = codecs.open(file, 'r', encoding='utf-8').read()
   for word in text.split(' '):
      if word:
         transcription = transcribe(word)
         transcription = ' '.join(transcription)
         transDict[word] = transcription

[outdict.writelines(item[0]+' '+item[1]+ '\n') for item in list(sorted(transDict.items()))]
outdict.close()
