# gemma-web-service

這是一個使用 Python、Keras、JAX 與 FastAPI library 實作的簡易 Gemma web service。

### 安裝必要軟體

這個專案使用 Python 3 與 Virtual Environments（`venv`）來管理套件並執行應用程式。以下安裝說明以 Linux host machine 為例。

若要安裝必要軟體：

* 安裝 Python 3 與 Python 的 `venv` virtual environment package：

        sudo apt update
        sudo apt install git pip python3-venv

#### 安裝 Python libraries

請在啟用 `venv` Python virtual environment 的情況下安裝 Python libraries，以便管理 Python packages 與 dependencies。請務必先啟用 Python virtual environment，再使用 `pip` installer 安裝 Python libraries。更多關於 Python virtual environments 的資訊，請參考 [Python venv](https://docs.python.org/3/library/venv.html) 文件。

安裝 Python libraries 的步驟如下：

1. 在 terminal 視窗中，切換到 `gemma-web-service` 目錄：

        cd Gemma/personal-code-assistant/gemma-web-service/

1. 為此專案設定並啟用 Python virtual environment（venv）：

        python3 -m venv venv
        source venv/bin/activate

1. 使用 `setup_python` script 安裝本專案所需的 Python libraries：

        ./setup_python.sh

提示：在 Linux 作業系統上，你可能需要先執行 `chmod +x setup_python.sh`，允許該 bash script 執行。

#### 設定環境變數

這個專案執行時需要幾個環境變數，包括 Kaggle username 與 Kaggle API token。你必須擁有 Kaggle 帳號，並申請 Gemma 模型的存取權限，才能下載模型。對此專案而言，你需要把 Kaggle Username 與 Kaggle API token 寫入兩個 `.env` 檔案，分別供 web application 與 tuning program 讀取。

注意：請將 Kaggle API token 視同密碼妥善保護。不要把金鑰寫進公開發佈的程式碼中。

設定環境變數的步驟如下：

1. 依照 [Kaggle documentation](https://www.kaggle.com/docs/api#authentication) 取得你的 Kaggle username 與 token key。
1. 依照 [Gemma Setup](/gemma/docs/setup#get-access) 頁面中的 *Get access to Gemma* 指示，取得 Gemma 模型存取權限。
1. 在你複製下來的專案中，於下列位置建立專案專用的環境變數檔案 `.env`：
<pre>
personal-code-assistant/gemma-web-service/.env
</pre>
1. 建立 `.env` 後，加入下列設定：

        KAGGLE_USERNAME=<YOUR_KAGGLE_USERNAME_HERE>
        KAGGLE_KEY=<YOUR_KAGGLE_KEY_HERE>

### 執行與測試應用程式

完成專案安裝與設定後，請先執行 web application，確認設定正確。這應作為你開始依自身需求修改專案前的 baseline check。

執行與測試專案的步驟如下：

1. 在 terminal 視窗中，切換到 `gemma-web-service` 目錄：

        cd personal-code-assistant/gemma-web-service/

1. 使用 `run_service` script 執行應用程式：

        ./run_service.sh

1. 啟動 web service 後，程式會列出可存取該服務的 URL。通常會是：

        http://localhost:8000/

1. 使用 `test_post` script 測試服務：

        ./test/test_post.sh
