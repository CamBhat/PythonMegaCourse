import FreeSimpleGUI as sg
import zip_extractor

sg.theme("DarkPurple4")

label1 = sg.Text("Select archive:")
input1 = sg.Input()
button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select destination:")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
label_extract = sg.Text(key="label_extract", text_color="green")

window = sg.Window("Archive Extractor",
                   layout=[[label1, input1, button1],
                           [label2, input2, button2],
                           [extract_button],
                           [label_extract]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    match event:
        case "Extract":
            archive_path = values["archive"]
            dest_path = values["folder"]
            zip_extractor.extract_archive(archive_path, dest_path)
            window["label_extract"].update(value="Archive extracted!")
        case sg.WIN_CLOSED:
            break

window.close()