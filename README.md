# TTS-sintetitzador

Construcció d'un sintetitzador de text-a-veu utilitzant com a mètode de síntesi la “selecció per unitats” (unit selection).

Exemple de TTS de selecció d'unitats a Python

Aquest és un exemple de joguina i una forma molt simplificada de construir un sintetitzador de selecció d'unitats amb Python.

Aquest repositori s'utilitza a l'article Medium:
https://medium.com/@pilarsoledad/construyendo-un-sintetizador-de-texto-a-voz-usando-python-y-selecci%C3%B3n-de-unidades-a5dc2e11a091

L'article només està en castellà, però bàsicament mostra com utilitzar aquests scripts per crear una veu de selecció d'unitats de joguina en espanyol.

Prerequisits:
   sudo apt install gcc-multilib libc-dev

   HTK (Hidden Markov ToolKit)
      tar xzf HTK-3.3.tar.gz
      cd htk
      export CPPFLAGS=-UPHNALG
      NO ./configure --prefix=/usr/local
      ./configure --disable-hlmtools --disable-hslab
      NO make all
      make clean
      make -j4 all
      sudo make -j4 install

   Prosodylab-Aligner
      git clone http://github.com/prosodylab/Prosodylab-Aligner
      cd Prosodylab-Aligner
      pip3 install -r requirements.txt
