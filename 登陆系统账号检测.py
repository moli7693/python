 # 定义变量
s = 3       # 设置登录次数
 
print('您还没有注册，无法登录！')           # 预先打印提示语
 
# 设置账号密码
origin_ID = input('请设置账号：')
origin_password = input('请设置密码：')
 
print('已注册成功！')                     # 预先打印提示语
print('欢迎来到系统登录界面')              # 预先打印提示语
 
 
while True:
 
    # 带提示语输入赋值
    ID = input('请输入账号：')
    password = input('请输入密码：')
 
    # 登陆成功
    if origin_ID == ID and origin_password == password:
        print('登录成功！')
        break
 
    # 密码错误
    elif origin_ID == ID:
        print('密码错误！', end='')
        if s != 1:
            print('还有{}次机会'.format(s - 1))
 
    # 账号错误
    elif origin_password == password:
        print('账号错误！', end='')
        if s != 1:
            print('还有{}次机会'.format(s - 1))
 
    # 账号密码错误
    else:
        print('账号和密码错误！', end='')
        if s != 1:
            print('还有{}次机会'.format(s - 1))
 
    # 结束条件
    if s <= 1:
        print('\n输入次数过多,账号已被冻结！')
        break
 
    s -= 1      # 记录输入次数