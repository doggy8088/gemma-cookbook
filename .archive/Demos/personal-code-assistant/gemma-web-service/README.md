# Gemma 網路服務

使用 Python、Keras、JAX 和 JAX 簡單實作 Gemma Web 服務
FastAPIlibrary。
### 安裝所需軟體

本專案使用Python 3和虛擬環境（`venv`）來管理套件
並執行應用程式。以下安裝說明適用於 Linux
主機。
要安裝所需的軟體：
*  安裝Python 3 和Python 的`venv` 虛擬環境包：

        sudo apt update
        sudo apt install git pip python3-venv

#### 安裝 Python 庫

使用`venv` Python 虛擬環境安裝Python 庫
啟動以管理Python套件和依賴項。確保您啟動了
Python 虛擬環境*在*使用`pip` 安裝Python 庫之前
安裝程式。有關使用 Python 虛擬環境的更多信息，請參閱
[Python venv](https://docs.python.org/3/library/venv.html) 文件。
要安裝 Python 庫：
1.  在終端機視窗中，導覽至 `gemma-web-service` 目錄：

        cd Gemma/personal-code-assistant/gemma-web-service/

1.  為此項目設定並啟動 Python 虛擬環境 (venv)：

        python3 -m venv venv
        source venv/bin/activate

1.  使用以下命令安裝該專案所需的 Python 庫
    `setup_python` script:

        ./setup_python.sh

提示：在 Linux 作業系統上，您可能需要允許執行 bash
透過執行命令 `chmod +x setup_python.sh` 來編寫腳本。
#### 設定環境變數

這個專案需要幾個環境環境變數才能執行，
包括Kaggle 用戶名和Kaggle API token。您必須有Kaggle
帳戶並要求存取 Gemma 模型才能下載它們。對於
在此項目中，您將Kaggle 用戶名和Kaggle API token 新增至兩個`.env`
由網路應用程式和調整程式讀取的文件，
分別。
注意：將您的Kaggle API token 像密碼一樣對待並保護它
適當地。不要將您的密鑰嵌入公開發布的程式碼中。
設定環境變數：
1.  按照說明取得您的 Kaggle 使用者名稱和 token 金鑰
    in the [Kaggle documentation](https://www.kaggle.com/docs/api#authentication).
1.  依照*取得Gemma*的存取權限來存取Gemma模型
    instructions in the [Gemma Setup](/gemma/docs/setup#get-access) page.
1.  為專案建立環境變數文件，透過建立
    `.env` text file at this location in your clone of the project:
<pre>
個人代碼助理/gemma-web-service/.env</pre>
1.  After creating the `.env` text file, add the following settings to it:

        KAGGLE_USERNAME=<YOUR_KAGGLE_USERNAME_HERE>
        KAGGLE_KEY=<YOUR_KAGGLE_KEY_HERE>

### 執行並測試應用程式

完成專案的安裝和設定後，執行
Web 應用程式以確認您已正確設定它。你應該
在編輯專案供您自己使用之前，請執行此操作作為基準檢查。
執行並測試專案：
1.  在終端機視窗中，導覽至 `gemma-web-service` 目錄：

        cd personal-code-assistant/gemma-web-service/

1.  Run the application using the `run_service` script:

        ./run_service.sh

1.  啟動 Web 服務後，程式碼會列出一個 URL，其中
    you can access the service. Typically, this address is:

        http://localhost:8000/

1.  透過執行 `test_post` 腳本來測試服務：

        ./test/test_post.sh