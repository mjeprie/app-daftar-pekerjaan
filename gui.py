from functions import get_pekerjaan, tulis_pekerjaan
import PySimpleGUI as sg
import time
import os

if not os.path.exists('data.txt'):
    with open('data.txt', 'w') as file:
        pass

sg.theme('DarkPurple1')

time_label = sg.Text('', key='waktu')
judul_label = sg.Text("Tambahkan pekerjaan:")
input_box = sg.InputText(tooltip="Pekerjaan baru", key='pekerjaan')
add_button = sg.Button('Add', key='Add')
list_box = sg.Listbox(values=get_pekerjaan(),
                      key='tampilkan',
                      enable_events=True,
                      size=(75,10))
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('Daftar Pekerjaan',
                   layout=[[time_label],
                           [judul_label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]])

while True:
    event,values = window.read(timeout=500)
    print(f"event: {event}")
    print(f"values: {values}")
    window['waktu'].update(value=time.strftime("%A, %B %e, %Y %H:%M:%S"))
    match event:

        case 'Add':
            pekerjaan_baru = values['pekerjaan']
            pekerjaan_baru = pekerjaan_baru.capitalize()
            tulis_pekerjaan('\n', 'a')
            tulis_pekerjaan(pekerjaan_baru, 'a')
            window['tampilkan'].update(values=get_pekerjaan())
            window['pekerjaan'].update(value='')

        case 'Edit':
            try:
                pekerjaan_edit = values['tampilkan'][0]
                pekerjaan_baru = values['pekerjaan'].capitalize()
                list_pekerjaan = get_pekerjaan()
                nomor_pekerjaan = list_pekerjaan.index(pekerjaan_edit)
                list_pekerjaan[nomor_pekerjaan] = pekerjaan_baru
                list_pekerjaan[nomor_pekerjaan] += '\n'
                tulis_pekerjaan(list_pekerjaan)
                window['tampilkan'].update(values=list_pekerjaan)
                window['pekerjaan'].update(value=pekerjaan_baru)
            except:
                sg.popup('Pilih dulu pekerjaan yang akan diedit.')

        case 'tampilkan':
            window['pekerjaan'].update(value=values['tampilkan'][0])

        case 'Complete':
            try:
                list_pekerjaan = get_pekerjaan()
                list_pekerjaan.remove(values['pekerjaan'])
                tulis_pekerjaan(list_pekerjaan)
                window['tampilkan'].update(values=get_pekerjaan())
                window['pekerjaan'].update(value='')
            except:
                sg.popup('Pilih dulu pekerjaan yang akan dihapus.', title='Peringatan')

        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break
window.close()
