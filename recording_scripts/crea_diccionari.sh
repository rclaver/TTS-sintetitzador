#!/bin/bash

source ~/bin/colores
echo -e "${CB_WHT}===================================================="
echo -e "${CB_BLU}Crea un diccionari fonètic català ${C_NONE}"
echo -e "${CB_WHT}====================================================${C_NONE}"

#lee el directori data (cada arxiu conté una única línia de text)
for arxiu in $(ls -v data/*.lab); do
   linia=$(cat $arxiu)  #captura el text de l'arxiu
   echo $arxiu :: $linia
   n=0
   words=( $linia )  #crea una matriu de paraules a partir de la línia
   for w in ${words[@]}; do
      #per a cada paraula crea un arxiu fonètic
      echo $((++n)) $w
      transcripcio=$(echo $w | espeak-ng -vca -b1 -xq)
      #afegeix la paraula i la seva transcripció al diccionari català
      echo -e "$w\t$transcripcio" >> ca.dict
   done
done