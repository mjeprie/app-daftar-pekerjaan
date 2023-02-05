from functions import get_pekerjaan, tulis_pekerjaan
from time import strftime


print('===  Daftar Pekerjaan  ===')
print(strftime("%A, %e %B %Y"))

while True:
    print()
    print("""Pilih salah satu perintah:
1. Tampilkan | 2. Tambah | 3. Edit | 4. Hapus | 5. Keluar""")

    pilihan_user = input().lower()

    if pilihan_user.startswith('1'):
        print('Daftar Pekerjaan:')
        list_pekerjaan = get_pekerjaan()
        for index, item in enumerate(list_pekerjaan):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif pilihan_user.startswith('2'):
        print("Pekerjaan baru:", end=' ')
        pekerjaan_baru = input()
        pekerjaan_baru = pekerjaan_baru.capitalize()
        tulis_pekerjaan('\n', 'a')
        tulis_pekerjaan(pekerjaan_baru, 'a')

    elif pilihan_user.startswith('3'):
        print('Nomor pekerjaan yang akan diubah:', end=' ')
        list_pekerjaan = get_pekerjaan()
        nomor_pekerjaan = int(input())
        nomor_pekerjaan -= 1
        pekerjaan_lama = list_pekerjaan[nomor_pekerjaan]
        pekerjaan_lama = pekerjaan_lama.strip('\n')
        print('Pekerjaan baru:', end=' ')
        pekerjaan_baru = input()
        pekerjaan_baru = pekerjaan_baru.capitalize()
        list_pekerjaan[nomor_pekerjaan] = pekerjaan_baru
        list_pekerjaan[nomor_pekerjaan] += '\n'
        tulis_pekerjaan(list_pekerjaan)
        # with open() as file:
        #     file.writelines()
        print(f"{pekerjaan_lama} sudah diganti dengan {pekerjaan_baru}.")

    elif pilihan_user.startswith('4'):
        print('Nomor pekerjaan yang sudah selesai:', end=' ')
        list_pekerjaan = get_pekerjaan()
        nomor_pekerjaan = int(input())
        nomor_pekerjaan -= 1
        pekerjaan_lama = list_pekerjaan.pop(nomor_pekerjaan)
        pekerjaan_lama = pekerjaan_lama.strip('\n')
        tulis_pekerjaan(list_pekerjaan)
        print(f"{pekerjaan_lama} sudah dihapus.")

    elif pilihan_user.startswith('5'):
        break

    else:
        print('Input tidak dikenali.')

print('Program ditutup')
