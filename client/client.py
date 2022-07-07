import PySimpleGUI as sg
import socket
import time
import psutil 
import multiprocessing


def menu(ip,port):
    layout = [[sg.Text('Connected to server')], [sg.Button('Stop')]]
    window = sg.Window('Client Startup', layout,margins=(100, 50),element_justification='c')
    th = multiprocessing.Process(target=run,args=(ip,port))
    th.start()
    while True:
        event, values = window.read(10)
        if not th.is_alive():
            window.close()
            return
        if event == "Stop":
            th.terminate()
            window.close()
            exit()
def run(host,port):
    print("Connecting to server...")
    HEADERSIZE = 10
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except:
        layout = [[sg.Text('Server not found')], [sg.Button('Ok')]]
        window = sg.Window('Error', layout,margins=(100, 50),element_justification='c')
        event, values = window.read()
        if event == 'Ok':
            window.close()
            return
    print("Connected to server")

    msg=s.recv(35)
    msg=msg.decode("utf-8")
    print(msg)

    while True:
        time.sleep(1)
        msg = f"{psutil.cpu_percent()}"+"-"+f"{psutil.virtual_memory()[2]}"+"-"+f"{psutil.disk_usage('c:')[3]}"+"-"+f"{socket.gethostbyname(socket.gethostname())}"
        msg = f"{len(msg):<{HEADERSIZE}}"+msg

        print(msg)

        s.send(bytes(msg,"utf-8"))      