echo "----------mari kita membandingkan sebuah angka!!----------"
echo "masukkan angka a: "
read a
echo "masukkan angka b: "
read b

echo "maka bagaimana nilai a terhadap nilai b?"
sleep 2

#menggunakan percabangan 1
if [ $a -gt $b ]
then
   echo "benar, nilainya memang lebih besar"
elif [ $a -lt $b ]
then
   echo "benar, nilainya memang lebih kecil"
elif [ $a -eq $b ]
then
   echo "benar, nilainya sama"
else
   echo "sayang sekali, kamu salah :("
fi
sleep 3

#penjumlahan
echo "----------mari kita berlatih penjumlahan----------"
sleep 2
echo "masukkan nilai x: "
read x
echo "masukkan nilai y: "
read y
let a=$x+$y
echo "maka hasil dari $x + $y = $a"

sleep 1.5
#bertanya
echo "apakah menyenangkan? (iya/tidak)"
read tanya
if [ $tanya == "iya" ]
then
   echo "mari berjumpa lagi ^^"
elif [ $tanya == "tidak" ]
then
   echo "terus semangat :)"
else
   echo "aku tidak mengerti :("
fi
