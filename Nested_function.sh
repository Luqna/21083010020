#!/bin/bash

#mendeklarasikan fungsi
nama() {
   echo "siapa namamu?"
   read nama
   npm			#<-------- memanggil fungsi di dalam fungsi
}
npm() {
   echo "sebutkan npm-mu"
   read npm
   echo -e "selamat datang $nama dengan npm $npm, \n selamat datang di praktikum sistem operasi yang seru ini ya!"
}

#memanggil fungsi
nama
