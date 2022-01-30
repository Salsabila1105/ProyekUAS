#RICECOOKER
#ubah objek
class TV:
# atribut
  Channel = ['rcti', 'tvri', 'Global tv']
  #ChannelTambahan = ['Indosiar', 'MNCTV', 'SCTV']
  #Channel.extend(ChannelTambahan)

  #methode constructor / __init__
  def __init__ (self, brand, size,):
    #assignment / memasukan ke variabel class
    self.brand = brand 
    self.size = size

#Menyalakan tv
  def menyalakanTV(self):
    self.tvmenyala = True
    print("tv menyala")

#metode / fungsi menambah channel dan menghapus channel
  def tambahChannel (self, chanel):
    if (self.tvmenyala):
      self.Channel.append(chanel)
      print('channel ditambahkan')
    else:
      print('tv belum menyala')

      
  def hapusChannel (self, chanel):
     if (self.tvmenyala):
      self.Channel.remove(chanel)
      print('Channel dihapus')
    else:
      print('tv belum menyala')
#membuat objek dari class tv

tv_kamar = TV ('TCL', '32inc')
#addChannel
##print(tv_kamar.Channel)

#menghapus channel 
#tv_kamar.Channel.remove("tvn")
tv_kamar.menyalakanTV()
tv_kamar.tambahChannel('TVN')
print(tv_kamar.Channel)

tv_kamar.hapusChannel('Global tv')
print(tv_kamar.Channel)
#masukan fungsi input di console
#tambah child class


