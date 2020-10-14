# -*- coding: utf-8 -*-
'''
如何安装 Python 的第三方模块

Python 的一大优势就是有丰富且易用的第三方模块，省去了大量重复造轮子的时间，节约了众多开发者的生命。对于已经熟悉 Python 开发的人来说，安装第三方模块是家常便饭的事情。但如果是刚入门的新手，很可能会被折腾一番。所以我来简单地科普一下，如何安装 Python 的第三方模块。

（本文基于 Python 2.7 版本）

安装通常有两种方式：通过包管理器、直接下载源码安装。

1. 包管理器
很多系统和语言都提供了包管理器。你可以把“包管理器”想象成一个类似应用商店的工具。Python 的包管理器里就是各种第三方模块。有了它，不用998，也不用98，只需要一条命令，就可以自动帮你下载并安装。

Python 常用的包管理器是 pip 和 easy_install。他们会从一个叫做 PyPI 的源里搜索你要的模块，找到后自动下载安装。PyPI 是 Python 官方的第三方模块仓库，供所有开发者下载或上传代码。

如果你用的是 Mac 或者 Linux，那么同 Python 一样，你的系统里应该自带了 pip。而如果你是 Windows，那么在安装 Python 的时候，勾选 pip 和 Add python.exe to Path，就会帮你同时安装好 pip 并设置好环境变量中的路径。如果无法使用 pip，确认 Python 安装目录下的 Scripts 子目录中有 pip，并且这个子目录的路径被加在了环境变量 Path 中。如果没有 pip，则要通过下载 setuptools 安装，或建议直接重新安装一遍 Python。

以 IPython 为例，通过 pip 命令进行安装，只需要在命令行输入：

pip install ipython
如果一切正常，网络不抽风，只要稍微等待，就可以看到下载进度，自动安装完就可使用。如果 Mac/Linux 下提示 Permission denied 之类的权限问题，在命令前加上 sudo。

IPython 是一个增强版的 Python shell，在命令行输入 ipython 就可以打开使用。比默认运行 python 进入的那个更好使，在里面调试代码会很方便。不过 windows 的话，还要再用 pip 装一个 pyreadline 的模块，才能使用 IPython 的 tab 键自动补全功能。（用 Windows 开发就是事多）

如果你不是很明确要下载的模块名，也可以进行搜索，比如：

pip search ipython
再来看 easy_install。安装 easy_install 的一种简单方法是去网上下载一个的脚本文件：


ez_setup.py ( peak.telecommunity.com/dist/ez_setup.py )

下载之后运行它：

python ez_setup.py
然后 easy_install 就被安装好了。同样，需确认 Scripts 在环境变量 PATH 里。

使用方法和 pip 一样简单：

easy_install ipython
一般来说，pip 和 easy_install 就可以搞定绝大多数的模块安装了。万一不行，还可以尝试下面的另一种方式。

2. 源码安装
几乎所有第三方模块都可以在 PyPI 或 github 上找到源码，都会提供 zip、tar 等格式的压缩包。把代码压缩包下载到本地并解压，应该会看到一个 setup.py 的文件。在命令行进入其所在目录，执行：

python setup.py install
就会安装这个第三方模块。最终效果和用包管理器是一样的。

无论哪种方法，都会将第三方模块代码安装至 Python 的路径下，根据系统不同，位置有所区别，大致都是叫做 site-packages 或 dist-packages。所以对于一些没有其他依赖，不需要编译其他语言的纯 Python 代码包，也可以直接手动将源码复制到 site-packages 或 dist-packages 目录下。只要路径正确，就可以在你的代码里引入这些模块。


友情提醒一些坑：

安装第三方模块前，请确认它所支持的版本，是不是包含你所使用的 Python 版本。有些模块对应 Python 2 和 3 需要下载不同的版本。

少数复杂的包可能无法直接一条命令安装成功，特殊情况特殊对待，搜索引擎会给你指引。

如果你的电脑上装有多个版本的 Python，使用 pip 很可能会造成混乱。对于这个问题，virtualenv 是一个很好的解决方案，下次会专门来讲一讲。


有一个叫做 Awesome Python 的项目，列出了各类优秀的、实用的、有意思的 Python 库：

awesome-python.com


Crossin的编程教室

微信ID：crossincode

论坛：Crossin的编程教室

QQ群：498545096

'''

# Sockets Tutorial with Python 3 part 1 - sending and receiving data
'''
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address=s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("welcome to the server!", "utf-8"))
    clientsocket.close()
'''

'''
# Sockets Tutorial with Python 3 part 2 - buffering and streaming data
import socket
import time

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg

    print(msg)

    clientsocket.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(3)
        msg = f"The time is: {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))
'''

'''

# Sockets Tutorial with Python 3 part 3 - sending and receiving Python Objects w/ Pickle
import socket
import time
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    d={1: "Hey", 2: "There"}
    msg = pickle.dumps(d)
    print(msg)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8")+ msg


    clientsocket.send(bytes(msg))
'''

# Socket Chatroom server - Creating chat application with sockets in Python
import socket
import select

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

# Create a socket
# socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# SO_ - socket option
# SOL_ - socket option level
# Sets REUSEADDR (as a socket option) to 1 on socket
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind, so server informs operating system that it's going to use given IP and port
# For a server using 0.0.0.0 means to listen on all available interfaces, useful to connect locally to 127.0.0.1 and remotely to LAN interface IP
server_socket.bind((IP, PORT))

# This makes server listen to new connections
server_socket.listen()

# List of sockets for select.select()
sockets_list = [server_socket]

# List of connected clients - socket as a key, user header and name as data
clients = {}

print(f'Listening for connections on {IP}:{PORT}...')

# Handles message receiving
def receive_message(client_socket):

    try:

        # Receive our "header" containing message length, it's size is defined and constant
        message_header = client_socket.recv(HEADER_LENGTH)

        # If we received no data, client gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
        if not len(message_header):
            return False

        # Convert header to int value
        message_length = int(message_header.decode('utf-8').strip())

        # Return an object of message header and message data
        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:

        # If we are here, client closed connection violently, for example by pressing ctrl+c on his script
        # or just lost his connection
        # socket.close() also invokes socket.shutdown(socket.SHUT_RDWR) what sends information about closing the socket (shutdown read/write)
        # and that's also a cause when we receive an empty message
        return False

while True:

    # Calls Unix select() system call or Windows select() WinSock call with three parameters:
    #   - rlist - sockets to be monitored for incoming data
    #   - wlist - sockets for data to be send to (checks if for example buffers are not full and socket is ready to send some data)
    #   - xlist - sockets to be monitored for exceptions (we want to monitor all sockets for errors, so we can use rlist)
    # Returns lists:
    #   - reading - sockets we received some data on (that way we don't have to check sockets manually)
    #   - writing - sockets ready for data to be send thru them
    #   - errors  - sockets with some exceptions
    # This is a blocking call, code execution will "wait" here and "get" notified in case any action should be taken
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)


    # Iterate over notified sockets
    for notified_socket in read_sockets:

        # If notified socket is a server socket - new connection, accept it
        if notified_socket == server_socket:

            # Accept new connection
            # That gives us new socket - client socket, connected to this given client only, it's unique for that client
            # The other returned object is ip/port set
            client_socket, client_address = server_socket.accept()

            # Client should send his name right away, receive it
            user = receive_message(client_socket)

            # If False - client disconnected before he sent his name
            if user is False:
                continue

            # Add accepted socket to select.select() list
            sockets_list.append(client_socket)

            # Also save username and username header
            clients[client_socket] = user

            print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))

        # Else existing socket is sending a message
        else:

            # Receive message
            message = receive_message(notified_socket)

            # If False, client disconnected, cleanup
            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))

                # Remove from list for socket.socket()
                sockets_list.remove(notified_socket)

                # Remove from our list of users
                del clients[notified_socket]

                continue

            # Get user by notified socket, so we will know who sent the message
            user = clients[notified_socket]

            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            # Iterate over connected clients and broadcast message
            for client_socket in clients:

                # But don't sent it to sender
                if client_socket != notified_socket:

                    # Send user and message (both with their headers)
                    # We are reusing here message header sent by sender, and saved username header send by user when he connected
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    # It's not really necessary to have this, but will handle some socket exceptions just in case
    for notified_socket in exception_sockets:

        # Remove from list for socket.socket()
        sockets_list.remove(notified_socket)

        # Remove from our list of users
        del clients[notified_socket]
