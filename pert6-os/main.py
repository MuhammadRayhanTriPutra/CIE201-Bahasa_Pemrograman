import os

# TUGAS 1
os.system("clear")
namaFolder = "."
namaFile = "data_matkul.txt"

with open(namaFile, "w") as file:
    file.write("NAMA MATA KULIAH : Bahasa Pemrograman\n")
    file.write("SKS              : 3\n")
    file.write("SEMESTER         : 2\n")

print("File berhasil dibuat")

# TUGAS 2
print(f"===== ISI FILE : {namaFile} #1 =====")

with open(namaFile, "r") as file:
    isi = file.read()
    print(isi)

# TUGAS 3
with open(namaFile, "w") as file:
    file.write("NAMA MATA KULIAH : Bahasa Pemrograman\n")
    file.write("SKS              : 3\n")
    file.write("SEMESTER         : 2\n")
    file.write("DOSEN PANGAMPU   : Ibu Ranny Meilisa, S.Kom., M.Pd.T.\n")

print("File berhasil diedit\n")

print(f"===== ISI FILE : {namaFile} #2 =====")

with open(namaFile, "r") as file:
    isi = file.read()
    print(isi)

# TUGAS 4
with open(namaFile, "r") as file:
    isi = file.readlines()
    print(f"Total Jumlah baris di file : {len(isi)}")
