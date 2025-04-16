import socket
from .constants import *
import time
import threading


class Server:
    def __init__(self, host=HOST, port=PORT, backlog=4, bufsize=BUFSIZE, timeout=1):
        # Actual backlog used seems to be backlog + 1.
        # Related: https://bugs.python.org/issue8498
        self.host = host
        self.port = port
        self.server_socket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP
        )
        self.bufsize = bufsize
        self.backlog = backlog
        self.timeout = timeout
        self.running = False

    def __enter__(self):
        return self

    def start(self):
        self.running = True
        self.server_socket.bind((self.host, self.port))
        self.server_socket.settimeout(self.timeout)
        self.server_socket.listen(self.backlog)
        while self.running:
            try:
                connection, client_address = self.server_socket.accept()
                handle_connection = threading.Thread(
                    target=self.handle_client, args=(connection, client_address)
                )
                handle_connection.start()
            except Exception as e:
                # Don't print exception if server stopped on purpose
                if self.running:
                    print(e, flush=True)
                break

    def handle_client(self, connection, client_address):
        print(f"Connection from {client_address} accepted", flush=True)
        while True:
            try:
                data = connection.recv(self.bufsize)
                print(f"Received {data!r} from {client_address}", flush=True)
                if not data:
                    break
                connection.sendall(b"+PONG\r\n")
            except:
                print("Client abruptly closed connection", flush=True)
                break
        connection.close()
        print(f"Closed connection to {client_address}", flush=True)

    def stop(self):
        self.running = False
        self.teardown()

    def teardown(self):
        self.server_socket.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"{exc_type}: {exc_val}", flush=True)
        self.stop()


def main():
    with Server() as server:
        server.start()


if __name__ == "__main__":
    ascii_art = r"""
                                   ,----,                                                               
         ,--.    ,----..         ,/   .`|                                                               
       ,--.'|   /   /   \      ,`   .'  :        ,-.----.       ,---,.    ,---,       ,---,  .--.--.    
   ,--,:  : |  /   .     :   ;    ;     /        \    /  \    ,'  .' |  .'  .' `\  ,`--.' | /  /    '.  
,`--.'`|  ' : .   /   ;.  \.'___,/    ,'         ;   :    \ ,---.'   |,---.'     \ |   :  :|  :  /`. /  
|   :  :  | |.   ;   /  ` ;|    :     |          |   | .\ : |   |   .'|   |  .`\  |:   |  ';  |  |--`   
:   |   \ | :;   |  ; \ ; |;    |.';  ;          .   : |: | :   :  |-,:   : |  '  ||   :  ||  :  ;_     
|   : '  '; ||   :  | ; | '`----'  |  |          |   |  \ : :   |  ;/||   ' '  ;  :'   '  ; \  \    `.  
'   ' ;.    ;.   |  ' ' ' :    '   :  ;          |   : .  / |   :   .''   | ;  .  ||   |  |  `----.   \ 
|   | | \   |'   ;  \; /  |    |   |  '          ;   | |  \ |   |  |-,|   | :  |  ''   :  ;  __ \  \  | 
'   : |  ; .' \   \  ',  /     '   :  |          |   | ;\  \'   :  ;/|'   : | /  ; |   |  ' /  /`--'  / 
|   | '`--'    ;   :    /      ;   |.'           :   ' | \.'|   |    \|   | '` ,/  '   :  |'--'.     /  
'   : |         \   \ .'       '---'             :   : :-'  |   :   .';   :  .'    ;   |.'   `--'---'   
;   |.'          `---`                           |   |.'    |   | ,'  |   ,.'      '---'                
'---'                                            `---'      `----'    '---'                             
                                                                                                        
    """
    print(ascii_art)
    main()
