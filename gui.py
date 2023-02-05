import functions
import PySimpleGUI as sg

label = sg.Text("Tambahkan pekerjaan:")
input_box = sg.InputText(tooltip="Pekerjaan baru")
add_button = sg.Button("Add")
window = sg.Window('Daftar Pekerjaan', layout=[[label], [input_box, add_button]])
window.read()
window.close()
