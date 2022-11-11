user_name = 'admin'
password = 'admin'

while True:
    in_put = input('''1:login
0:exit 
请输入选项：
''')
    if in_put == '1':
        user_name1 = input("请输入用户名：")
        password1 = input("请输入密码")
        if user_name1 == user_name and password1 == password:
            print("login success\r\n")
        else:
            print("login fail")
    elif in_put == '0':
        break

#hhh