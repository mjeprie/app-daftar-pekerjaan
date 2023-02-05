FILEPATH = 'data.txt'

def get_pekerjaan(filepath = FILEPATH):
    """Membaca data pekerjaan dari file"""
    with open(filepath) as file:
        list_pekerjaan = file.readlines()
    return list_pekerjaan


def tulis_pekerjaan(pekerjaan, mode = 'w', filepath = FILEPATH):
    """Menulis data pekerjaan ke dalam file"""
    with open(filepath, mode) as file:
        file.writelines(pekerjaan)
