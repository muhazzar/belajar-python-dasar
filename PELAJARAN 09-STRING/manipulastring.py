#concatenate (menggabungkan string)
nama1 = "Abdul"
nama2 = "Wahidi"

nama_lengkap = nama1 +' '+ nama2
print(nama_lengkap)

#menghitung panjang string (len)
jumlah_string = len(nama_lengkap)
print(jumlah_string)

#mengecek char didalam string (in)
print("d" in nama_lengkap)
print("c" in nama_lengkap)

#mengulang string
print(10*"wk")
print("ha"*20)

#indexing []
print(nama1[0])
print(nama_lengkap[0:5])

#ngecek char paling kecil
print(min(nama_lengkap))#hasilnya spasi

#ngecek char paling besar
print(max(nama_lengkap))


#operator dalam bentuk method
jumlah_i = nama_lengkap.count("i")
print(jumlah_i)