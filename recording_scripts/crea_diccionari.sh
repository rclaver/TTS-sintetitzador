#!/bin/bash

source ~/bin/colores
echo -e "${CB_WHT}===================================================="
echo -e "${CB_BLU}Crea un diccionari fonètic català ${C_NONE}"
echo -e "${CB_WHT}====================================================${C_NONE}"

# elimina, si existeix, l'arxiu ca.dict
if [ -f ca.dict ]; then rm ca.dict; fi

# llegeix el directori data (cada arxiu conté una única línia de text)
for arxiu in $(ls -v data/*.lab); do
   linia=$(cat $arxiu)  #captura el text de l'arxiu
   echo $arxiu :: $linia
   n=0
   words=( $linia )  #crea una matriu de paraules a partir de la línia
   for w in ${words[@]}; do
      # per a cada paraula crea un arxiu fonètic
      echo $((++n)) $w
      transcripcio=$(echo $w | espeak-ng -vca -b1 -xq)
      # afegeix la paraula i la seva transcripció al diccionari català
      #echo -e "$w\t$transcripcio" >> ca.dict

      # split i separació dels caracters de la transcripció
      #car=$(echo $transcripcio|sed -E -e '/(.)/\1 /g')
      car=""
      for (( i=0 ; i < ${#transcripcio} ; i++ )) {
          car+="${transcripcio:i:1} "
          echo -e "${transcripcio:i:1}" >> ca.yaml.dict
      }
      car="${car:0:${#car}-1}"   #elimina l'últim espai blanc

      # afegeix la paraula i la seva transcripció al diccionari català
      echo -e "$w\t$car" >> ca.dict
   done
done