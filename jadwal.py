import requests
import json
import  time


kota = 'cianjur'
data_kota = json.loads(requests.get(f"https://api.myquran.com/v1/sholat/kota/cari/{kota}").text)
# print(data_kota)
print('JADWAL SHOLAT')
kode_kota = data_kota['data'][0]['id']
nama_kota = data_kota['data'][0]['lokasi']
print(nama_kota)

year = time.strftime("%Y", time.localtime())
month = time.strftime("%m", time.localtime())
date = time.strftime("%d", time.localtime())

jadwal_sholat = json.loads(requests.get(f"https://api.myquran.com/v1/sholat/jadwal/{kode_kota}/{year}/{month}/{date}").text)
print(jadwal_sholat['data']['jadwal']['tanggal'])
print(jadwal_sholat['data']['jadwal']['dzuhur'])