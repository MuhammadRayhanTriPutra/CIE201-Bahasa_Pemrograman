import os
os.system("clear")
class matakuliah:
  def __init__(self, namaMatakuliah, sks, dosenPengampu):
    self.namaMatakuliah = namaMatakuliah
    self.sks = sks
    self.dosenPengampu = dosenPengampu

  def tampilkanData(self):
    print(f"Nama Matakuliah : {self.namaMatakuliah}")
    print(f"SKS             : {self.sks}")
    print(f"Dosen Pengampu  : {self.dosenPengampu}\n\n\n")

matakuliah1 = matakuliah("Bahasa Pemrograman", 3, "Ibu Ranny Meilisa, S.Kom., M.Pd.T.")
matakuliah2 = matakuliah("Kalkulus 1", 3, "Pak Ir. Nixon Erzed, MT.")

matakuliah1.tampilkanData()
matakuliah2.tampilkanData()