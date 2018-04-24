import mlab
from models.service import User, Song, Place, Video, Book
mlab.connect()
admin = User.objects(username="admin", password="admin").first()
admin_id = str(admin["id"])
new_book = Book(
                happy = 1,
                name = "Ba Chàng Ngốc",
                author = "Chetan Bhagat",
                link = "http://sachvui.com/ebook/ba-chang-ngoc-chetan-bhagat.2462.html",
                user_id =admin_id)
new_book.save()
new_book1 = Book(
                happy = 1,
                name = "Bố Là Bà Giúp Việc",
                author = "Anne Fine",
                link = "http://sachvui.com/ebook/bo-la-ba-giup-viec-anne-fine.1577.html",
                user_id =admin_id)
new_book1.save()
new_book2 = Book(
                happy = 1,
                name = "Chúa Ơi Chàng Muốn Lấy Con",
                author = "Agnes Abecassis",
                link = "http://sachvui.com/ebook/chua-oi-chang-muon-lay-con-agnes-abecassis.1222.html",
                user_id =admin_id)
new_book2.save()
new_book3 = Book(
                happy = 1,
                name = "Truyện Cười Song Ngữ Anh - Việt",
                author = "Chưa rõ",
                link = "http://sachvui.com/ebook/truyen-cuoi-song-ngu-anh-viet-chua-ro.903.html",
                user_id =admin_id)
new_book3.save()
new_book4 = Book(
                happy = 1,
                name = "Ba Chàng Cùng Hội Cùng Thuyền",
                author = "Jerome Clapka",
                link = "http://sachvui.com/ebook/ba-chang-cung-hoi-cung-thuyen-jord-jerome-clapka.842.html",
                user_id =admin_id)
new_book4.save()
new_book5 = Book(
                happy = 1,
                name = "Tuyển tập truyện cười Vova",
                author = "Chưa rõ",
                link = "http://sachvui.com/ebook/tuyen-tap-truyen-cuoi-vova.626.html",
                user_id =admin_id)
new_book5.save()
new_book6 = Book(
                happy = 1,
                name = "Tiếng cười Bác Ba Phi",
                author = "Nhiều tác giả",
                link = "http://sachvui.com/ebook/tieng-cuoi-bac-ba-phi.501.html",
                user_id =admin_id)
new_book6.save()
new_book7 = Book(
                happy = 1,
                name = "Chuyện đời trong quán rượu",
                author = "Azit Nesin",
                link = "http://sachvui.com/ebook/chuyen-doi-trong-quan-ruou.478.html",
                user_id =admin_id)
new_book7.save()
new_book8 = Book(
                happy = 1,
                name = "Truyện cười dân gian Việt Nam",
                author = "Nhiều tác giả",
                link = "http://sachvui.com/ebook/truyen-cuoi-dan-gian-viet-nam.291.html",
                user_id =admin_id)
new_book8.save()
new_book9 = Book(
                happy = 1,
                name = "Truyện Xiển Bột",
                author = "Khuyết Danh",
                link = "http://sachvui.com/ebook/truyen-xien-bot.244.html",
                user_id =admin_id)
new_book9.save()
new_book10 = Book(
                happy = 1,
                name = "Trạng Quỳnh",
                author = "Khuyết Danh",
                link = "http://sachvui.com/ebook/trang-quynh.242.html",
                user_id =admin_id)
new_book10.save()
new_book11 = Book(
                happy = 1,
                name = "Trạng Lợn",
                author = "Khuyết Danh",
                link = "http://sachvui.com/ebook/trang-lon.241.html",
                user_id =admin_id)
new_book11.save()
new_book12 = Book(
                happy = 1,
                name = "Ba Giai - Tú Xuất",
                author = "Khuyết Danh",
                link = "http://sachvui.com/ebook/ba-giai-tu-xuat.235.html",
                user_id =admin_id)
new_book12.save()
new_book13 = Book(
                happy = 1,
                name = "Truyện Cười Trung Quốc",
                author = "Nguyễn Duy Chiếm",
                link = "http://sachvui.com/ebook/truyen-cuoi-trung-quoc.227.html",
                user_id =admin_id)
new_book13.save()
new_book14 = Book(
                happy = 1,
                name = "Tiếu lâm chính trị Việt Nam năm 1980",
                author = "Trần Khốt",
                link = "http://sachvui.com/ebook/tieu-lam-chinh-tri-viet-nam-nam-1980.211.html",
                user_id =admin_id)
new_book14.save()
new_book15 = Book(
                happy = 1,
                name = "Những người thích đùa",
                author = "Azit Nesin",
                link = "http://sachvui.com/ebook/nhung-nguoi-thich-dua.47.html",
                user_id =admin_id)
new_book15.save()
new_book16 = Book(
                happy = 1,
                name = "Truyện cười Azit Nêxin - Xin ch-ào-ào!",
                author = "Azit Nesin",
                link = "http://sachvui.com/ebook/truyen-cuoi-azit-nexin-xin-ch-ao-ao.43.html",
                user_id =admin_id)
new_book16.save()
new_book17 = Book(
                happy = 1,
                name = "Có Hai Con Mèo Bên Cửa Sổ",
                author = "Nguyễn Nhật Ánh",
                link = "http://sachvui.com/ebook/co-hai-con-meo-ben-cua-so-nguyen-nhat-anh.1374.html",
                user_id =admin_id)
new_book17.save()
new_book18 = Book(
                happy = 1,
                name = "Hoàng Tử Hạnh Phúc Và Những Truyện Khác",
                author = "Oscar Wilde",
                link = "http://sachvui.com/ebook/hoang-tu-hanh-phuc-va-nhung-truyen-khac-oscar-wilde.1582.html",
                user_id =admin_id)
new_book18.save()
new_book19 = Book(
                happy = 1,
                name = "Cái Tết Của Mèo Con",
                author = "Nguyễn Đình Thi - Thùy Dung",
                link = "http://sachvui.com/ebook/cai-tet-cua-meo-con-nguyen-dinh-thi-thuy-dung.2099.html",
                user_id =admin_id)
new_book19.save()
