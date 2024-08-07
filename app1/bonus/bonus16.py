import FreeSimpleGUI as sg
import zip_creator

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
button1 = sg.FilesBrowse(button_text="Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
button2 = sg.FolderBrowse(button_text="Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Bonus 16 - File Compressor",
                   layout=[[label1, input1, button1],
                           [label2, input2, button2],
                           [compress_button],
                           [output_label]])

while True:
    event, values = window.read()
    filepaths = values["files"].split(";")
    folder = values["folder"]
    zip_creator.make_archive(filepaths, folder)
    window["output"].update(value="Compression completed!")
    match event:
        case sg.WIN_CLOSED:
            break

window.close()