def option1(): #xem lich
    ngay=0
    thangdu=[4,6,9,11]
    while True:
        nam=int(input("Nhập năm: "))
        if 0<nam<3000:
            break
        else:
            print("\nNhập lại! ")
    while True:
        thang=int(input("Nhập tháng: "))
        if 0<thang<13:
            break
        else:
            print("Không tồn tại tháng",thang," mời bạn nhập lại!")
    if thang==2:
        if (nam%4==0 and nam%100!=0) or nam%400==0:
            ngay=29
        else:
            ngay=28
    else:
        for i in range(len(thangdu)):
            if thang == thangdu[i]:
                ngay = 30
                break
            else:
                ngay = 31
    print("Tháng ",thang,"năm",nam,"có",ngay,"ngày.")
    cont()

def option2(): #Tính lươg
    gio = int(input("Số giờ làm việc của nhân viên đó: "))
    luong=int(input("Tiền lương trong một giờ (ngàn đồng): "))
    if gio<=40:
        print("Tồng lương của nhân viên đó là: ", f'{gio*luong:,d}',"VND")
    else:
        print("Tồng lương của nhân viên đó là: ", f'{int(40*luong+((gio-40)*3/2*luong)):,d}',"VND")
    cont()

def option3(): #Xem lương thứ tự tăng dần
    Ten_nv=[]
    luong=[]

    maxten = " "
    maxmoney = " "
    while True:
        n = int(input("Số lượng nhân viên bạn muốn nhập: "))
        if n<2:
            print("Nhập lại! Số nhân viên phải từ 2 nhân viên trở lên")
        else:
            break
    for i in range(1,n+1):
        Ten_nv.append(input("Nhập tên nhân viên thứ %d:" %i))
        luong.append(int(input("Nhập lương (đơn vị ngàn đồng) của nhân viên %s: "%Ten_nv[i-1])))
    for a in range (n):
        for b in range(a):
            if luong[a] < luong[b]:
                f = luong[a]
                ff=Ten_nv[a]
                luong[a] = luong[b]
                Ten_nv[a] = Ten_nv[b]
                luong[b] = f
                Ten_nv[b]=ff

    
    for h in range(n):
        if len(Ten_nv[h]) > len(maxten): #Tìm tên nhân viên có độ dài lớn nhất
            maxten=Ten_nv[h]
        if len(str(luong[h])) > len(str(maxmoney)):#Tìm số tiền lương nhập vào có độ dài lớn nhất
            maxmoney=luong[h]


    print("Danh sách lương nhân viên được sắp xếp theo thứ tự tăng dần:\n")
    print("_" * (17 + len(str(maxmoney)) + len(str(maxten))+len(str(maxmoney))//3))
    print("|STT |"," TÊN "," "*(len(str(maxten))-5),"| LƯƠNG"," "*(len(str(maxmoney))-2+len(str(maxmoney))//3),"|")
    print("_"*(17+len(str(maxmoney))+len(str(maxten))+len(str(maxmoney))//3))

    for j in range(n):
        print("|", j+1,'.|', Ten_nv[j], " " * (len(str(maxten)) - len(Ten_nv[j])), "|", f'{luong[j]:,d}VND'. format (luong[j]) .replace (',', '.'),
              " " * (len(str(maxmoney))+(len(str(maxmoney))//3) - len(str(luong[j]))-((len(str(luong[j]))-1)//3)), "|")
        print("-" * (17 + len(str(maxmoney)) + len(str(maxten))+len(str(maxmoney))//3))

    cont()

def option4():#In tên hoa
    nn=input("Nếu tên nhân viên là tiến Anh, nhập E. Nếu không thì nhấn Enter ")
    n=input("Nhập tên nhân viên: ")
    name_capital=[]
    name=n.split()
    for i in range (len(name)):
        name_capital.append(name[i].capitalize())
    if nn=="E" or nn=="e":
        print("Họ và tên đệm của nhân viên: ", end=" ")
        for y in range(len(name_capital)-1,0,-1):
            print(name_capital[y], end=" ")
        print("\nTên của nhân viên là: ", name_capital[0])
        print("Họ tên đầy đủ của nhân viên: ", end="")
        for b in name_capital:
            print(b, end=" ")

    else:
        print("Họ và tên lót của nhân viên: ",end=" ")
        for j in range(len(name_capital)-1):
            print(name_capital[j],end=" ")
        print("\nTên của nhân viên là: ",name_capital[-1])
        print("Họ tên đầy đủ của nhân viên: ",end="")
        for a in name_capital:
            print(a,end=" ")

    cont()


def option5(): #Tính điểm trung bình các môn học
    dtb=0
    mon=[]
    diem=[]
    heso=[]
    sbmax=" "
    diemmax=" "
    n=int(input("Nhập số môn học: "))
    for i in range (1,n+1):
        mon.append(input(("Nhập tên môn học thứ %d: "%i)))
        while True:
            d=float(input("Nhập điểm môn %s:"%mon[i-1]))
            if 0 <= d <=10:
                diem.append(d)
                break
            else:
                print("Nhập lại! Điểm môn học chỉ từ 0 đến 10.")
        while True:
            hs=float(input("Nhập hệ số môn %s:"%mon[i-1]))
            if 1<= hs <= 3 and hs % 0.5==0:
                heso.append(hs)
                break
            else:
                print("Nhập lại! Hệ số là các số 1; 1.5; 2; 2.5; 3.")
    print("\nĐây là danh sách sau khi bạn nhập: ")


    for sb in mon:
        if len(sb) > len(sbmax): #Tìm tên môn học có độ dài lớn nhất
            sbmax=sb
    for l in diem:
        if len(str(l)) > len(str(diemmax)): #Tìm điểm có độ dài lớn nhất
            diemmax=l
    print("_"* (30 + len(str(sbmax))))
    print("|STT |","MÔN HỌC"," "*(len(str(sbmax))-5),"|  ĐIỂM"," "*(len(str(diemmax))-3),  "|","HỆ SỐ |")

    print("-" * (30 + len(str(sbmax))))
    for a in range(n):
        print("|", a + 1, '.| ', mon[a], " " * (len(str(sbmax)) - len(mon[a])), " |", diem[a],
              " " * (len(str(diemmax)) - len(str(diem[a]))), "  |", heso[a], "  |")
        print("-" * (30 + len(str(sbmax))))
    for j in range(n):
        dtb += diem[j] * heso[j]

    print("\nTổng số môn học: ",n,"(Gồm các môn",", ".join(mon),")")
    print("Tổng số hệ số: ", sum(heso))
    print("Điểm trung bình của %d môn học: %.1f "%(n,float(dtb/sum(heso))))
    cont()

def cont(): #Tiếp tục chương trình
    n=input("\nNếu muốn tiếp tục hãy nhập 'Yes',nhấn Enter để thoát:\n")
    if n=="Yes" or n=="yes":
        chon()
    else:
        print("Bạn đã xác nhận thoát khỏi chương trình.\nHẹn gặp lại!")
        exit()

def chon(): #Bảng chọn
    while True:
        n=int(input("Vui lòng chọn: "))
        if n==1:
            option1()
            break
        elif n==2:
            option2()
            break
        elif n==3:
            option3()
            break
        elif n==4:
            option4()
            break
        elif n==5:
            option5()
            break
        elif n==6:
            print("Bạn đã xác nhận thoát khỏi chương trình.\nHẹn gặp lại!")
            exit()
        else:
            print("Không tồn tại lựa chọn ",n,"\b! Mời bạn nhập lại")


def background():  # In mẫu
    print("""\
                        +------------------------------------------------------+
                        | **************************************************** |
                        | ************Chương Trình Học Thông Minh************* |
                        | **************************************************** |
                        +------------------------------------------------------+

    +---------------------------------------------------------------------------------------------+
    |===========================================MENU==============================================|
    +---------------------------------------------------------------------------------------------+

    +---------------------------------------------------------------------------------------------+
    |   Xin vui lòng chọn:                                                                        |
    |   1. Xem lịch                                                                               |
    |   2. Tính lương                                                                             |
    |   3. Xem lương                                                                              |
    |   4. Xem thông tin nhân viên                                                                |
    |   5. Tính điểm của học sinh                                                                 |
    |   6. Thoát chương trình                                                                     |
    +---------------------------------------------------------------------------------------------+
    """)

background()
chon()




















