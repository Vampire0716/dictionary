"""
dict客户端
主要功能：
    根据用户输入-发送请求-得到结果
结构：
    1.一级界面：注册 登录 退出
    2.二级界面：查单词 查历史记录 注销
"""
from socket import *
from getpass import getpass   #运行只在终端，pycharm中不支持
import sys

#服务器地址
ADDR = ('172.40.74.148',1888)
#功能函数都需要套接字，所以定义为全局变量
s = socket()
s.connect(ADDR)

#一级界面-注册函数
def do_register():
    while True:
        name = input("User:")
        passwd = getpass()
        passwd_ = getpass('Again:')

        if (' ' in name) or (' ' in passwd):
            print("用户名和密码不能有空格")
        if passwd != passwd_:
            print("两次密码不一致")
            continue
        msg = "R %s %s"%(name,passwd)
        s.send(msg.encode())#发送请求
        data = s.recv(1024).decode()#接收反馈信息
        if  data == 'OK':
            print("恭喜注册成功：")
            login(name) #进入二级界面
        else:
            print("抱歉傻屌，注册失败！")
        return

#一级界面-登录函数
def do_login():
    while True:
        name = input("User:")
        passwd = getpass()
        msg = "L %s %s"%(name,passwd)
        s.send(msg.encode())
        data = s.recv(1024).decode()
        if data =='OK':
            print("登陆成功！")
            login(name)
        else:
            print("登录失败！")
        return

#二级界面-查找单词
def do_query(name):
    while True:
        word = input("请输入单词：")
        if word == '##':
            break
        msg = "Q %s %s"%(name,word)
        s.send(msg.encode())
        data = s.recv(2048).decode()
        print(data)

#二级界面-查询历史记录
def do_hist(name):
    msg = "H %s"%name
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'OK':
        while True:
            data = s.recv(1024).decode()
            if data == '##':
                break
            print(data)
    else:
        print("没有历史记录")

#建立并进入二级界面
def login(name):
    while True:
        print("""
        ******************这里就是德莱联盟*******************
        *     1.查单词          2.历史记录         3.注销    *
        *****************************************************
        """)
        cmd = input("请出入选项：")
        if cmd == '1':
            do_query(name)
        elif cmd == '2':
            do_hist(name)
        elif cmd == '3':
            return
        else:
            print("请输入正确选项")


#搭建客户端网络,建立一级界面
def main():
    while True:
        print("""
        ******************欢迎来到德莱联盟*******************
        *     1.注册            2.登录            3.退出    *
        *****************************************************
        """)
        cmd = input("请出入选项：")
        if cmd == '1':
            do_register()
        elif cmd == '2':
            do_login()
        elif cmd == '3':
            s.send(b'E')
            sys.exit("""
            <<<<<<<<<<<<<<<<<<谢谢使用>>>>>>>>>>>>>>>>>>>
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ~~~~~~~~~~~~~~~~~~~~~BYE~~~~~~~~~~~~~~~~~~~~
            ~~~~~~~~~~~~~~~~~~~~~BYE~~~~~~~~~~~~~~~~~~~~
            ~~~~~~~~~~~~~~~~~~~~~~!~~~~~~~~~~~~~~~~~~~~~
            """)
        else:
            print("请输入正确选项")

if __name__ == "__main__":
    main()