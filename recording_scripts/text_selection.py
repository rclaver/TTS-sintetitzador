#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs
import re
import sys; sys.path.append('../')
from catala_transcriber import transcribe

text_original = 'textos/selva_frases.txt'
arxiu_scores = 'textos/selva_score.txt'
arxiu_frases = 'textos/selva_trans.txt'

phoneDict = {}
selectedSentences = []

def broadSelection(corpora):
    sentences = codecs.open(corpora, 'r', encoding='utf-8').read().replace('\n', '.').split('.')
    for sentence in sentences:
        sentence = sentence.replace('-', '')
        sentence = re.sub("([^a-z' \.àèéíòóúç0-9])", " ", sentence.lower())
        sentence = re.sub(' +', ' ', sentence).strip()
        # sentence = sentence.replace(u'—', '').replace('_', '').replace('*', '').replace('"', '').replace(',', '').replace(u'¿', '').replace('  ', ' ')
        # sentence = sentence.replace(u'!', '').replace(u'¡', '').replace(':', '').replace(';', '').replace('\f', '').replace(u'?', '')
        if not re.findall(r'[0-9]', sentence) and len(sentence) < 100:
            transcription = transcribe(sentence)
            for phone in transcription:
                if phone not in phoneDict:
                    phoneDict[phone] = 0
                    selectedSentences.append((sentence, transcription))
                    break

def scoreSelection(transcripted_sentences):
    f = open(arxiu_scores, "w")
    scores = []
    for transcription in transcripted_sentences:
       sc = (len(set(transcription[1])), transcription)
       f.write(f"{sc[0]}"); f.write(sc[1]); f.write(f"\n")
       scores.append(sc)
       #scores.append((len(set(transcription[1])), transcription))
    f.close()
    scores = sorted(scores, key=lambda x: x[0])
    print("SCORES:", scores)
    return scores

def countCoverage(transcripted_sentences):
    for transcription in transcripted_sentences:
        for phone in transcription[1][1]:
           if phone not in phoneDict: phoneDict[phone] = 0
           phoneDict[phone] += 1



if __name__ == "__main__":
   broadSelection(text_original)
   scoresSentences = scoreSelection(selectedSentences)
   countCoverage(scoresSentences)
   for p in phoneDict:
       print(p, phoneDict[p])

   N = 20
   outf = codecs.open(arxiu_frases, 'w', encoding='utf-8')
   for sentence in scoresSentences[N:]:
       outf.writelines(sentence[1][0].strip()+'\n')
   outf.close()
