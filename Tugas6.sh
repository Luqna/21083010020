#!/bin/bash

echo "banyak nilai yang akan di masukkan:" 
read ipk

jumlah=0;
ipk_mhs=0;

for ((i=1; i<=ipk; i++))
do
	echo "nilai ke $i: "
	read tulis[$i]
	let jumlah=$jumlah+${tulis[i]};
	let ipk_mhs=$jumlah/$ipk; 
done

echo "IPS mhs: " $jumlah/$ipk
echo "IPK mhs: " $ipk_mhs
