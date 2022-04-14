from bs4 import BeautifulSoup  #Khai báo thư viện 
import requests #Khai báo thư viện
url = requests.get("https://www.random.org/")
#Truy cập, và gửi Request để Get nội dung , lưu nội dung vào biến url
Soup= BeautifulSoup(url.content,"lxml") #Format lại các nội dung , chỉ lấy các Content, lưu vào biến Soup 

tai = Soup.find_all(True,limit=1) #Tìm nội dung của tất cả các thẻ, rồi cho vào mảng , biến limit = 1 nghĩa là ta chỉ duyệt 1 lần 
for i in tai:
    print(i.text)