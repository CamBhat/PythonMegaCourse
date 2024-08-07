import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("Bonus 16 - File Compressor",
                   layout=[[label1, input1, button1],
                           [label2, input2, button2],
                           [compress_button]])
window.read()
window.close()