from socket import socket, AF_INET, SOCK_STREAM
from gc import collect
from threading import Thread


class fast_sock:
    __TCP_sock: socket
    __TCP_host: str
    __TCP_port: int
    __TCP_queue: list
    __TCP_rebind: bool
    __TCP_RECV_thread: Thread
    __TCP_peak_index: int

    def __init__(self, __TCP_host: str, __TCP_port: int) -> None:
        fast_sock.__TCP_queue = []
        self.__TCP_socket_init(__TCP_host, __TCP_port)
        self.__TCP_recv_thread()
        fast_sock.__TCP_peak_index = 0

    def TCP_send(self, data, __TCP_host="", __TCP_port=0):
        if __TCP_host != "" or __TCP_port != 0:
            if __TCP_host != fast_sock.__TCP_host or __TCP_port != fast_sock.__TCP_port:
                try:
                    self.__TCP_sock.close()
                    collect()
                    self.__TCP_socket_init(__TCP_host, __TCP_port)
                except Exception as e:
                    print(e)
        try:
            self.__TCP_sock.send(data)
        except Exception as e:
            print(e)

    def TCP_recv(self):
        while not fast_sock.__TCP_rebind:
            try:
                data = self.__TCP_sock.recv(1024)
                if data != b'':
                    if fast_sock.__TCP_queue.__len__() >= 1024:
                        collect()
                        fast_sock.__TCP_queue.pop(0)
                    fast_sock.__TCP_queue.append(data)
            except:
                pass

        collect()
        fast_sock.__TCP_rebind = True
        # self.__TCP_recv_thread()

    def TCP_peak(*index):
        if index != None:
            try:
                return fast_sock.__TCP_queue[index]
            except Exception as e:
                print(e)
                return None
        else:
            fast_sock.__TCP_peak_index += 1
            return fast_sock.__TCP_queue[fast_sock.__TCP_peak_index-1]

    def __TCP_socket_init(self, __TCP_host: str, __TCP_port: int):
        fast_sock.__TCP_sock = socket(AF_INET, SOCK_STREAM)
        fast_sock.__TCP_sock.connect((__TCP_host, __TCP_port))
        fast_sock.__TCP_host = __TCP_host
        fast_sock.__TCP_port = __TCP_port
        fast_sock.__TCP_rebind = True

    def __TCP_recv_thread(self):
        fast_sock.__TCP_RECV_thread = Thread(
            target=fast_sock.TCP_recv, args=(self,))
        fast_sock.__TCP_RECV_thread.setDaemon = True
        fast_sock.__TCP_RECV_thread.start()

    def UPD_send():
        pass


fs = fast_sock("127.0.0.1", 2024)
fs.TCP_send("test data 01".encode())
fs.TCP_send("test data 02".encode(), "127.0.0.1", 2025)
print(fs.TCP_peak())
print(fs.TCP_peak())
