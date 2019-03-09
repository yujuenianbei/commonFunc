import socket  # 导入socket模块

sk = socket.socket()  # 创建socket对象
sk.bind(("127.0.0.1", 8888))  # 绑定端口,“127.0.0.1”代表本机地址，8888为设置链接的端口地址
sk.listen(5)  # 设置监听，最多可有5个客户端进行排队
conn, addr = sk.accept()  # 阻塞状态，被动等待客户端的连接
print(conn)  # conn可以理解客户端的socket对象
# <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9005), raddr=('127.0.0.1', 36694)>
print(addr)  # addr为客户端的端口地址
# ('127.0.0.1', 40966)
accept_data = conn.recv(1024)  # conn.recv()接收客户端的内容，接收到的是bytes类型数据，
# str(data,encoding="utf8")用“utf8”进行解码
accept_data2 = str(accept_data, encoding="utf8")
print("".join(("接收内容：", accept_data2, "    客户端口：", str(addr[1]))))
send_data = input("输入发送内容：")
# 发送内容必须为bytes类型数据，bytes(data, encoding="utf8")用“utf8”格式进行编码
conn.sendall(bytes(send_data, encoding="utf8"))
conn.close()
