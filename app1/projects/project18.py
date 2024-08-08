import FreeSimpleGUI as sg

sg.theme("DarkPurple4")

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
output = sg.Text(key="output")

window = sg.Window("Convertor",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_button, exit_button, output]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()

    match event:
        case "Convert":
            feet = float(values["feet"])
            inches = float(values["inches"])

            feet = feet + (inches / 12)
            meters = feet / 3

            window["output"].update(value=f"{meters} m")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()