
from tkinter import *
import numpy as np
from PIL import ImageTk, Image
from tkinter import filedialog
from keras.models import load_model
import webbrowser



# Tạo cửa sổ giao diện chính
root = Tk()
root.title('GRAPHICSAL USER INTERFACE')
root.geometry("1366x720")


# Tải mô hình đã được đào tạo
model_h5 = load_model('CNN_BienBaoVN_new.h5')

# Tạo class chứa danh sách tên các loại biển báo đã train
classes = {
    1: 'Duong Cam',
    2: 'Cam Di Nguoc Chieu',
    3: 'Cam O To',
    4: 'Cam O To Re Phai',
    5: 'Cam O To Re Trai',
    6: 'Cam Xe May',
    7: 'Cam O To Va Xe May',
    8: 'Cam Xe Tai',
    9: 'Cam Xe Tai Tren 2.5 tan',
    10: 'Cam O To Khach Va O To',
    11: 'Cam O To Ro-Mooc',
    12: 'Cam May Keo',
    13: 'Cam Xe Dap',
    14: 'Cam Xe Dap Tho',
    15: 'Cam Xe 3 va 4 Banh Tho So',
    16: 'Cam Nguoi Di Bo',
    17: 'Cam Xe Keo Day',
    18: 'Cam Xe Suc Vat Keo',
    19: 'Han Che Trong Luong Xe',
    20: 'Han Che Trong Luong Truc Xe',
    21: 'Han Che Chieu Cao Xe',
    22: 'Han Che Chieu Rong Xe',
    23: 'Han Che Chieu Dai O To',
    24: 'Han Che Chieu Dai Ro-Mooc',
    25: 'Khoang Cach Toi Thieu Giua Hai Xe',
    26: 'Dung Lai',
    27: 'Cam Re Trai',
    28: 'Cam Re phai',
    29: 'Cam Quay Dau',
    30: 'Cam O To Quay Dau',
    31: 'Cam Vuot',
    32: 'Cam O To Vuot',
    33: 'Toc Do Toi Da',
    34: 'Cam Bop Coi',
    35: 'Tram Thue Quan',
    36: 'Cam Dung Va Do Xe',
    37: 'Cam Do Xe',
    38: 'Cam Do Xe Ngay Le',
    39: 'Cam Do Xe Ngay Chan',
    40: 'Nhuong Duong Cho Xe Co Gioi Di Nguoc Chieu Trong Duong Hep',
    41: 'Het Cam Vuot',
    42: 'Het Han Che Toi Da',
    43: 'Het Tat Ca Cac Lenh Cam',
    44: 'Cam Di Thang',
    45: 'Cam Re Trai Va Phai',
    46: 'Cam Di Thang va Re Phai',
    47: 'Cam Di Thang va Re Trai',
    48: 'Cam Xe Cong Nong',
    49: 'Cho Ngoac Vong Ben Trai',
    50: 'Cho Ngoac Vong Ben Phai',
    51: 'Nhieu Cho Ngoac Nguy Hiem Lien Tiep',
    52: 'Duong Hep Hai Ben',
    53: 'Duong Hep Ben Trai',
    54: 'Duong Hep Ben Phai',
    55: 'Duong Hai Chieu',
    56: 'Duong Cat Nhau',
    57: 'Duong Cat Nhau Trai',
    58: 'Duong Cat Nhau Phai',
    59: 'Duong Cat Nhau Chu T',
    60: 'Duong Cat Nhau Chu Y',
    61: 'Duong Giao Nhau Chay Theo Vong Xuyen',
    62: 'Giao Nhau Voi Duong Khong Uu Tien Hai Ben',
    63: 'Giao Nhau Voi Duong Khong Uu Tien Ben Phai',
    64: 'Giao Nhau Voi Duong Khong Uu Tien Ben Trai',
    65: 'Giao Nhau Voi Duong Uu Tien',
    66: 'Giao Nhau Voi Tin Hieu Den',
    67: 'Giao Nhau Voi Duong Sat Co Rao Chan',
    68: 'Giao Nhau Voi Duong Sat Khong Co Rao Chan',
    69: 'Cau Hep',
    70: 'Cau Tam',
    71: 'Cau Xoay - Cau Dat',
    72: 'Ke Vuc Sau Phia Truoc',
    73: 'Duong Ngam',
    74: 'Ben Pha',
    75: 'Cua Chui',
    76: 'Doc Xuong Nguy Hiem',
    77: 'Doc Len Nguy Hiem',
    78: 'Duong Khong Bang Phang',
    79: 'Duong Tron Truot',
    80: 'Vach Nui Nguy Hiem',
    81: 'Nguoi Di bo Cat Ngang',
    82: 'Tre Em',
    83: 'Nguoi Di Xe Dap Cat Ngang',
    84: 'Cong Truong',
    85: 'Da Lo',
    86: 'Dai May bay',
    87: 'Gia Suc',
    88: 'Thu Rung Di Ngang',
    89: 'Gio Ngang',
    90: 'Nguy Hiem Khac',
    91: 'Giao Nhau Voi Duong Hai Chieu',
    92: 'Duong Doi',
    93: 'Het Duong Doi',
    94: 'Cau Vong',
    95: 'Duong Cap Dien Phia Tren',
    96: 'Duong Cao Toc Phia Truoc',
    97: 'Duong Ham',
    98: 'Cho Duong Sat Cat Duong Bo',
    99: 'Duong Sat Cat Duong Bo Khong Vuong Goc',
    100: 'Doan Duong Hay Xay Ra Tai Nan',
    101: 'Di Cham',
    102: 'Vong Tranh Hai Ben',
    103: 'Vong Tranh Ben Trai',
    104: 'Vong Tranh Ben Phai',
    105: 'Cac Xe Chi Duoc Di Thang',
    106: 'Cac Xe Chi Duoc Re Phai',
    107: 'Cac Xe Chi Duoc Re Trai',
    108: 'Cac Xe Chi Duoc Re Phai',
    109: 'Cac Xe Chi Duoc Re Trai',
    110: 'Cac Xe Chi Duoc Di Thang va Re Phai',
    111: 'Cac Xe Chi Duoc Di Thang va Re Trai',
    112: 'Cac Xe Chi Duoc Re Trai va Re Phai',
    113: 'Huong Di Vong Chuong Ngai Vat Sang Phai',
    114: 'Huong Di Vong Chuong Ngai Vat Sang Trai',
    115: 'Noi Giao Nhau Chay Theo Vong Xuyen',
    116: 'Duong Danh Cho Xe Tho So',
    117: 'Duong Danh Cho Nguoi Di Bo',
    118: 'Toc Do Toi Thieu Cho Phep',
    119: 'Het Han Che Toc Do Toi Thieu',
    120: 'Tuyen Duong Cau Vuot Bat Qua',
    121: 'An Coi'
}


#Hàm mở trang web
def open_url():
    url = "http://127.0.0.1:7860"
    webbrowser.open_new(url)
#Nút nhấn mở trang web
webapp = Button(root, text="WEB APP", background='brown', foreground='white', font=('arial', 12, 'bold'), command=open_url)
webapp.place(x=200, y=660)


#Hàm nhận diện ảnh từ file h5 đã train và hiện tên biển báo từ danh sách class
def classify(file_path):
    images = Image.open(file_path)              #Mở ảnh từ đường dẫn của biến file_path
    images = images.resize((64, 64))            #Set kích thước ảnh
    images = np.expand_dims(images, axis=0)     #Thiết lập hình ảnh thành mảng đa chiều để thực hiện tính toán

    #tính toán giá trị dự đoán của mô hình trên tập hình ảnh images bằng cách sử dụng hàm predict() của model_h5
    # và lấy chỉ số của lớp có xác suất cao nhất bằng hàm argmax()
    pred = np.argmax(model_h5.predict(images), axis=1)[0]
    #lấy tên biển báo tương ứng với chỉ số pred từ danh sách các lớp classes
    sign = classes[pred + 1]
    print(sign)
    label.configure(foreground='green', text=sign)

#Hàm thiết lập nút nhấn dự đoán
def show_classify_button(file_path):
    classify_b = Button(root, text='DETECT', command=lambda: classify(file_path))
    classify_b.configure(background='brown', foreground='white', font=('arial', 12, 'bold'))
    classify_b.place(x=650, y=660)

#Hàm tải hình ảnh biển báo lên
def upload_image():
    try:
        file_path = filedialog.askopenfilename()        #Hiển thị hôp thoại chọn ảnh
        uploaded = Image.open(file_path)                #Tải ảnh lên
        resize_down = uploaded.resize((350, 350))       #Set lại kích thước ảnh
        img = ImageTk.PhotoImage(resize_down)           #Hiển thị hình ảnh lên giao diện
        sign_image.configure(image=img)
        sign_image.image = img
        label.configure(text='')                        #Sau khi chọn hình ảnh mới thì xóa tên biển báo cũ
        show_classify_button(file_path)                 #Cho hiển thị nút nhấn
    except:
        pass

#Hàm thoát giao diện
def CLOSE():
    root.destroy()




#Upload logo Truong
lgtruong = ImageTk.PhotoImage(Image.open("logotruong.jpg"))
lblgtruong = Label(image=lgtruong)
lblgtruong.place(x=20, y=5)

#Upload logo Khoa
lgkhoa = ImageTk.PhotoImage(Image.open("logokhoa.jpg"))
lblgkhoa = Label(image=lgkhoa)
lblgkhoa.place(x=1040, y=60, anchor=CENTER)

#Upload logo Gradio
uplgGr = Image.open("logo_gradio.png")
resize_lgGr = uplgGr.resize((350, 350))
lgGr = ImageTk.PhotoImage(resize_lgGr)
lblgGr = Label(image=lgGr)
lblgGr.place(x=250, y=400, anchor=CENTER)

#Hien thi cac Thông tin nhóm Giao dien
myLabel2 = Label(root, text="Khoa Cơ Khí Chế Tạo Máy", font="Arial 15 bold", fg="darkblue")
myLabel3 = Label(root, text="CNKT Cơ Điện Tử", font="Arial 15 bold", fg="darkblue")
myLabel2.place(x=1000, y=220)
myLabel3.place(x=1000, y=250)
myLabel4 = Label(root, text="NHẬN DIỆN BIỂN BÁO GIAO THÔNG ĐƯỜNG BỘ VIỆT NAM", font="Arial 25 bold", fg="darkred")
myLabel4.place(x=683, y=160, anchor=CENTER)
myLabel5 = Label(root, text="Môn học: Thị Giác Máy", font="Arial 15 bold", fg="darkblue")
myLabel6 = Label(root, text="GVHD: TS. Nguyễn Văn Thái", font="Arial 15 bold", fg="darkblue")
myLabel5.place(x=1000, y=290)
myLabel6.place(x=1000, y=320)
myLabel7 = Label(root, text="Nhóm MV04 - STT: 13", font="Arial 15 bold", fg="darkblue")
myLabel8 = Label(root, text="Lê Trung Thịnh    - 20146535", font="Arial 15 bold", fg="darkblue")
myLabel9 = Label(root, text="Cao Thanh Thủy  - 20146537", font="Arial 15 bold", fg="darkblue")
myLabel10 = Label(root, text="Phạm Quang Huy - 20146126", font="Arial 15 bold", fg="darkblue")
myLabel7.place(x=1000, y=360)
myLabel8.place(x=1030, y=390)
myLabel9.place(x=1030, y=420)
myLabel10.place(x=1030, y=450)

#Tạo nút nhấn upload hình và thoát giao diện
btnUpload = Button(root, text="UPLOAD", font="Arial 25 bold", fg="red", bg = "Snow3", command=upload_image)
btnUpload.place(x=1150, y=570, anchor=CENTER)
btnClose = Button(root, text="CLOSE", font="Arial 25 bold", fg="red", bg = "Snow3", command=CLOSE)
btnClose.place(x=1150, y=660, anchor=CENTER)

#Tạo label hiển thị ảnh trên giao diện
sign_image = Label(root)
sign_image.place(x=700, y=400, anchor=CENTER)
#Tạo label hiển thị kết quả nhận diện trên giao diện
label = Label(root, font=('arial', 15, 'bold'))
label.place(x=700, y=620, anchor=CENTER)


root.mainloop()
