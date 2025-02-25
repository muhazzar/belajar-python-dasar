# membuat kalkulator menggunakan elif

input01 = int(input("masukan angka pertama: "))
input02 = int(input("masukan angka kedua: "))
input03 = input("masukan jenis operasi: ")

if input03 == "*":
    print("hasil:",input01 * input02)
elif input03 == "/":
    print(input01 / input02)
elif input03 == "-":
    print(input01 - input02)
elif input03 == "+":
    print(input01 + input02)
else :
    print("masukan operasi yang benar!! (*,/,-,+)")