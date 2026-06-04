# Spoken Language Tasks Assistant with Gemma

這份教學會帶你完成以 Gemma 與 Python 建立的 spoken language task 應用程式的設定、執行與延伸。這個應用程式提供一個基本的 web 使用者介面，你可以依需求修改。它目前是為一家虛構的韓國烘焙坊產生客戶 email 回覆，且所有語言輸入與輸出都完全以韓文處理。你可以將這個應用模式套用到任何語言，以及任何以文字輸入與文字輸出為主的商務任務。

## 專案設定

以下說明會帶你完成本專案的開發與測試設定。整體步驟包括安裝必要軟體、從程式碼 repository 複製專案、設定幾個環境變數，以及執行安裝設定流程。

### 安裝先決條件

這個專案使用 Python 3 與 Python Poetry 來管理套件並執行應用程式。以下安裝說明以 Linux host machine 為例。

若要安裝必要軟體：

* 安裝 Python 3 與 Python 的 `venv` virtual environment package。
<pre>
sudo apt update
sudo apt install git pip python3-venv
</pre>

### 複製並設定專案

下載專案程式碼，並使用 Poetry 安裝命令抓取所需 dependencies 並完成設定。你需要 [git](https://git-scm.com/) source control 軟體來取得專案原始碼。

下載專案程式碼的步驟如下：

1. 使用下列命令複製 git repository。
<pre>
git clone https://github.com/google-gemini/gemma-cookbook.git
</pre>
1. 你也可以選擇設定本機 git repository 使用 sparse checkout，如此只會取回本專案所需檔案。
<pre>
cd gemma-cookbook/
git sparse-checkout set Gemma/spoken-language-tasks/
git sparse-checkout init --cone
</pre>

安裝 Python libraries 的步驟如下：

1. 為此專案設定並啟用 Python virtual environment（venv）：
<pre>
python3 -m venv venv
source venv/bin/activate
</pre>
1. 使用 {{setup_python}} script 安裝本專案所需的 Python libraries。
<pre>
./setup_python.sh
</pre>

### 設定環境變數

設定幾個本程式碼專案執行所需的環境變數，包括 Kaggle user name 與 Kaggle token key。你必須擁有 Kaggle 帳號，並申請 Gemma 模型的存取權限。

你需要將 Kaggle Username 與 Kaggle Token Key 寫入兩個 `.env` 檔案，分別供 web application 與 tuning program 讀取。

注意：請將 Kaggle Token Key 視同密碼妥善保護。不要把金鑰寫進公開發佈的程式碼中。

設定環境變數的步驟如下：

1. 依照 [Kaggle documentation](https://www.kaggle.com/docs/api#authentication) 取得你的 Kaggle username 與 token key
1. 依照 [Gemma Setup](/gemma/docs/setup#get-access) 頁面中的 *Get access to Gemma* 指示，取得 Gemma 模型存取權限。
1. 在你複製下來的專案中，於下列 *每一個* 位置建立 `.env` 文字檔：
<pre>
k-mail-replier/k_mail_replier/.env
k-gemma-it/.env
</pre>
1. 建立 `.env` 文字檔後，將以下設定加入 **兩個** 檔案中：
<pre>
KAGGLE_USERNAME=&lt;YOUR_KAGGLE_USERNAME_HERE&gt;
KAGGLE_KEY=&lt;YOUR_KAGGLE_KEY_HERE&gt;
</pre>

### 執行與測試應用程式

1. 在 terminal 視窗中，切換到 `spoken-language-tasks/k-mail-replier/k_mail_replier/` 目錄。
<pre>
cd spoken-language-tasks/k-mail-replier/
</pre>
1. 使用 `run_flask_app.sh` script 執行應用程式：
<pre>
./run_flask_app.sh
</pre>
