import sqlite3
from Xu_ly.Khach_tham_quan.Xu_ly_3L import *
# conn = sqlite3.connect('Du_lieu/ql_ban_tivi.db')
# # chuoi_sql = "Select Ten, Ma_so, Ky_hieu, Don_gia_Ban, Don_gia_Nhap, So_luong_Ton from tblTivi"
# # cursor = conn.execute(chuoi_sql)
# # for item in cursor:
# #     print(item[0])

# chuoi_sql = 'insert into tblCongty(Ten,Ma_so,Dien_thoai,Dia_chi,Mail) values(?,?,?,?,?)'
# curror = conn.execute(chuoi_sql, ('Cong Ty TNHH A', '123456', '10909090909','Nguyen Chi Thanh', 'mail@gmail.com'))
# conn.commit()
# conn.close()

# conn = sqlite3.connect('Du_lieu/sqlite/db_module_2.db')
# dsTivi = Doc_Danh_sach_Tivi()
# for tv in dsTivi:
#     chuoiSQL = 'insert into tblTivi(Ma_so,Ten,Ky_hieu,Don_gia_ban,Don_gia_nhap,So_luong_Ton,Ma_so_nhom) values(?,?,?,?,?,?,?)'
#     conn.execute(chuoiSQL, ( tv['Ma_so'],tv['Ten'],tv['Ky_hieu'],tv['Don_gia_Ban'],tv['Don_gia_Nhap'],tv['So_luong_Ton'],tv['Nhom_Tivi']['Ma_so'] ) )
#     conn.commit()
# conn.close()

# conn = sqlite3.connect('Du_lieu/sqlite/db_module_2.db')
# dsTivi = Doc_Danh_sach_Tivi()
# ds_nhom_tivi = []
# for tv in dsTivi:
#     if tv['Nhom_Tivi']['Ma_so'] in ds_nhom_tivi:
#         continue
#     else:
#         ds_nhom_tivi.append(tv['Nhom_Tivi']['Ma_so'])
#     chuoiSQL = 'insert into tblNhomTivi(Ma_so,Ten_Nhom) values(?,?)'
#     conn.execute(chuoiSQL, ( tv['Nhom_Tivi']['Ma_so'] , tv['Nhom_Tivi']['Ten'] ))
#     conn.commit()
# conn.close()