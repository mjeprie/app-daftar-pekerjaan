from functions import get_pekerjaan, tulis_pekerjaan
import PySimpleGUI as sg

sg.theme('GreenTan')

label = sg.Text("Tambahkan pekerjaan:")
input_box = sg.InputText(tooltip="Pekerjaan baru", key='pekerjaan')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=get_pekerjaan(),
                      key='tampilkan',
                      enable_events=True,
                      size=(75,10))
edit_button = sg.Button('Edit')

window = sg.Window('Daftar Pekerjaan',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button]])

while True:
    event,values = window.read()
    print(f"event: {event}")
    print(f"values: {values}")
    match event:
        case 'Add':
            pekerjaan_baru = values['pekerjaan']
            pekerjaan_baru = pekerjaan_baru.capitalize()
            tulis_pekerjaan('\n', 'a')
            tulis_pekerjaan(pekerjaan_baru, 'a')
            window['tampilkan'].update(values=get_pekerjaan())
            # window['pekerjaan'].update(values='[]')
        case 'Edit':
            pekerjaan_edit = values['tampilkan'][0]
            pekerjaan_baru = values['pekerjaan'].capitalize()
            list_pekerjaan = get_pekerjaan()
            nomor_pekerjaan = list_pekerjaan.index(pekerjaan_edit)
            list_pekerjaan[nomor_pekerjaan] = pekerjaan_baru
            list_pekerjaan[nomor_pekerjaan] += '\n'
            tulis_pekerjaan(list_pekerjaan)
            window['tampilkan'].update(values=list_pekerjaan)
        case 'tampilkan':
            window['pekerjaan'].update(value=values['tampilkan'][0])


        case sg.WIN_CLOSED:
            break
window.close()
