import PySimpleGUI as sg

label1 = sg.Text('Select files:')
input_box1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text('Destination:')
input_box2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window('Zip My Files', layout=[[label1, input_box1, choose_button1],
                                           [label2, input_box2, choose_button2],
                                           [compress_button]])
window.read()
window.close()