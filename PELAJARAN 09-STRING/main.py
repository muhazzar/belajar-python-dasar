## Cara membuat string

#1. menggunakan singgle quote '...'
data01 = '"im Batman 1"'
print(data01)

#2.menggunakan double quote "...."
data02="i'm Batman 2"
print(data02)


## membuat tanda ' menjadi string dalam string singgle quote menggunakan \
data03='i\'m Batman 3'
print(data03)

## membuat \ agar terbaca sebagai string
data04="i'm bat\\man 4"
print(data04)

# tab \t
data05="i'm \t Batman 5"
print(data05)

# newline \n
data06="i'm batman 6 \nno,i'm Batman 6"
print(data06)


## raw string (merubah semua menjadi string)
print(r"C:\new folder \todler \border \\")

## multiline literal string
print("""
Nama : Tepe
Umur : 90
""")

## multiline literal string dan raw
print(r"""
Nama : Tepe
Umur : 90
C:\new folder \todler \border \\
""")

