#!/bin/bash

printf "jajan apa yang kamu suka? \n"
printf "pentol? \n"
printf "batagor? \n"
printf "cireng? \n"

echo "jadi apa yang kamu suka?"
read jajan

case "$jajan" in 
   "pentol")
     echo "pentol buk ma uwenak slur!"
     ;;
   "batagor")
     echo "batagore mas budi mantap bet!"
     ;;
   *)
     echo "makanan yang kamu suka gaenak hehe"
     ;;
esac
