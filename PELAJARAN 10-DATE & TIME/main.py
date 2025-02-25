import datetime as dt

#ngecek hari
print('Masukan tanggal lahir')
tanggal = int(input('Tanggal : '))
bulan = int(input('Bulan : '))
tahun = int(input('Tahun : '))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(tanggal_lahir)
print(f"hari: {tanggal_lahir:%A}")

sekarang = dt.date.today()
print(f"Today : {sekarang}")
umur_hari = sekarang - tanggal_lahir
print(f"umur anda: {umur_hari}")
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365)//30
print(f"umur anda: {umur_tahun} tahun {umur_bulan_sisa} bulan")