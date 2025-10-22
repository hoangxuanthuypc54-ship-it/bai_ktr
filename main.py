# Viết chương trình guizero hiển thị một thiệp chúc mừng đơn giản, gồm:

# Một cửa sổ App có tiêu đề là "Chúc mừng", màu nền "lightblue" và bố cục layout dạng grid.

# Một dòng Text hiển thị nội dung "Chúc bạn một ngày vui vẻ!", font "Arial", size 20, màu "red".

# Một Picture hiển thị ảnh "flower.png" (ảnh có sẵn trong thư mục).

# Cả hai thành phần Text và Picture được bố trí theo grid layout, lần lượt ở các ô [0,0] và [0,1].
from guizero import App, Text, Picture
cuaso = App("Chúc mừng", bg = "lightblue", layout = "grid", width = 330, height = 250)
anh = Picture(cuaso, image = "a1.jpng", width = 150, height = 100, grid = (0,1))
chu = Text(cuaso, "Chúc bạn một ngày vui vẻ!", font = "Arial", size = 20, color = "red", grid = (0,0))
cuaso.display()
