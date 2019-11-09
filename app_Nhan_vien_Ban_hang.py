 
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, Markup
from Xu_ly.Nhan_vien_Ban_hang.Xu_ly_3L import *

app = Flask(__name__, static_url_path="", static_folder="Media",template_folder='Giao_dien')
app.secret_key = "super secret key"

@app.route("/", methods=['GET', 'POST'])
def Dang_nhap():
# ****** Khởi động Dữ liệu Nguồn/Nội bộ ********
    if session.get("Nhan_vien_Dang_nhap"):
        return redirect(url_for('index'))
    Cong_ty = Doc_Cong_ty()
    Ten_dang_nhap = ""
    Mat_khau = ""
    Chuoi_Thong_bao = "Xin vui lòng Nhập Tên đăng nhập và Mật khẩu"
    if request.method == 'POST':
        Ten_dang_nhap = request.form.get('Th_Ten_dang_nhap')
        Mat_khau = request.form.get('Th_Mat_khau')
        Nhan_vien = Dang_nhap_Nhan_vien(
            Cong_ty["Danh_sach_Nhan_vien_Ban_hang"], Ten_dang_nhap, Mat_khau)
        Hop_le = (Nhan_vien != None)
        if Hop_le:            
            session['Nhan_vien_Dang_nhap'] = Nhan_vien
            return redirect(url_for('index'))
        else:
            Chuoi_Thong_bao = "Đăng nhập không hợp lệ"
    Khung = render_template(
        'Nhan_vien_Ban_hang/MH_Dang_nhap.html',
        Chuoi_Thong_bao=Chuoi_Thong_bao, Ten_dang_nhap=Ten_dang_nhap, Mat_khau=Mat_khau)
    return Khung

@app.route("/Nhan_vien_Ban_hang", methods=['GET', 'POST'])
def index():
# ****** Khởi động Dữ liệu Nguồn/Nội bộ ********   
    Nhan_vien_Dang_nhap = session["Nhan_vien_Dang_nhap"]
    Chuoi_HTML_Nhan_vien = Tao_chuoi_HTML_Nhan_vien(Nhan_vien_Dang_nhap)
    
    Dia_chi_MH = "/Nhan_vien_Ban_hang/Xem_Danh_sach_Tivi"
    
    if request.method == 'POST':
        Ma_so = request.form.get('Th_Ma_so')     
        if Ma_so == "DANH_SACH":           
            Dia_chi_MH = "/Nhan_vien_Ban_hang/Xem_Danh_sach_Tivi"           
        if Ma_so == "TRA_CUU":
            Chuoi_Tra_cuu = request.form.get('Th_Chuoi_Tra_cuu')
            Dia_chi_MH = "/Nhan_vien_Ban_hang/Tra_cuu/" + Chuoi_Tra_cuu + "/"   
        if Ma_so == "DOANH_THU":           
            Dia_chi_MH = "/Nhan_vien_ban_hang/Thong_ke"      
        
    return render_template(
        'Nhan_vien_ban_hang/MH_Chinh.html', Dia_chi_MH=Dia_chi_MH, Chuoi_HTML_Nhan_vien =  Chuoi_HTML_Nhan_vien, )

def Thong_tin():
    Nhan_vien_Dang_nhap = session["Nhan_vien_Dang_nhap"]
    Chuoi_HTML_Nhan_vien = Tao_chuoi_HTML_Nhan_vien(Nhan_vien_Dang_nhap)
    Danh_sach_Tivi=Doc_Danh_sach_Tivi()
    Danh_sach_Tivi_theo_Nhan_vien = Doc_Danh_sach_Tivi_theo_Nhan_vien(Danh_sach_Tivi, Nhan_vien_Dang_nhap)
    return Chuoi_HTML_Nhan_vien, Danh_sach_Tivi_theo_Nhan_vien
 
@app.route("/Nhan_vien_Ban_hang/Xem_Danh_sach_Tivi", methods=['GET', 'POST'])
def Xem_Danh_sach_Tivi():    
    print("I am here!!!!!")
    Chuoi_HTML_Nhan_vien, Danh_sach_Tivi_theo_Nhan_vien = Thong_tin()
 # ****** Khai báo Biến ********   
    Danh_sach_Tivi_Xem=Danh_sach_Tivi_theo_Nhan_vien # Biến Kết quả     
# ****** Kết xuất  ********  
    Chuoi_HTML_Danh_sach_Tivi=Tao_Chuoi_HTML_Danh_sach_Tivi(
           Danh_sach_Tivi_Xem)
    Khung= render_template('Nhan_vien_ban_hang/MH_Xem_Danh_sach_Tivi.html', 
       Chuoi_HTML_Nhan_vien =  Chuoi_HTML_Nhan_vien,
       Chuoi_HTML_Danh_sach_Tivi=Chuoi_HTML_Danh_sach_Tivi)
    return Khung

@app.route("/Nhan_vien_Ban_hang/Tra_cuu/<string:Chuoi_Tra_cuu>/", methods=['GET', 'POST'])
def Tra_cuu_Tivi_theo_Chuoi_Tra_cuu(Chuoi_Tra_cuu):    
    print('Cần phải vào đây: ',Chuoi_Tra_cuu)    
    # ****** Khởi động Dữ liệu Nguồn/Nội bộ ********   
    Chuoi_HTML_Nhan_vien, Danh_sach_Tivi_theo_Nhan_vien = Thong_tin()
 # ****** Khai báo Biến ********
    Danh_sach_Tivi_Xem=Danh_sach_Tivi_theo_Nhan_vien 
    # Biến Kết quả 
    Danh_sach_Tivi_Xem= Tra_cuu_Tivi(Chuoi_Tra_cuu,Danh_sach_Tivi_theo_Nhan_vien)
    
# ****** Kết xuất  ********  
    Chuoi_HTML_Danh_sach_Tivi=Tao_Chuoi_HTML_Danh_sach_Tivi(
           Danh_sach_Tivi_Xem)
    Khung= render_template('Nhan_vien_ban_hang/MH_Xem_Danh_sach_Tivi.html', 
       Chuoi_Tra_cuu=Chuoi_Tra_cuu, Chuoi_HTML_Nhan_vien =  Chuoi_HTML_Nhan_vien,
       Chuoi_HTML_Danh_sach_Tivi=Chuoi_HTML_Danh_sach_Tivi)
    return Khung 

@app.route("/Nhan_vien_Ban_hang/Ban/<string:Ma_so>/", methods=['GET', 'POST'])
def Nhan_vien_Ban_Tivi(Ma_so):
    Nhan_vien_Dang_nhap = session["Nhan_vien_Dang_nhap"]
    Chuoi_HTML_Nhan_vien = Tao_chuoi_HTML_Nhan_vien(Nhan_vien_Dang_nhap)

    Danh_sach_Tivi=Doc_Danh_sach_Tivi()

    Danh_sach_Tivi_theo_Nhan_vien = Doc_Danh_sach_Tivi_theo_Nhan_vien(Danh_sach_Tivi, Nhan_vien_Dang_nhap)
    print("Mã số là:", Ma_so)
    Tivi_Chon = Lay_chi_tiet_Tivi(Danh_sach_Tivi_theo_Nhan_vien, Ma_so)

    if Tivi_Chon != None:
        So_luong = 1
        Thong_bao = ""
        if request.method == 'POST':
            So_luong = int(request.form.get('Th_So_luong'))
            print("Số lượng: ", So_luong)
            Tien = Ban_Tivi(Nhan_vien_Dang_nhap, Tivi_Chon, So_luong)                        
            Thong_bao = "Vừa bán " +str(So_luong)+ " Tivi " + Tivi_Chon["Ten"] + " - Tiền phải trả là: {:,}".format(Tien).replace(",",".")
            Ghi_Tivi(Tivi_Chon)            
        Chuoi_HTML_Tivi = Tao_Chuoi_HTML_Tivi(Tivi_Chon, Thong_bao, So_luong)
        return render_template(
            'Nhan_vien_Ban_hang/MH_Ban_Tivi.html', Chuoi_HTML_Tivi = Chuoi_HTML_Tivi)

@app.route("/Nhan_vien_ban_hang/Thong_ke", methods=['GET', 'POST'])
def Thong_ke_Doanh_thu():
       
    Chuoi_HTML_Nhan_vien, Danh_sach_Tivi_theo_Nhan_vien = Thong_tin()
    
    Ngay = datetime.now().strftime('%d-%m-%Y')
    Danh_sach_Tivi_ban = Danh_sach_Tivi_Da_ban_Theo_ngay(Danh_sach_Tivi_theo_Nhan_vien, Ngay)
    

    Danh_sach_Thong_ke = Tong_ket_Danh_sach_Tivi(Danh_sach_Tivi_ban, Ngay)
    print(Danh_sach_Thong_ke)

    Chuoi_HTML_Thong_ke_Tivi =  Tao_Chuoi_HTML_Thong_ke_Tivi(Danh_sach_Thong_ke)   
    return render_template(
            'Nhan_vien_Ban_hang/MH_Xem_Doanh_thu.html', Chuoi_HTML_Thong_ke_Tivi = Chuoi_HTML_Thong_ke_Tivi)


@app.route("/Nhan_vien_Ban_hang/Dang_xuat/", methods=['GET', 'POST'])
def Dang_xuat():
    session.pop('Nhan_vien_Dang_nhap', None)
    return redirect(url_for('Dang_nhap'))

if __name__ == "__main__":
    app.debug = True
    #app.run()
    app.run(host='127.0.0.1', port=5002)
    
    
