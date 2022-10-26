
# 定义变量
add = 0
s = 1
str_add = ''
inv_str_add = ''
# 带提示输入赋值
z = input('请输入需要加密的字符串：')
# 把字符串转换为ASCII码
for i in z:
    print(i)
    add += ord(i)
    str_add += str(ord(i))
 
# 调试代码
print(add)      # 打印转换ASCII码之和
print(str_add)  # 打印转换ASCII码拼接
 
# 计算ASCII码拼接后的个数
for i in str_add:
    #print(i)
    s += 1
# 拼接后的ASCII码做倒序处理
for i in range(1, s):
   # print(i)
    inv_str_add += str_add[-i]
#print(inv_str_add)  # 打印拼接后的ASCII码倒序he
# 打印加密后的字符串
print ('加密后：',add+int(inv_str_add))
#print("加密后:",buf,add,int(inv_str_add))