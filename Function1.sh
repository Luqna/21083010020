#!/bin/bash

#mendeklarasikan fungsi
nama() {
   echo "siapa namamu?"
   read nama
}
npm() {
   echo "berapa npm-mu?"
   read npm
   echo -e "hai $nama dengan $npm, selamat datang \n pada praktikum sistem operasi yang seru ini yaa!"
}

#memanggil fungsi
nama
npm
