from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, Markup
from Xu_ly.Khach_tham_quan.Xu_ly_3L import *


app = Flask(__name__, static_url_path="", static_folder="Media",template_folder='Giao_dien')
app.secret_key = "super secret key"
 
@app.route("/", methods=['GET', 'POST'])
def index1():
    # ****** Khởi động Dữ liệu Nguồn/Nội bộ ********
    Danh_sach_Tivi = Doc_Danh_sach_Tivi()

 # ****** Khai báo Biến ********
    Chuoi_Tra_cuu="" # Biến Nhập liệu
    Danh_sach_Tivi_Xem = Danh_sach_Tivi # Biến Kết quả 

# ****** Nhập liệu và Xử lý nếu Hợp lệ ********  
    if (request.form.get('Th_Chuoi_Tra_cuu') !=None):
       Chuoi_Tra_cuu=request.form.get('Th_Chuoi_Tra_cuu')
       Danh_sach_Tivi_Xem= Tra_cuu_Tivi(Chuoi_Tra_cuu,Danh_sach_Tivi)

# ****** Kết xuất  ********  
    Chuoi_HTML_Danh_sach_Tivi=Tao_Chuoi_HTML_Danh_sach_Tivi(
           Danh_sach_Tivi_Xem)
    Khung= render_template('Khach_tham_quan/MH_Chinh.html', 
       Chuoi_Tra_cuu=Chuoi_Tra_cuu,
       Chuoi_HTML_Danh_sach_Tivi=Chuoi_HTML_Danh_sach_Tivi)
    return Khung
def index():
    # ****** Khởi động Dữ liệu Nguồn/Nội bộ ********
    Danh_sach_Tivi = Doc_Danh_sach_Tivi()

    # ****** Khai báo Biến ********
    Chuoi_Tra_cuu="" # Biến Nhập liệu
    Danh_sach_Tivi_Xem = Danh_sach_Tivi # Biến Kết quả 

    # ****** Nhập liệu và Xử lý nếu Hợp lệ ********  
    if (request.form.get('Th_Chuoi_Tra_cuu') !=None):
        Chuoi_Tra_cuu=request.form.get('Th_Chuoi_Tra_cuu')
        Danh_sach_Tivi_Xem= Tra_cuu_Tivi(Chuoi_Tra_cuu,Danh_sach_Tivi)

    # ****** Kết xuất  ********  
    Chuoi_HTML_Danh_sach_Tivi=Tao_Chuoi_HTML_Danh_sach_Tivi(
            Danh_sach_Tivi_Xem)
    Khung= render_template('Khach_tham_quan/MH_Chinh.html', 
        Chuoi_Tra_cuu=Chuoi_Tra_cuu,
        Chuoi_HTML_Danh_sach_Tivi=Chuoi_HTML_Danh_sach_Tivi)
    return Khung

if __name__ == "__main__":
    app.debug = True
    #app.run()
    app.run(host='127.0.0.1', port=5001)
    
    
