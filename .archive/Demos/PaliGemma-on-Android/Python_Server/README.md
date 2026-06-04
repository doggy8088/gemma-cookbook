# 以 Python Django Ninja 建立的 API server

**注意：** 這個 Python server 已經 productize 並部署在 [Render](https://paligemma.onrender.com)。如果你想在本機執行，請依照下列步驟操作：

## 設定步驟
1. 使用 `virtualenv` 或 `venv` 建立 virtual environment。
2. 使用 `pip install -r requirements.txt` 安裝 requirements。
3. 進入 `manage.py` 所在的 `/apiserver` 目錄。
4. 執行 `python manage.py migrate` 完成資料庫初始化。
5. 執行 `mkdir -p apiserver/media/images`。
6. 開啟 [settings.py](apiserver/apiserver/settings.py)，設定以下內容：
  - SECRET_KEY = 'YOUR_DJANGO_SECRET_KEY'
  - ALLOWED HOSTS = ['localhost']

7. 執行 `python manage.py runserver` 啟動 server。
8. 開啟 [http://127.0.0.1:8000/api/docs#/default/api_views_detect](http://127.0.0.1:8000/api/docs#/default/api_views_detect) 測試 API。
