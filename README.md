# nhapmon-congnghe-phanmem
# Giải thích code Crawl
import requests
# Nhập thư viện requests dùng để gửi HTTP request (tải nội dung trang web).

import os
# Nhập thư viện os để tương tác với hệ điều hành (kiểm tra sự tồn tại của thư mục/file).

import json
# Nhập thư viện json để làm việc với dữ liệu định dạng JSON (chuyển đổi dict sang JSON string).

from bs4 import BeautifulSoup
# Nhập BeautifulSoup từ thư viện bs4 để phân tích cú pháp HTML và trích xuất dữ liệu.

data = []
# Khởi tạo một danh sách (list) rỗng để lưu trữ thông tin của các hội thảo sau khi cào (crawl) về.

def crawlData ( url ):
# Khai báo hàm `crawlData` nhận vào tham số là một đường dẫn `url` cần cào dữ liệu.

    resp = requests . get ( url )
    # Gửi yêu cầu GET đến trang web và lưu phản hồi vào biến `resp`.

    soup = BeautifulSoup ( resp . content , "html.parser" )
    # Tạo đối tượng BeautifulSoup từ nội dung HTML của trang web để bắt đầu phân tích.

    links = soup . select ( 'table.conference:first-of-type > tbody >tr' )
    # Dùng CSS selector để tìm bảng đầu tiên có class là 'conference', sau đó lấy tất cả các dòng (`<tr>`) nằm trong thân bảng (`<tbody>`).

    for link in links :
    # Bắt đầu vòng lặp duyệt qua từng dòng (`link`) vừa tìm được trong danh sách.

        confers = link . find ( 'a' ). text
        # Tìm thẻ `<a>` đầu tiên trong dòng để lấy tên hội thảo (dưới dạng văn bản).

        confers_link = link . find ( 'a' )[ 'href' ]
        # Lấy giá trị của thuộc tính `href` trong thẻ `<a>` vừa tìm để làm đường dẫn chi tiết của hội thảo.

        locations = link . find ( 'td' , attrs = { 'class' : 'location' }). text
        # Tìm thẻ `<td>` có thuộc tính `class="location"` trong dòng để lấy thông tin về địa điểm tổ chức.

        try :
        # Thử thực hiện khối lệnh bên dưới (dùng để bắt lỗi khi một số trường dữ liệu không tồn tại).

            deadlines = link . find ( 'td' , attrs = { 'class' : 'now-deadline' }). text
            # Cố gắng tìm thẻ `<td>` có class là 'now-deadline' (hạn nộp đang diễn ra) để lấy nội dung.

        except :
        # Nếu câu lệnh trong `try` gặp lỗi (không tìm thấy class 'now-deadline'), chương trình sẽ chuyển sang chạy phần này.

            deadlines = link . find ( 'td' , attrs = { 'class' : 'deadline' }). text
            # Nếu không có class 'now-deadline', chương trình sẽ chuyển sang tìm thẻ `<td>` có class là 'deadline' để lấy hạn nộp.

        dates = link . find ( 'td' , attrs = { 'class' : 'date' }). text
        # Tìm thẻ `<td>` có class là 'date' để lấy thời gian diễn ra hội thảo.

        notifications = link . find ( 'td' , attrs = { 'class' : 'notification' }). text
        # Tìm thẻ `<td>` có class là 'notification' để lấy thời gian thông báo kết quả.

        subformats = link . find ( 'td' , attrs = { 'class' : 'subformat' }). text
        # Tìm thẻ `<td>` có class là 'subformat' để lấy thông tin về hình thức nộp bài/hội thảo.

        data . append ({
        # Tạo một từ điển (dictionary) chứa các thông tin vừa trích xuất và thêm (`append`) nó vào danh sách `data`.

            "Conference" : confers ,
            # Lưu tên hội thảo vào khóa "Conference".

            "ConferLink" : confers_link , 
            # Lưu đường dẫn hội thảo vào khóa "ConferLink".

            "Location" : locations ,
            # Lưu địa điểm vào khóa "Location".

            "Deadline" : deadlines ,
            # Lưu hạn nộp vào khóa "Deadline".

            "Date" : dates ,
            # Lưu ngày diễn ra vào khóa "Date".

            "Notification" : notifications ,
            # Lưu thời gian thông báo vào khóa "Notification".

            "Subformat" : subformats ,
            # Lưu hình thức vào khóa "Subformat".

        })

    if os . path . exists ( "data/ddata.json" ):
    # Kiểm tra xem thư mục/đường dẫn file "data/ddata.json" đã tồn tại trên máy tính hay chưa.

        json_obj = json . dumps ( data )
        # Nếu file tồn tại, chuyển đổi danh sách dữ liệu `data` thành định dạng chuỗi JSON.

        with open ( "data/ddata.json" , "w" ) as outfile :
        # Mở file "data/ddata.json" ở chế độ ghi (`"w"` - write).

            outfile . write ( json_obj )
            # Ghi toàn bộ chuỗi JSON vừa tạo vào file.

    else :
    # Trường hợp đường dẫn/file lưu không tồn tại.

        print ( "The file does not exists" )
        # In ra màn hình dòng thông báo file không tồn tại.

    return data
    # Trả về danh sách `data` chứa toàn bộ thông tin hội thảo đã cào được sau khi hàm kết thúc.

crawlData ( 'https://www.lix.polytechnique.fr/~hermann/conf.php' )
# Gọi hàm `crawlData` và truyền vào đường dẫn trang web mẫu cần lấy dữ liệu hội thảo.
