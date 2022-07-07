import PySimpleGUI as sg
import client
if __name__ == '__main__':
    sg.theme('DarkTeal4')   # Add a touch of color
    layout = [[sg.Text('Connect to Server')],[sg.Text('Enter host IP'), sg.InputText()],[sg.Text('Enter port'), sg.InputText()], [sg.Button('Connect'),sg.Button('Cancel')]]
    window = sg.Window('Client Startup',  layout,margins=(100, 50),element_justification='c')
    event, values = window.read()
    if event == 'Connect':
        window.close()
        client.menu(values[0],int(values[1]))
    if event == 'Cancel' or event == sg.WIN_CLOSED:
        window.close()