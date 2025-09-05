# คำสั่ง break, continue
# break ใน loop ทำงานเมื่อใดจบ loop ทันที
# continue ใน loop ทำงานเมื่อใดจบ loop แค่รอบนั้นทันทีให้ไปรอบต่อไปโลดด

for aa in range(5):
    if aa == 2:
        break
    print(aa, 'Hi...')

for aa in range(5):
    if aa == 2:
        continue
    print(aa, 'Hi...')