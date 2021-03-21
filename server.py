import socket

host = ''
port = 5560

storedValue = 'HelloWorld'

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("socket bind complete")
    return s

def setupConnection():
    s.listen(1) # allows 1 connection at a time
    conn, address = s.accept()
    print("connected to: " +address[0] + str(address[1]))
    return conn
        
def GET():
    reply = storedValue
    return reply

def REPEAT(dataMessage):
    reply = dataMessage[1]
    return reply

def dataTransfer(conn):
    # Loop that sends /receives data until told to stop
    while True:
        # receive data
        data = conn.recv(1024) # receive data (buffersize)
        data = data.decode('utf-8')
        # split data to separate command from the rest of the data
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]
        if command == 'GET':
            reply = GET()
        elif command == 'REPEAT':
            reply = REPEAT(dataMessage)
        elif command == 'EXIT':
            print("our client has left")
            break
        elif command == 'KILL':
            print("our server is shutting down")
            s.close()
            break
        else:
            reply = 'unknown command'
        # send reply back to client
        conn.sendall(str.encode(reply))
        print("data has been sent")
    conn.close()

s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break