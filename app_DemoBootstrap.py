from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, Markup
from Xu_ly.Khach_tham_quan.Xu_ly_3L import *

app = Flask(__name__, static_url_path="", static_folder="Media",template_folder='Giao_dien')
app.secret_key = "super secret key"

@app.route("/", methods=['GET', 'POST'])
def index_demo_bootstrap():
    Khung= render_template('DemoBootstrap/index.html')
    return Khung

@app.route("/demo-table/<int:page>", methods=['GET', 'POST'])
def demo_table(page):
    Danh_sach_tivi = Doc_Danh_sach_Tivi()
    n = len(Danh_sach_tivi)
    offset = 10
    total = int(n / offset)
    currentPage = (page - 1) * offset
    dsTiviView = Danh_sach_tivi[currentPage:currentPage+offset]
    if n % offset > 0:
        total += 1
    Khung= render_template('DemoBootstrap/table.html', Danh_sach_tivi=dsTiviView, page=page, total=total, currentPage=currentPage)
    return Khung


@app.route("/demo-card", methods=['GET', 'POST'])
def demo_card():
    Danh_sach_tivi = Doc_Danh_sach_Tivi()
    Khung= render_template('DemoBootstrap/card.html', Danh_sach_tivi=Danh_sach_tivi)
    return Khung

@app.route("/demo-modal", methods=['GET', 'POST'])
def demo_modal():
    Danh_sach_tivi = Doc_Danh_sach_Tivi()
    Khung= render_template('DemoBootstrap/modal.html', Danh_sach_tivi=Danh_sach_tivi)
    return Khung

if __name__ == "__main__":
    app.debug = True
    #app.run()
    app.run(host='127.0.0.1', port=5001)