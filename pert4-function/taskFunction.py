def tambah(a, b):
  return a+b

def kurang(a, b):
  return a-b

def kali(a, b):
  return a*b

def bagi(a, b):
  return a/b

for i in range(3*4):
  print("Pilih operasi: + - / *")
  pilih = input("Masukan pilihan operasi: ")

  a = float(input("Angka pertama: "))
  b = float(input("Angka kedua: "))

  if pilih == "+":
    print(tambah(a, b))
  elif pilih == "-":
    print(kurang(a, b))
  elif pilih == "/":
    print(bagi(a, b)-)
  elif pilih == "*":
    print(kali(a, b))
  else:
    print("Operasi tidak valid / tidak ada!")