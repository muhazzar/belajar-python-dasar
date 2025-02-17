##operator dalam bentuk method

# menghitung char dalam string
nama_lengkap = "apipiii"
jumlah_i = nama_lengkap.count("i")
print(jumlah_i)


# mengubah case dari string
data = "SpidermaN"

print(data.upper())#semuanya jadi uppercase
print(data.lower())#semuanya jadi lowcase


# mengecek dengan is method

#isupper untuk ngecek uppercase
data01="gakhit"
cekUpp=data01.isupper()
print(bool(cekUpp))

#islower untuk ngecek lowercase
cekLow=data01.islower
print(bool(cekLow))

#isalpha() untuk ngecek huruf
alpha="bangkong"
print("alpha = ",alpha.isalpha())

#isalnum() untuk ngecek angka dan huruf
alnum="1234yo"
print("alnum = ",alnum.isalnum())

#isdecimal() untuk ngecek angka
decim="12345"
print("decim = ",decim.isdecimal())

#isspace() untuk ngecek spasi,tab,newline
spas="\n \t "
print("spas = ",spas.isspace())

#istitle()untuk ngecek awal kata diawali dgn huruf besar
title="Spider Man"
print("title = ",title.istitle())


# ngecek komponen 
cekstartend="babang tamvan"
#startswith()
print("cekstart = ",cekstartend.startswith("babang"))
#endswith()
print("cekend = ",cekstartend.endswith("tamvan"))  


# penggabungan komponen
#join()
data02=['ryo','yamada','dumb']
print(data02)
print(" ".join(data02))

#split()
data03="ryo@yamada@dumb"
print(data03)
print(data03.split("@"))


#alokasi karakter
#rjust()
print("awok".rjust(30))
#center()
print("awok".center(30))
#ljust()
print("awok".ljust(30))