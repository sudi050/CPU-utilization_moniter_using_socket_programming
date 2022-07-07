import graph
import os
import PySimpleGUI as sg

arr = os.listdir('data/.')

file_list_column = [
    [
        sg.Text("Choose among the following files: ")
    ],
    [
        sg.Listbox(
            values=arr, enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

layout = [[sg.Column(file_list_column)]]

window = sg.Window("File Selection", layout, margins=(100, 50))

while True:
	event, values = window.read()
	if event == "Exit" or event == sg.WIN_CLOSED:
		break
	if event == "-FILE LIST-":
		try:
			graph.graphplot(values["-FILE LIST-"][0])
			break
		except:
			pass
window.close()