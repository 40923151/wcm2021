import requests
import bs4
# for os.environ and os.system
import os
# for geting html file path
import pathlib
# 以下因應改為 Heroku based 程式所需導入模組,  修改步驟 1/6
from flask import Flask, request 
from flask_cors import CORS
 
 
# 修改步驟 2/6 , 加入 Flask 相關物件設定
app = Flask(__name__)
# 此一設定可以讓程式跨網域擷取資料
CORS(app)
 
# for pythn 3.9,  在近端測試時仍需要設定 proxy, 若使用 Python 3.8 執行則會自動使用系統的 Proxy 設定
proxy = 'http://[2001:288:6004:17::69]:3128'
 
os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
'''
url:  'jclassroom_ajax.php',
data: { pselyr: pselyr, pselclssroom: pselclssroom },
'''
 
# 修改步驟 3/6, 試著將程式改為網際模式, 需要套用 Flask 的網際 decorator
@app.route('/')
def timeTableList():
    semester = '1092'
    classroomno = 'BGA0611'
    column = True
 
    if semester == None:
        semester = '1092'
    if classroomno == None:
        # BGA0810 電腦輔助設計室
        classroomno = 'BGA0611'
         
    headers = {'X-Requested-With': 'XMLHttpRequest'}
 
    url = 'https://qry.nfu.edu.tw/jclassroom_ajax.php'
    post_var = {'pselyr': semester, 'pselclssroom': classroomno}
 
    result = requests.post(url, data = post_var, headers = headers)
 
    soup = bs4.BeautifulSoup(result.content, 'lxml')
 
    # 先除掉所有 anchor
    for a in soup.findAll('a'):
        # bs3 語法
        #a.replaceWithChildren()
        # bs4 語法, 將標註與內容拆開
        a.unwrap()
 
    # 根據輸出設定, 取出 class='tbcls' 的 table 資料
    table = soup.find('table', {'class': 'tbcls'})
 
    # 重建 table, 設定邊線為 1 pixel
    output = "<table border='1'>"
 
    for i in table.contents:
        # 利用 replace 復原  
        output += str(i).replace("&nbsp", " ")
    output += "</table>"
    #print(output)
    # 修改步驟 5/6 , 因為已經將原先可列印出程式的步驟改為 function, 因此必須以 return 將擷取到的網頁資料傳回
    return output
     
# 修改步驟 4/6 , 因為改寫為網際程式後, 下列將內容存檔並自動呼叫 Firefox 的程式碼不再適用, 必須蓋掉
'''
# 將 output 寫入 w1_classroom.html
fileName = "w1_classroom.html"
with open(fileName, "w", encoding="utf-8") as file:
    file.write(output)
# 利用 os.system() 以 default browser 開啟 w1_class_local.html
filePath = pathlib.Path(__file__).parent.absolute()
#print(filePath)
# set firefox as default browser and start url to open html file
os.system("start file:///" + str(filePath) + "\\" + fileName)
'''
 
# 修改步驟 6/6, 配合網際程式啟動,  以及 Python 程式執行與納入其他程式執行的特定進行配置
 
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)