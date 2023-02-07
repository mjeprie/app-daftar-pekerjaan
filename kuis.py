from functions import get_pekerjaan, tulis_pekerjaan
import PySimpleGUI as sg

soal_label = sg.Text("Soal:")
pilihan_a_radio = sg.Radio("Pilihan A",'pilihan')
pilihan_b_radio = sg.Radio("Pilihan B",'pilihan')
pilihan_c_radio = sg.Radio("Pilihan C",'pilihan')
pilihan_d_radio = sg.Radio("Pilihan D",'pilihan')
jawab_button = sg.Button('Jawab')

window = sg.Window('Daftar Pekerjaan',
                   layout=[[soal_label],
                           [pilihan_a_radio],
                           [pilihan_b_radio],
                           [pilihan_c_radio],
                           [pilihan_d_radio],
                           [jawab_button]])

while True:
    event,values = window.read()
    print(f"event: {event}")
    print(f"values: {values}")
    match event:

        case 'Jawab':

            for key, value in values.items():
                print(key, value)

        case sg.WIN_CLOSED:
            break
window.close()
