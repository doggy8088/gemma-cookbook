# Python 基於 Django Ninja API 伺服器

**注意：** Python 伺服器已生產並託管在 [Render](https://paligemma.onrender.com) 上。如果您希望在本地執行此程序，請按照以下步驟操作：
## 設定步驟
1. 使用`virtualenv` 或`venv` 建立虛擬環境。
2. 使用`pip install -r requirements.txt` 安裝要求。
3. 進入 manage.py 檔案所在目錄/apiserver。
4. 執行指令`python manage.py migrate`來設定資料庫。
5. 執行命令`mkdir -p apiserver/media/images`。
6. 前往 [settings.py](apiserver/apiserver/settings.py) 並設定以下內容：
  - SECRET_KEY = 'YOUR_DJANGO_SECRET_KEY'
  - ALLOWED HOSTS = ['localhost']
    
7. 執行命令`python manage.py runserver`啟動伺服器。
8. 前往 URL [http://127.0.0.1:8000/api/docs#/default/api_views_detect](http://127.0.0.1:8000/api/docs#/default/api_views_detect) 測試API。
