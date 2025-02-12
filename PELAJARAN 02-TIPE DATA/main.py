#INTEGER (angka satuan)
data_01 = 10
print(type(data_01))

#FLOAT (angka dengan koma)
data_02 = 2.0
print(type(data_02))

#string (kumpulan karakter)
data_03 = 'dizz 666'
print(type(data_03))

#BOOLEAN (biner true/false)
data_04 = True
print(type(data_04))
data_05 = False
print (type(data_05))


##TIPE DATA KHUSUS

#BILANGAN KOMPLEKS
data_06 = complex(5,6)
print(type(data_06))

#tipe data dari bahsa C
from ctypes import c_double

data_07 = c_double(10.5)
print(type(data_07))