# Soal 1
NIM = 20250801080;
IPK = 3.99;
nama = "rayhan";
lulus = True;
matkul = ["Algoritma", "Bahasa Pemrograman", "Kalkulus"];

print("=====SOAL 1=====")
print(f"NIM       : {NIM}, Tipe Data: ", type(NIM))
print(f"IPK       : {IPK}, Tipe Data: ", type(IPK))
print(f"Nama      : {nama}, Tipe Data: ", type(nama))
print(f"Lulus     : {lulus}, Tipe Data: ", type(lulus))
print(f"Matakuliah: {matkul}, Tipe Data: ", type(matkul))

print("\n")

# Soal 2
data = {
    "nama" : "Rayhan",
    "NIM" : 20250801080,
    "prodi" : "Teknik Informatika",
    "semester" : 2
};

print("=====SOAL 2=====")
print(data, "\n")
print(data["nama"], type(data["nama"]))
print(data["NIM"], type(data["NIM"]))
print(data["prodi"], type(data["prodi"]))
print(data["semester"], type(data["semester"]))

print("\n")

# Soal 3
angka1 = 10;
angka2 = 12.2;

print("=====SOAL 3=====")
print(f"Nilai variabel / objek angka1:", angka1, type(angka1), id(angka1))
print(f"Nilai variabel / objek angka2:", angka2, type(angka2), id(angka2))
