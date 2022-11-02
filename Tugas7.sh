#!/bin/bash

#medeklarasikan fungsi
input(){
   input1=$1
   input2=$2
   echo "panjangnya: $input1"
   echo "lebarnya: $input2"
}

echo "masukkan panjangnya:"
read a
echo "masukkan lebarnya:"
read b

persegi() {
   let c=$a*$b
   echo $c
}

printf "\n"
input $a $b
printf "maka hasilnya: "
persegi $c
