class mahasiswa:
  def __init__(self, nim, nama, jurusan, alamat, tglLahir):
    self.nim = nim
    self.nama = nama
    self.jurusan = jurusan
    self.alamat = alamat
    self.tglLahir = tglLahir

mhs = mahasiswa(20250801080, "Muhammad Rayhan Tri Putra", "Teknik Informatika", "Kab. Tangerang", "Jakarta, 06 Juli 2007")

print("========== Data Mahasiswa ==========")
print(f"NIM                    : {mhs.nim}")
print(f"NAMA                   : {mhs.nama}")
print(f"JURUSAN                : {mhs.jurusan}")
print(f"ALAMAT                 : {mhs.alamat}")
print(f"TEMPAT / TGL LAHIR     : {mhs.tglLahir}")