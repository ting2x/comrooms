roomlist = [("[1]","Computer room 1"),
            ("[2]","Computer room 2"),
            ("[3]","Computer room 3"),
            ("[4]","Computer room 4")]

weekdays = [("[1]","จันทร์"),
            ("[2]","อังคาร"),
            ("[3]","พุธ"),
            ("[4]","พฤหัสบดี"),
            ("[5]","ศุกร์")]

times = [("[1]","08:30am - 09:30am"),
         ("[2]","09:30am - 10:30am"),
         ("[3]","10:30am - 11:30am"),
         ("[4]","11:30am - 12:30pm"),
         ("[5]","13:30am - 14:30am"),
         ("[6]","14:30am - 15:30pm")]

 
#def Login():
    #name = input('\n\n\n\n\n\n\nกรุณากรอกชื่อเพื่อทำการจองค่ะ --> ')
    #selectRoom()
def Logout():
    input("\n------------------------------\nท่านได้ออกจากระบบเรียบร้อยแล้ว\n------------------------------")
    exit


def ReadBookings(): #Try กรณีเกิด Error หาไฟล์ไม่เจอ | Except จะสร้างไฟล์ใหม่ | Finally ทำงานทุกกรณี
    try:
        open("rooming.csv","r")
    except FileNotFoundError: 
        New = open("rooming.csv","w",encoding='UTF-8-SIG') #ต้องใส่ -SIG ไว้ด้วย
        New.write("ชื่อ,ห้อง,วัน,เวลา\n")
    finally:
        Data = open("rooming.csv","r",encoding='UTF8') 
        return  Data.readlines()[1:]

def WriteBookings(booking): #เขียนลงไฟล์csv
    Data = open("rooming.csv","a",encoding='UTF8')
    Data.write(booking+"\n")
    Data.close()  

def checkroom(name,room,day,time): #เช็คว่าห้องจองอยู่รึเปล่า?
    for i in ReadBookings():
        checkcsv = i.split(",")
        if name in checkcsv[0] and room in checkcsv[1] and day in checkcsv[2] and time in checkcsv[3] : 
            return False
    else:
        return True

def selectTime(Day,Rum): 
    print()
    for q,time in times: print(q,time)
    picktime = input("\nโปรดเลือกเวลาที่ต้องการเข้าใช้: ")
    if picktime in '123456':
        picktime = times[int(picktime)-1][1]
        if checkroom(name,Rum,Day,picktime):
            WriteBookings(f'{name}, {Rum}, {Day}, {picktime}')
            selectRoom()
        else:
            print("\n----------------------\nห้องถูกจองแล้วกรุณาเลือกใหม่!\n----------------------")
            input('')
            selectRoom()
    else:
        print("\n-----------\nข้อมูลไม่ถูกต้อง\n-----------")
        selectTime(Day,Rum)

def selectDay(RooM):
    print()
    for q, day in weekdays: print(q,day)
    pickday = input("\nโปรดเลือกวันที่ต้องการเข้าใช้: ")
    if pickday in '12345':
        dayy = weekdays[int(pickday)-1][1]
        selectTime(dayy,RooM)
    else:
        print("\n-----------\nข้อมูลไม่ถูกต้อง\n-----------")
        selectDay(RooM)

def selectRoom():
    print("\n--------------------------------------------\nระบบจองห้องคอมพิวเตอร์ กด [x] เพื่อออก\n--------------------------------------------")
    for q,rm in roomlist : print(q,rm)
    pickroom = input("\nโปรดเลือกห้องที่ต้องการเข้าใช้: ")  
    if pickroom in '1234':
        room = roomlist[int(pickroom)-1][1]
        selectDay(room)
    elif pickroom in 'Xx':
        Logout()
    elif pickroom in 'Ss':
        showroom()
    else: 
        print("\n-----------\nข้อมูลไม่ถูกต้อง\n-----------")
        selectRoom()

def showroom(): 
    print('{0:<40}{1:<10}'.format('\n','My friend report'))
    print('{0:_<110}'.format(''))
    print('{0:<4}{1:<16}{2:<20}{3:<18}{4:<8}'.format('No.','Name','Room','Day','Time'))
    print('{0:_<110}'.format(''))
    import csv 
    with open("rooming.csv","r",encoding='UTF8') as csvfile:
        reader = csv.reader(csvfile)
        line_count = 0
        count = 0
        for row in reader:
            if line_count == 0:
                line_count += 1
            else:
                count += 1
                print(count,end=" ) ")
                print('{0:<15}{1:<20}{2:<20}{3:<30}'.format(row[0],row[1],row[2],row[3]))
                line_count += 1

        input("\nEnter to conti...")
        selectRoom()
def showroomdel(): 
    print('{0:<40}{1:<10}'.format('\n','Computer Room'))
    print('{0:_<110}'.format(''))
    print('{0:<4}{1:<16}{2:<20}{3:<18}{4:<8}'.format('No.','Name','Room','Day','Time'))
    print('{0:_<110}'.format(''))
    import csv 
    with open("rooming.csv","r",encoding='UTF8') as csvfile:
        reader = csv.reader(csvfile)
        line_count = 0
        count = 0
        for row in reader:
            if line_count == 0:
                line_count += 1
            else:
                count += 1
                print(count,end=" ) ")
                print('{0:<15}{1:<20}{2:<20}{3:<30}'.format(row[0],row[1],row[2],row[3]))
                line_count += 1

def Admin():
    import csv
    member= input("\n----------------------\nเลือกรายการที่ต้องการ\n1[Delete name]\n2[Delete All]\n----------------------\n->")
    if member == '1':
        lines = list()
        showroomdel()
        members= input("\n----------------------\nพิมพ์ชื่อที่ต้องการลบออก\n----------------------\n->")
        with open('rooming.csv', 'r',encoding='UTF8') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == members:
                        lines.remove(row)
        with open('rooming.csv', 'w',encoding='UTF8') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
            print('\n-----------\nลบข้อมูลเรียบร้อย\n-----------')
            input('Enter to close program')
            exit
    elif members == '2':
        f = open("rooming.csv", "w")
        f.truncate()
        f.close()
        print('\n-----------\nลบข้อมูลเรียบร้อย\n-----------')
        input('Enter to close program')
        exit

name = input('\n\n\n\n\n\n\nกรุณากรอกชื่อเพื่อทำการจองค่ะ --> ')
namelow = name.lower() 
if namelow == 'admin':
    Admin()
    
selectRoom() 

