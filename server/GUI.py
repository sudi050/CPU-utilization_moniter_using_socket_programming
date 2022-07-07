import PySimpleGUI as sg
import server
if __name__ == '__main__':
    layout = [[sg.Text("Start Server")],[sg.Text('Enter port'), sg.InputText()], [sg.Button("Yes"),sg.Button("No")]]
    window = sg.Window("Server Startup", layout, margins=(100, 50), element_justification='c')
    event, values = window.read()
    if event == "Yes":
        window.close()
        server.run(int(values[0]))
    if event == "No" or event == sg.WIN_CLOSED:
        window.close()