#@2019 Dajinzhu
#大金猪计算器
def jia():
	a = int(input('请输入一个数:'))
	b = int(input('请输入一个数:'))
	H = a + b
	print(f'你的得数是 {H} 。')
def jian():
	a = int(input('请输入一个数:'))
	b = int(input('请输入一个数:'))
	H = a - b
	print(f'你的得数是 {H} 。')
def cheng():
	a = int(input('请输入一个数:'))
	b = int(input('请输入一个数:'))
	H = a * b
	print(f'你的得数是 {H} 。')
def chu():
	a = int(input('请输入一个数:'))
	b = int(input('请输入一个数:'))
	if b != 0:
		H = a / b
		print(f'你的得数是 {H} 。')
	else:	
		print('错误:0不能当除数。')
def mu():
	a = int(input('请输入一个数:'))
	b = int(input('请输入一个数:'))
	H = a ** b
	print(f'你的得数是 {H} 。')
		
print('欢迎来到大金猪计算器！！！')
print('--------------------------')
print('1.加法                   -')
print('2.减法                   -')
print('3.乘法                   -')
print('4.除法                   -')
print('5.乘方                   -')
print('--------------------------')
xz = input('请选择一种运算:')
print('--------------------------')
if xz == '1':
	jia()
if xz == '2':
	jian()
if xz == '3':
	cheng()
if xz == '4':
	chu()
if xz == '5':
	mu()
print('再见！！！')
