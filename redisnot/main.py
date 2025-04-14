import socket
from .constants import *
import time


def main():
    server_socket = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP
    )
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    connection, client_address = server_socket.accept()
    print(f"Successfully connected to {client_address}", flush=True)
    while True:
        try:
            data = connection.recv(BUFSIZE)
            print(data, flush=True)
            if not data:
                break
            connection.sendall(b"+PONG\r\n")
        except:
            print("Client closed connection", flush=True)
            break
    connection.close()
    print(f"Closed connection to {client_address}", flush=True)


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
