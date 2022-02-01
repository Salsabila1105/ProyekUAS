class Ricecooker:
  # attribute / class varible
  merk = ['YoungMa', 'Cosmos', 'Philip']
  Ricecooker_menyala = False

  # method contructor / __init_ 
  def __init__ (self, mode , size):
    # asignmet / memasukan ke varible class
    self.mode = mode
    self.size = size

  # menyalakan tv
  def menyalakanRicecooker(self):
    self.Ricecooker_menyala = True
    print("Ricecooker menayala")

  # metode / funsgi menambah chanel dan menghapus chanel
  def tambahMerk(self, nama_merk):
    if(self.Ricecooker_menyala):
      self.merk.append(nama_merk)      
      print("merk ditambahkan")
    else:
      print("merk belum menayala")

  # metode / funsgi menambah chanel dan menghapus chanel
  def hapusMerk(self, nama_merk):
    if(self.Ricecooker_menyala):
      self.merk.remove(nama_merk)      
      print("merk dihapus")
    else:
      print("Ricecooker belum menayala")

class ModernRicecooker(Ricecooker):
  # app
  fitur = ['cook','warm']

  # metode / funsgi menambah apliakasi
  def tambahFitur(self, nama_aplikasi):
    if(self.Ricecooker_menyala):
      self.fitur.append(nama_aplikasi)      
      print("fitur ditambahkan")
    else:
      print("Ricecooker belum menayala")

  # metode / funsgi menghapus apliakasi
  def hapusApikasi(self, nama_fitur):
    if(self.Ricecooker_menyala):
      self.fitur.remove(nama_fitur)      
      print("fitur dihapus")
    else:
      print("Ricecooker belum menayala")

# mebuat object dari clas tv
Ricecooker_kamar = Ricecooker('YoungMa', '2Liter')
Ricecooker_tamu = ModernRicecooker('Toshiba', '3Liter')
  

while True:
  print("1) nyalakan Ricecooker")
  print("2) tambakan merk Ricecooker")
  print("3) Hapus merk Ricecooker")
  print("4) Tambah temperature")
  print("5) keluar dari program")
  pilihan = int(input("silahkan masukan pilihan anda "))
  if(pilihan == 1):
    Ricecooker_kamar.menyalakanRicecooker()
  elif(pilihan == 2):
    print('merk sekarang:')
    print(Ricecooker_kamar.merk)
    merk = input("silahkan masukan merk: ")
    Ricecooker_kamar.tambahMerk(merk)
    print('merk sekarang:')
    print(Ricecooker_kamar.merk)
  elif(pilihan == 3):
    print('merk sekarang:')
    print(Ricecooker_kamar.merk)
    merk = input("silahkan masukan merk: ")
    Ricecooker_kamar.hapusMerk(merk)
    print('merk sekarang:')
    print(Ricecooker_kamar.merk)
  elif(pilihan == 4):
    try:
      temperature = int(input('Silahkan masukan temperature : '))
      settemperature = int(input('Silahkan set temperature : '))
      newtemperature = temperature + settemperature
    except:
      print('temperature error')
      print('Temperature berhasil diubah, temperature sekarang adalah : ', newtemperature)
  elif(pilihan == 5):
    print('anda keluar program')
    break
  else:
    print('pilihan tidak ditemukan')