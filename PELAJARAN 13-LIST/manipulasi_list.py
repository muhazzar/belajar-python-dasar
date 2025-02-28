
data_nama = ["Ambatukir","Asep knalpot","Agung useup"]

# mengambil data
print(data_nama[0])#memunculkan data index 0
print(data_nama[1])#memunculkan data index terakhir

# mengambil info jumlah data
print(len(data_nama))

#menambah item .insert
data_nama.insert(1,"Ambagong")
print(data_nama)

# menambah item di akhir .append
data_nama.append("Muklis")
print(data_nama)

#menggabungkan list .extend
data_lain = ["Gorillazz","Kong","Bokir"]
data_nama.extend(data_lain)
print(data_nama)

#merubah data
data_nama[3] = "Tepen"
print(data_nama)

#remove data
data_nama.remove("Ambagong")
print(data_nama)

#remove data akhir
data_nama.pop()
print(data_nama)