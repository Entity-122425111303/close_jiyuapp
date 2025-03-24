#  MIT License
#
#  Copyright (c) 2025 Entity-122425111303
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

import os
print('版权所有©Entity-122425111303')
print('下载地址：https://lxy111303.lanzoub.com/b00je8621c   密码:eszb')
dict = {1:'打开防火墙',2:'关闭防火墙',3:'关闭极域',4:'打开下载页面',5:'退出'}
while True:
    str1 = '%s \t %s'
    str2 = ('序号', '操作')
    print(str1%str2)
    for x,y in dict.items():
        str2 = (x,y)
        print(str1%str2)
    try:
        num = int(input('请输入应用/操作相应的序号：'))
        choice = dict[num]
    except:
        exit('error:incorrect input(choose number)!')
    if choice == '打开防火墙':
        os.system('netsh advfirewall set allprofiles state on')
    elif choice == '关闭防火墙':
        os.system('netsh advfirewall set allprofiles state off')
    elif choice == '关闭极域':
        os.system('taskkill /IM StudentMain.exe /F')
        choice = input('是否关闭防火墙(y/n)?')
        if choice == 'y':
            os.system('netsh advfirewall set allprofiles state off')
    elif choice == '打开下载页面':
        print('密码:eszb')
        os.system('start https://lxy111303.lanzoub.com/b00je8621c')
    elif choice == '退出':
        print('正在退出...')
        break
