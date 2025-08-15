# คำสั่งรับค่าข้อความ string ทางแป้นพิพมพ์ ใช้ฟังก์ชัน input()
# ****** ตัวแปร variable คือ ชื่อที่ Dev ตั้งขึ้นมาเอง (ต้องเป็นไปตามกฎการตั้งชื่อ) เอาไว้เก็บข้อมูลขึ้นในโปรแกรม

fullname = input('ป้อนชื่อ: ')
year_born = input('ป้อนปีเกิด พ.ศ.: ')
print("------")
print(f'สวัสดีคุณ{fullname}')
print(f'คุณเกิดในปี{year_born}ตอนนี้คุณอายุ{2568 - int(year_born)}')
#  ใช้ ,
print("f'คุณ {fullname}",year_born,'+set(year_born)+ตอนนี้คุณอายุ'+str(2568 -int(year_born)))
# ใช้ +
print('Hello'+str)+'คุณ {fullname}'+str(year_born)+ตอนนี้คุณอายุ'+str(2568 -int(year_born)))
# ใช้ format
print(' ' ,format('A','B','C','D','E'))
# ใช้ F+sting
print(f'Hello (555) Wow {999} {True} Hi {10+20-5} {152.875}')