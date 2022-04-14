from bs4 import BeautifulSoup #Thư viện trích xuất dữ liệu HTML 

with open('test.xml', 'r') as f: #Mở file XML có trong máy 
	file = f.read() #Lấy nội dung 
soup = BeautifulSoup(file,'lxml') #Trích xuất dữ liệu rồi lưu vào biến soup

names = soup.find_all(True,limit=1)

#Duyệt tất cả các thẻ bằng find_all 

for ttai in names:
    print(ttai.text)