from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, Markup
from Xu_ly.Quan_ly_Nhap_hang.Xu_ly_3L import *

app = Flask(__name__, static_url_path="",
            static_folder="Media", template_folder='Giao_dien')
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
            Cong_ty["Danh_sach_Quan_ly_Nhap_hang"], Ten_dang_nhap, Mat_khau)
        Hop_le = (Nhan_vien != None)
        if Hop_le:
            session['Nhan_vien_Dang_nhap'] = Nhan_vien
            return redirect(url_for('index'))
        else:
            Chuoi_Thong_bao = "Đăng nhập không hợp lệ"
    Khung = render_template(
        'Quan_ly_Nhap_hang/MH_Dang_nhap.html',
        Chuoi_Thong_bao=Chuoi_Thong_bao, Ten_dang_nhap=Ten_dang_nhap, Mat_khau=Mat_khau)
    return Khung


@app.route("/Quan_ly_Nhap_hang", methods=['GET', 'POST'])
def index():
    # ****** Khởi động Dữ liệu Nguồn/Nội bộ ********
    Nhan_vien_Dang_nhap = session["Nhan_vien_Dang_nhap"]
    Chuoi_HTML_Nhan_vien = Tao_chuoi_HTML_Nhan_vien(Nhan_vien_Dang_nhap)
    Dia_chi_MH = "/Quan_ly_Nhap_hang/Xem_Danh_sach_Tivi"

    if request.method == 'POST':
        Ma_so = request.form.get('Th_Ma_so')
        if Ma_so == "DANH_SACH":
            Dia_chi_MH = "/Quan_ly_Nhap_hang/Xem_Danh_sach_Tivi"
        if Ma_so == "TRA_CUU":
            Chuoi_Tra_cuu = request.form.get('Th_Chuoi_Tra_cuu')
            Dia_chi_MH = "/Quan_ly_Nhap_hang/Tra_cuu/" + Chuoi_Tra_cuu + "/"
        # PHIEU_NHAP
        if Ma_so == "SO_LUONG_TON":            
            Dia_chi_MH = "/Quan_ly_Nhap_hang/Thong_ke/"

    return render_template(
        'Quan_ly_Nhap_hang/MH_Chinh.html', Dia_chi_MH=Dia_chi_MH, Chuoi_HTML_Nhan_vien=Chuoi_HTML_Nhan_vien, )


def Thong_tin():
    Nhan_vien_Dang_nhap = session["Nhan_vien_Dang_nhap"]
    Chuoi_HTML_Nhan_vien = Tao_chuoi_HTML_Nhan_vien(Nhan_vien_Dang_nhap)
    Danh_sach_Tivi = Doc_Danh_sach_Tivi()

    return Chuoi_HTML_Nhan_vien, Danh_sach_Tivi


@app.route("/Quan_ly_Nhap_hang/Xem_Danh_sach_Tivi", methods=['GET', 'POST'])
def Xem_Danh_sach_Tivi():    
    Chuoi_HTML_Nhan_vien, Danh_sach_Tivi = Thong_tin()
 # ****** Khai báo Biến ********
    Danh_sach_Tivi_Xem = Danh_sach_Tivi # Biến Kết quả
# ****** Kết xuất  ********
    Chuoi_HTML_Danh_sach_Tivi = Tao_Chuoi_HTML_Danh_sach_Tivi(
        Danh_sach_Tivi_Xem)
    Khung = render_template('Quan_ly_Nhap_hang/MH_Xem_Danh_sach_Tivi.html',
                            Chuoi_HTML_Nhan_vien=Chuoi_HTML_Nhan_vien,
                            Chuoi_HTML_Danh_sach_Tivi=Chuoi_HTML_Danh_sach_Tivi)
    return Khung

@app.route("/Quan_ly_Nhap_hang/Tra_cuu/<string:Chuoi_Tra_cuu>/", methods=['GET', 'POST'])
def Tra_cuu_Tivi_theo_Chuoi_Tra_cuu(Chuoi_Tra_cuu):
    print('Cần phải vào đây: ', Chuoi_Tra_cuu)
    # ****** Khởi động Dữ liệu Nguồn/Nội bộ ********
    Chuoi_HTML_Nhan_vien, Danh_sach_Tivi = Thong_tin()
 # ****** Khai báo Biến ********
    Danh_sach_Tivi_Xem = Danh_sach_Tivi
    # Biến Kết quả
    Danh_sach_Tivi_Xem = Tra_cuu_Tivi(
        Chuoi_Tra_cuu, Danh_sach_Tivi)

# ****** Kết xuất  ********
    Chuoi_HTML_Danh_sach_Tivi = Tao_Chuoi_HTML_Danh_sach_Tivi(
        Danh_sach_Tivi_Xem)
    Khung = render_template('Quan_ly_Nhap_hang/MH_Xem_Danh_sach_Tivi.html',
                            Chuoi_Tra_cuu=Chuoi_Tra_cuu, Chuoi_HTML_Nhan_vien=Chuoi_HTML_Nhan_vien,
                            Chuoi_HTML_Danh_sach_Tivi=Chuoi_HTML_Danh_sach_Tivi)
    return Khung

@app.route("/Quan_ly_Nhap_hang/Cap_nhat/<string:Ma_so>/", methods=['GET', 'POST'])
def Quan_ly_Nhap_Tivi(Ma_so):
    Nhan_vien_Dang_nhap = session["Nhan_vien_Dang_nhap"]
    Chuoi_HTML_Nhan_vien, Danh_sach_Tivi = Thong_tin()   
    print("Mã số là:", Ma_so)
    Tivi_Chon = Lay_chi_tiet_Tivi(Danh_sach_Tivi, Ma_so)
    if Tivi_Chon != None:
        Don_gia_Nhap = 0
        Thong_bao = ""
        if request.method == 'POST':
            Don_gia_Nhap = int(request.form.get("Th_Don_gia_Nhap"))
            print("Đơn giá nhập: ", Don_gia_Nhap)            
            Tivi_Chon["Don_gia_Nhap"] = Don_gia_Nhap
            Ghi_Tivi(Tivi_Chon)
            Thong_bao = "Cập nhật thành công đơn giá mới là " + \
                " {:,}".format(Don_gia_Nhap).replace(",", ".") 

        Chuoi_HTML_Tivi = Tao_Chuoi_HTML_Tivi(Tivi_Chon, Thong_bao, Don_gia_Nhap)
        return render_template(
            'Quan_ly_Nhap_hang/MH_Cap_nhap_Tivi.html', Chuoi_HTML_Tivi=Chuoi_HTML_Tivi)


@app.route("/Quan_ly_Nhap_hang/Thong_ke/", methods=['GET', 'POST'])
def Thong_ke_SL_ton():
    Chuoi_HTML_Nhan_vien, Danh_sach_Tivi = Thong_tin()
    Cong_ty = Doc_Cong_ty()
    Danh_sach_Nhom_Tivi = Cong_ty["Danh_sach_Nhom_Tivi"]

    Danh_sach_Thong_ke = Thong_ke_So_luong_Ton(Danh_sach_Nhom_Tivi, Danh_sach_Tivi)
    print(Danh_sach_Thong_ke)

    Chuoi_HTML_Thong_ke_Tivi = Tao_Chuoi_HTML_Thong_ke_Tivi(Danh_sach_Thong_ke)
    return render_template(
        'Quan_ly_Nhap_hang/MH_Xem_SL_Ton.html', Chuoi_HTML_Thong_ke_Tivi=Chuoi_HTML_Thong_ke_Tivi)

@app.route("/Quan_ly_Nhap_hang/Dang_xuat/", methods=['GET', 'POST'])
def Dang_xuat():
    session.pop('Nhan_vien_Dang_nhap', None)
    return redirect(url_for('Dang_nhap'))


if __name__ == "__main__":
    app.debug = True
    # app.run()
    app.run(host='127.0.0.1', port=5004)
