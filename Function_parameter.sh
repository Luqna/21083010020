#!/bin/bash

identitas() {
   parameter1=$1
   parameter2=$2
   parameter3=$3
   echo "$parameter1"
   echo "$parameter2"
   echo "$parameter3"
}

echo "masukkan nama: "
read a
echo "masukkan Npm: "
read b
echo "hobimu apa: "
read c

printf "\n"
identitas $a $b $c
