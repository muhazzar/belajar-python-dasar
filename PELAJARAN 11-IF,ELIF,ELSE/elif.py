# membuat kalkulator menggunakan elif

input01 = int(input("masukan angka pertama: "))
input03 = input("masukan jenis operasi: ")
input02 = int(input("masukan angka kedua: "))

if input03 == "*":
    print(input01,'x',input02,'=',input01 * input02)
elif input03 == "/":
    hasil = input01 / input02
    print(f"{input01} / {input02} =",hasil)
elif input03 == "-":
    print(f"{input01} - {input02} =",input01 - input02)
elif input03 == "+":
    print(f"{input01} + {input02} =",input01 + input02)
else :
    print("masukan operasi yang benar!! (*,/,-,+)")