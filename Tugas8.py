from multiprocessing import cpu_count, Pool, Process
from os import getpid
from time import time, sleep

a = int(input("masukkan batasan: "))
print(" ")
def cetak(i):
   for i in range(a):
       if i % 2 == 0:
           print(f"{i+1} Angka Ganjil"," - ID prosess", getpid())
       else:
           print(f"{i+1} Angka Genap","  - ID prosess" , getpid())
   sleep(1)


#multiprocessing sekuensial
print("Multiprocessing.Sekuensial")
sekuensial_awal=time()

for i in range(1):
   cetak(i)
sekuensial_akhir=time()
print(" ")


#multiprocessing Process
print("Multiprocessing.Process")
kumpulan_proses=[]
proses_awal=time()

for i in range(1):
   p= Process(target=cetak, args=(i,))
   kumpulan_proses.append(p)
   p.start()
for i in kumpulan_proses:
   p.join()
proses_akhir=time()
print(" ")


#multiprocessing Pool
print("Multiprocessing.Pool")
pool_awal = time()
pool = Pool()
pool.map(cetak, range(0,1))
pool.close()
pool_akhir=time()
print(" ")


#waktu eksekusi
print("Waktu eksekusi Sekuensial             : ",sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi Multiprocessing.Process: ",proses_akhir - proses_awal, "detik")
print("Waktu eksekusi Multiprocessing.Pool   : ",pool_akhir - pool_awal, "detik")
