import pytest
import threading
import time
import socket

from redisnot.main import main
from redisnot.constants import *


def test_ping_pong():
    server_thread = threading.Thread(target=main, daemon=True)
    server_thread.start()

    time.sleep(0.1)

    client = socket.socket()
    client.connect((HOST, PORT))
    client.sendall(b"*1\r\n$4\r\nPING\r\n")
    response = client.recv(BUFSIZE)

    assert response == b"+PONG\r\n", f"Expected +PONG\r\n, got {response!r}"

    client.sendall(b"*1\r\n$4\r\nPING\r\n")
    response = client.recv(BUFSIZE)

    assert response == b"+PONG\r\n", f"Expected +PONG\r\n, got {response!r}"

    client.close()
