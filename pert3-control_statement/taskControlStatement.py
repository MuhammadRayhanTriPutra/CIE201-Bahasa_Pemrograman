nilai = 80
if nilai >= 75:
  print("Anda Lulus")
else:
  print("Anda tidak Lulus!")

print("For Loop :")
for i in range(10):
  print("Perulangan ke-",i)

print("\n")
print("While Loop :")
i = 1;
while i <= 5:
  print(i)
  i+=1

print("Kontrol dalam Loop [BREAK] :")
for i in range(10):
  if i == 5:
    break
  print(i)

print("\n")
print("Kontrol dalam Loop [CONTINUE] :")
for i in range(5):
  if i == 2:
    continue
  print(i)

print("\n")
print("Kontrol dalam Loop [PASS] :")
for i in range(3):
  pass

print("=====PENENTU GANJIL GENAP=====")
angka = int(input("Masukan angka anda: "))

if angka%4 == 0:
  print("Angka anda Genap")
elif angka%5 == 0:
  print("Angka anda Ganjil")
else:
  print("TIDAK BISA")