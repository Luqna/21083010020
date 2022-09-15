#!/bin/bash

#deklarasi Array
distrolinux=("mint" "ubuntu" "kali" "arch" "debbian")

#random distro
let pilih=$RANDOM%5

#eksekusi
echo "saya memiliih distro $pilih, ${distroLinux[$pilih]} !"

