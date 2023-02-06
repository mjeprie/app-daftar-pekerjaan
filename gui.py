from functions import get_pekerjaan, tulis_pekerjaan
import PySimpleGUI as sg

label = sg.Text("Tambahkan pekerjaan:")
input_box = sg.InputText(font=('Algerian',12),tooltip="Pekerjaan baru",key='pekerjaan')
add_button = sg.Button("Add")

window = sg.Window('Daftar Pekerjaan',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica',20))

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            print("Pekerjaan baru:", end=' ')
            pekerjaan_baru = values['pekerjaan']
            pekerjaan_baru = pekerjaan_baru.capitalize()
            tulis_pekerjaan('\n', 'a')
            tulis_pekerjaan(pekerjaan_baru, 'a')
        case sg.WIN_CLOSED:
            break
window.close()
