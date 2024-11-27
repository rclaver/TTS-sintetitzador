#!/bin/bash

source ~/bin/colores
echo -e "${CB_WHT}===================================================="
echo -e "${CB_BLU}Crea un diccionari fonètic català ${C_NONE}"
echo -e "${CB_WHT}====================================================${C_NONE}"

frases_origen="data/*.lab"
arxiu_caracters="ca.char"
arxiu_diccionari="ca.dict"

# elimina, si existeixen, els arxius de sortida
if [ -f $arxiu_caracters ]; then rm $arxiu_caracters; fi
if [ -f $arxiu_diccionari ]; then rm $arxiu_diccionari; fi

# llegeix el directori data (cada arxiu conté una única línia de text)
for arxiu in $(ls -v $frases_origen); do
   linia=$(cat $arxiu)  #captura el text de l'arxiu
   echo $arxiu :: $linia
   n=0
   words=( $linia )  #crea una matriu de paraules a partir de la línia
   for w in ${words[@]}; do
      # per a cada paraula crea un arxiu fonètic
      echo $((++n)) $w
      transcripcio=$(echo $w | espeak-ng -vca -b1 -xq)
      # afegeix la paraula i la seva transcripció al diccionari català
      #echo -e "$w\t$transcripcio" >> $arxiu_diccionari

      # split i separació dels caracters de la transcripció
      #car=$(echo $transcripcio|sed -E -e '/(.)/\1 /g')
      car=""
      for (( i=0 ; i < ${#transcripcio} ; i++ )) {
          car+="${transcripcio:i:1} "
          echo -e "${transcripcio:i:1}" >> $arxiu_caracters
      }
      car="${car:0:${#car}-1}"   #elimina l'últim espai blanc

      # afegeix la paraula i la seva transcripció al diccionari català
      echo -e "$w\t$car" >> $arxiu_diccionari
   done
done