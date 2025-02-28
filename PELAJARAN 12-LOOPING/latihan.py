# membuat segitiga dengan for loop
sisi = 5
dummy = 0

for i in range(sisi):
    dummy += 1
    print("*"*dummy)


# membuat segitiga mengguanakan while loop
dummy = 0
while True:
    dummy += 1
    print("*"*dummy)

    if dummy >= sisi :
        break
#lieurrr skip