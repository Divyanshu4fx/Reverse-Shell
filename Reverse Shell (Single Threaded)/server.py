import socket
import sys
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
        print("....................................")
    except socket.error as msg:
        print("Socket binding error : "+str(msg))
        print("Trying again...")
        bind_socket()

def send_command(conn):
    while True:
        cmd=input("> ")
        if(cmd=="quit"):
            conn.send(str.encode(cmd))
            print("Program Exit...")
            sys.exit()
            return
        if(len(str.encode(cmd))>0):
            conn.send(str.encode(cmd))
            response=conn.recv(1024).decode("utf-8")
            if(response!=" "):
                print(response,end="")
        response=conn.recv(1024).decode("utf-8")
        print(response,end="")

def accept_socket():
    print("Listenig for connection...")
    conn,address=server.accept()
    print("Connection Successful")
    print("IP : "+address[0]+" on Port : "+str(address[1]))
    msg=conn.recv(1024)
    print(msg.decode("utf-8"),end="")
    send_command(conn)
    conn.close()
    server.close()

def main():
    create_socket()
    accept_socket()

main()