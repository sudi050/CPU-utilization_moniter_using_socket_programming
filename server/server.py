import socket
import PySimpleGUI as sg
from _thread import *
import multiprocessing

clientnum = 0

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def clientthread(clientsocket):
    global clientnum
    i = 0
    true=True
    while true:
        full_msg = ''
        while True:
            msg = clientsocket.recv(50)
            string=msg.decode("utf-8")
            string=string[3:].strip()
            if string:
                infolist= string.split('-')
                if not (infolist[0]==" "):
                    if not is_number(infolist[0]):
                        infolist[0]="0"
                    if not is_number(infolist[1]):
                        infolist[1]="0"
                    if not is_number(infolist[2]):
                        infolist[2]="0"
                    print("string:"+infolist[0]+" "+infolist[1]+" "+infolist[2]+" "+infolist[3],"msg:"+msg.decode("utf-8"))
                    file="data/"+str(infolist[3])+".txt"
                    f2 = open(file, "a")
                    info=str(i)+","+infolist[0]+"-"+str(i)+","+infolist[1]+"-"+str(i)+","+infolist[2]+"-"+infolist[3]+"\n"
                    f2.write(info)
                    i+=2
                    full_msg += msg.decode("utf-8")
                    print("full length:",len(full_msg))
                    f2.close()
            else:
                print("disconnected")
                clientnum -= 1
                clientsocket.close()
                break
        true=False

def run(port):
    global clientnum
    layout = [[sg.Text("Server Running")], [sg.Button("Stop Server")]]
    window = sg.Window("Server Status", layout, margins=(100, 50))
    th = multiprocessing.Process(target = findclients, args =(port, ))
    th.start()
    while True:
        event, values = window.read(10)
        if not th.is_alive():
            window.close()
            exit()
        if event == "Stop Server" or event == sg.WIN_CLOSED:
            clientnum = 0
            th.terminate()
            window.close()
            break

def findclients(port):
    global clientnum
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10000)
    host="192.168.103.234"
    s.bind((host,port))
    s.listen(5)
    while True:
        try:
            clientsocket, address = s.accept()
            print(f"Connection from {address} has been established.\n")
            clientnum += 1
            welcome = f"you are connected to {socket.gethostbyname(socket.gethostname())}"
            clientsocket.send(bytes(welcome,"utf-8"))
            start_new_thread(clientthread,(clientsocket, ))
        except: 
            pass
        if clientnum == 0:
            exit()