data_nama = "aloy"
data_umur = 18
data_tinggi = 150.9

#string standar
data_str = f"nama : {data_nama}, umur : {data_umur}, tinggi : {data_tinggi}\n"
print(data_str)

#string multiline 1
data_str = f"nama : {data_nama} \numur : {data_umur} \ntinggi : {data_tinggi}"
print(data_str)

#string multiline 2
data_str = f"""
nama : {data_nama}
umur : {data_umur}
tinggi : {data_tinggi}
"""
print(data_str)