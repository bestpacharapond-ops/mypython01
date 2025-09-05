# 2. have parameter no return

'''
def func_name(parameter1, parameter2,...):
    คำสั่ง
    คำสั่ง
'''
def showHi(your_name):
    print('-------------')
    print(f'สวัสดี {your_name} ! ')
    print('-------------')

def showNumber(n1,n2):
    print('-------------')
    print(f'ผลบวกของ {n1} และ {n2} เท่ากับ {n1+n2} ! ')
    print('-------------')

showHi('สมชาย') #ข้อมูลที่ส้งให้ parameter เรียก เป็น argument
showHi('สมศรี')
showNumber(10,20)
showHi('Sombat')