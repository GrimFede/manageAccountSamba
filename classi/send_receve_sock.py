import socket
class SRS:
    def __init__( self, connessione ):
        self.__conn = connessione
    def invia(self, s):
        self.__conn.sendall(s.encode())
    def ricevi(self):
        s = ""
        data = self.__conn.recv(1024)
        return data.decode("utf-8")