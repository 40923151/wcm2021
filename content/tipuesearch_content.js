var tipuesearch = {"pages": [{'title': '下學期網際內容管理', 'text': '\n', 'tags': '', 'url': '下學期網際內容管理.html'}, {'title': '課程進度', 'text': '', 'tags': '', 'url': '課程進度.html'}, {'title': '第三周', 'text': '更新cmsimde \n 簡化cmsimde/python wsgi.py 和 git push \n \n \n 先 git pull 把新的內容抓下來 \n \n \n 再把者五個檔案選起來複製 \n \n \n 貼到自己倉儲的目錄 \n \n \n 再來測試看看就可以了 \n \n \n 測試git add\xa0 git commit\xa0 git push 是否正常 \n \n', 'tags': '', 'url': '第三周.html'}, {'title': '第四~九週', 'text': "同步 github 和 heroku \n \n 要先依序設定這些 \n 完成後就可以在cmd登入你的heroku \n 再來就可以同步了 \n \n \n \n \n heroku 查詢課表app 建立過程 \n \n 先到老師的倉儲 git calone nfulist 到自己的倉儲 \n \n \n \n \n 點進來後修改 wsgi.py \n \n 去老師的wcm2021裡找 \n \n 再貼到這上面 \n 另存 檔名叫 wsgi.py 覆蓋掉原本 nfulist 裡的\xa0 wsgi.py \n \n 再來要把 proxy 屏蔽掉 \n 原因:在heroku開啟app時是外部的連線所以不需要設定proxy \n \n \n 還要新增這兩的變數 \n 1: semester = request.args.get('semester')\xa0 \n 2:classroomno = request.args.get('classroomno') \n 沒理解錯誤的話\xa0 semester 是控制第幾學年的第幾個學期 \n \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 classroomno 是控制要第幾間教室的課表 \n \n 都改完就可以把 nfulist 推到 heroku \n 再來打開 app \n \n \n \n 改改看變數 有成功換教室就是完成了 \n 中間要用問號隔開 \n ?classroomno=BGA0730 \n \n", 'tags': '', 'url': '第四~九週.html'}, {'title': '第十四週', 'text': '', 'tags': '', 'url': '第十四週.html'}]};