import math

print("============= OPERASI DERET =============")
print("|   1. Deret Aritmatika                 |")
print("|   2. Deret Bilangan Rill              |")
print("|   3. Deret Bilangan Ganjil            |")
print("|   4. Deret Bilangan Genap             |")
print("|   5. Keluar                           |")
print("=========================================")
print(" ")

user =int(input("Masukkan angka dari pilihan diatas, lalu tekan enter untuk memulai ^^ ---------> "))

if user==1:
    print("================================ DERET ARITMATIKA =================================")
    print("Selamat Datang pada program perhitungan deret aritmatika, sebelum itu mohon masukkan ketentuan dibawah agar kami dapat menghitungnya ^^")
    print(" ")
    u1=int(input("masukkan nilai U1:"))
    u2=int(input("masukkan nilai U2:"))
    n=int(input("masukkan nilai ke-n:"))
    print(" ")
    b=u2-u1
    un= u1+(n-1)*b
    print("+++ DIKETAHUI +++")
    print("nilai b:",b)
    print("nilai un:", un) 
    print(" ") 
    print("+++ DERETNYA +++")
    i=u1
    while i <= un:
        print(i)
        i=i+b
    print(" ")
    print("Terimakasih telah menggunakan program ini")
    print("Semoga sehat selalu ^^") 

elif user==2:
    print("============================== DERET RILL ========================================")
    print("Selamat Datang pada program perhitungan deret bilangan Rill, sebelum itu mohon masukkan ketentuan dibawah agar kami dapat menghitungnya ^^")
    print(" ")
    a=int(input("Masukkan batas nilai awal: "))
    b=int(input("Masukkan batas nilai akhir: "))
    print(" ")
    p=a+1
    print("+++ DERETNYA +++")
    y=a
    while y <= b:
        print(y)
        y=y+1
    print(" ")
    print("Terimakasih telah menggunakan program ini")
    print("Semoga sehat selalu ^^")
    print(" ")


elif user==3:
    print("=================================== DERET GANJIL ==========================================")
    print("Selamat Datang pada program perhitungan deret bilangan ganjil, sebelum itu mohon masukkan ketentuan dibawah agar kami dapat menghitungnya ^^")
    print(" ")
    awal=int(input("Masukkan batas awal:"))
    akhir=int(input("Masukkan batas akhir:"))
    print(" ")
    print("+++ DIKETAHUI +++")
    print("Batas awal:", awal)
    print("Batas akhir:", akhir)
    print(" ")
    print("+++ DERETNYA +++")
    if awal%2==1:
        x=awal
        while akhir >= x:
            print(x,)
            x=x+2
    elif awal%2==0:
        print("Mohon maaf batas awal yang anda masukkan bernilai genap :(")
    else:
        print("Mohon maaf kami tidak mengeri")
    print("")
    print("Terimakasih telah menggunakan program ini")
    print("Semoga sehat selalu ^^")
    print(" ")

elif user==4:
    print("=============================== DERET GENAP ==================================")
    print("Selamat Datang pada program perhitungan deret bilangan genap, sebelum itu mohon masukkan ketentuan dibawah agar kami dapat menghitungnya ^^")
    print(" ")
    awal=int(input("Masukkan batas awal:"))
    akhir=int(input("Masukkan batas akhir:"))
    print(" ")
    print("+++ DIKETAHUI +++")
    print("Batas awal:", awal)
    print("Batas akhir:", akhir)
    print(" ")
    print("+++ DERETNYA +++")
    if awal%2==0:
        x=awal
        while akhir >= x:
            print(x,)
            x=x+2
    elif awal%2==1:
        print("Mohon maaf batas awal yang anda masukkan bernilai ganjil :(")
    else:
        print("Mohon maaf kami tidak mengeri")
    print("")
    print("Terimakasih telah menggunakan program ini")
    print("Semoga sehat selalu ^^")
    print(" ")

elif user==5:
    print("=================== TERIMAKASIH TELAH DATANG ==================")
    print("                       SEMOGA SEHAT SELALU                     ")

else:
    print("=================== Mohon maaf kami tidak mengerti :( =================")

