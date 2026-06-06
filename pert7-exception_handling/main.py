# Menangani pembagian NOL
try:
  angka1 = int(input(f"Masukan angka ke-1 : "))
  angka2 = int(input(f"Masukan angka ke-2 : "))
  print(f"{angka1} / 0 = ", angka1/0)
  print(f"{angka2} / 0 = ", angka2/0)
except ZeroDivisionError:
  print("Error : Tidak bisa di bagi dengan 0")

# Menangani Kesalahan Input
try:
  umur = int(input("Masukan umur anda : "))
  print(f"Umur anda : {umur}")
except ValueError:
  print("Error : Tidak bisa memasukan huruf, masukan ANGKA")

# Menangani File - 1
import os
namaFile = "Mahasiswa.txt"
try:
  with open(namaFile, "r") as file:
    isi = file.read()
    print(isi)
except FileNotFoundError:
  print(f"Error : File bernama {namaFile} tidak ditemukan")

# Menangani File - 2
try:
  with open(namaFile, "w") as file:
    file.write("NAMA : Muhammad Rayhan Tri Putra \n")
    file.write("NIM  : 20250801080")
  with open(namaFile, "r") as file:
    isi = file.read()
    print(isi)
except FileNotFoundError:
   print(f"Error : File bernama {namaFile} tidak ditemukan")

# Menggunakan Else dan Finally
try:
  angka = int(input("Masukan angka : "))
finally:
  print("Program selesai")

# Custom Exception
try:
  nilai = int(input("Masukan nilai mahasiswa : "))
  if nilai < 0 or nilai > 100:
    raise ValueError
  else:
    print(f"Nilai mahasiswa : {nilai}")
except ValueError:
  print(f"Error : Nilai yang dimasukan kurang dari 0 atau lebih dari 100 : {nilai}")

# Sistem ATM Sederhana
try:
  saldo = 5000000
  withdraw = int(input("Berapa yang ingin di ambil dari bank : "))
  if withdraw > saldo:
    print(f"Saldo anda tidak cukup untuk menarik : {withdraw:,}")
  else:
    print(f"Anda menarik saldo : {withdraw:,} \nSisa saldo anda : {saldo - withdraw:,}")
except ValueError:
  print(f"Error : Masukan ANGKA bukan huruf atau simbol")
finally:
  print("Transaksi selesai")