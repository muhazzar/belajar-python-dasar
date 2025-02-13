#Latihan konversi fahrenheit ke kelvin
fahrnht = float(input("masukan suhu fahrenheit :"))
print("suhu fahrenheit :",fahrnht)

kelvin = 5/9*(fahrnht-32)+273
print("suhu dalam kelvin :\n",kelvin)



#Latihan konversi kelvin ke fahrenheit
k = float(input("masukan suhu kelvin :"))
print("suhu kelvin :",k)

f = (k - 273) * (9/5) + 32
print("suhu dalam fahrenheit :",f)