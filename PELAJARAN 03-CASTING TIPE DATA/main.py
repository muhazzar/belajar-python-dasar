#CASTING TIPE DATA (MERUBAH SATU TIPE KE TIPE YG LAIN)

## MERUBAH TIPE DATA INTEGER
data_int = 10
print(data_int,type(data_int))

#INT -> STR
data_str = str(data_int)
print(data_str,type(data_str))

#INT -> FLOAT
data_float = float(data_int)
print(data_float,type(data_float))

#INT -> BOOL
data_bool = bool(data_int)
print(data_bool,type(data_bool))#hasilnya false jika nilai integernya = 0


print()


## MERUBAH DATA FLOAT
data_float = 9.5
print(data_float,type(data_float))

#FLOAT -> INT
data_int = int(data_float)
print(data_int,type(data_int))#nilai akan dibulatkan ke bawah

#FLOAT -> STR
data_str = str(data_float)
print(data_str,type(data_str))

#FLOAT -> BOOL
data_bool = bool(data_float)
print(data_bool,type(data_bool))


print()


## MERUBAH TIPE DATA BOOLEAN
data_bool = True
print(data_bool,type(data_bool))

#BOOL -> INT
data_int = int(data_bool)
print(data_int,type(data_int))

#BOOL -> STR
data_str = str(data_bool)
print(data_str,type(data_str))

#BOOL -> FLOAT
data_float = float(data_bool)
print(data_float,type(data_float))

print()


## MERUBAH TPE DATA STRING
data_str = "10"
print(data_str,type(data_str))

#STR -> INT (jika nilai data string = "huruf" maka tidak bisa)
data_int = int(data_str)
print(data_int,type(data_int))

#STR -> FLOAT (jika nilai data string = "huruf" maka tidak bisa)
data_float = float(data_str)
print(data_float,type(data_float))

#STR -> BOOL (hasil akan True kecuali nilai data string = " ")
data_bool = bool(data_str)
print(data_bool,type(data_bool))