#***************************#
#  Made By: Rico Alexander  #
#  Version: Alpha Testing   #
#  (Requires an internet    #
#        connection)        #
#***************************#

#python chat.py 10.0.0.94

import socket, threading, sys

def read_file(filename):
    f = open(filename,'r')
    line = f.readline()
    f.close()
    return line

def write_file(filename,text):
    f = open(filename,'w')
    f.write(text)
    f.close()

write_file("port.txt", str(int(read_file("port.txt"))+1))
num = int(read_file("num.txt"))
port = int(raw_input("Enter a port:"))
username = raw_input("Eneter a Username:")
#port, num = int(read_file("port.txt")), int(read_file("num.txt"))
print "Num:",num
print "Port:",port
print("System is normal\n\nWaiting for connection\n")

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sock.bind(('0.0.0.0', port))
        self.sock.listen(1)

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
                c, a = self.sock.accept()
                cThread = threading.Thread(target=self.handler, args=(c,a))
                cThread.daemon = True
                cThread.start()
                self.connections.append(c)
                print("Connection found!\n\n")
                print("Current connections:")
                print(self.connections)

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def sendMsg(self):
        while True:
            self.sock.send(bytes(raw_input("")))
        
    def __init__(self, adress):
        global num
        print "Num:",num
        print "Client port is:",port
        print "Atempting port:",port-num
        print("Connection succsesful!")
        self.sock.connect((adress, port-num))
        num += 1
        write_file("num.txt",str(num))
        num = int(read_file("num.txt"))
        print num-1,"connections\nWaiting for",str(num)+"rd"

        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print "\n"+username+":"
            print(data)
            print("")

if (len(sys.argv) > 1):
    client = Client(sys.argv[1])
else:
    write_file("num.txt", "1")
    server = Server()
    server.run()





