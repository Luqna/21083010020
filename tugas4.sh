#!/bin/bash

echo "masukkan sebuah angka: "
read a


echo "maka kelipatan bilangannya adalah"
until [ ! $a -gt 0 ]
do
	echo $a
	a=$((a - 2))
done
