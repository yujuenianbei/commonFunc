import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 8888))  # 主动初始化与服务器端的连接
send_data = input("输入发送内容：")
print(send_data)
# 发送数据
sk.sendall(bytes(send_data, encoding="utf8"))
# 接收服务端数据
accept_data = sk.recv(1024)
print(str(accept_data, encoding="utf8"))
sk.close()