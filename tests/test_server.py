import pytest
import threading
import time
import socket

import redisnot.server
import redisnot.constants


@pytest.fixture
def server():
    server = redisnot.server.Server()
    server_thread = threading.Thread(target=server.start, daemon=True)
    server_thread.start()
    time.sleep(0.1)

    yield server

    server.stop()
    time.sleep(1.1)


def test_ping_pong(server):

    client = socket.socket()
    client.connect((server.host, server.port))
    client.sendall(b"*1\r\n$4\r\nPING\r\n")
    response = client.recv(redisnot.constants.BUFSIZE)

    assert response == b"+PONG\r\n", f"Expected +PONG\r\n, got {response!r}"

    client.sendall(b"*1\r\n$4\r\nPING\r\n")
    response = client.recv(redisnot.constants.BUFSIZE)

    assert response == b"+PONG\r\n", f"Expected +PONG\r\n, got {response!r}"

    client.close()
    time.sleep(0.1)


def test_concurrent_clients(server):
    clients = [socket.socket() for _ in range(10)]
    # Separated sending and receiving to monitor backlog behaviour.
    for client in clients:
        client.settimeout(1)
        client.connect((server.host, server.port))
        client.sendall(b"*1\r\n$4\r\nPING\r\n")

    for client in clients:
        response = client.recv(redisnot.constants.BUFSIZE)
        assert response == b"+PONG\r\n", f"Expected +PONG\r\n, got {response!r}"

    for client in clients:
        client.close()
