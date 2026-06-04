# 口說任務助理Gemma

本教學將引導您完成設定、執行和擴展語音
使用Gemma 和Python 建立的語言任務應用程式。該應用程式提供
您可以修改以滿足您的需求的基本 Web 使用者介面。應用
旨在為一家虛構的韓國麵包店生成對客戶電子郵件的回复，
所有語言輸入和輸出完全用韓語處理。您可以使用
此應用程式模式適用於任何語言和任何使用文字的業務任務
輸入和文字輸出。
## 項目設定

這些說明將引導您完成此項目的設置
開發和測試。一般步驟是安裝一些先決條件
軟體，從程式碼儲存庫複製項目，設定一些環境
變數，並執行設定安裝。
### 安裝先決條件

本專案使用Python 3和Python Poetry 來管理套件和
執行應用程式。以下安裝說明適用於 Linux
主機。
要安裝所需的軟體：
*  安裝Python 3 和Python 的`venv` 虛擬環境包。
<pre>
須藤 apt 更新
sudo apt install git pip python3-venv</pre>

### 克隆並設定項目

下載專案代碼，使用 Poetry 安裝指令下載
所需的依賴項並設定項目。你需要
[git](https://git-scm.com/) 原始碼控制軟體來檢索
專案原始碼。
下載專案代碼：
1.  使用以下命令克隆 git 儲存庫。
<pre>
git 克隆https://github.com/google-gemini/gemma-cookbook.git</pre>
1.  （可選）設定本機 git 儲存庫以使用稀疏結帳，
    so you have only the files for the project.
<pre>
cd gemma-cookbook/
git 稀疏結帳設定Gemma/spoken-language-tasks/
git 稀疏結帳初始化--cone</pre>

要安裝 Python 庫：
1.  為此項目設定並啟動 Python 虛擬環境 (venv)：
<pre>
python3 -m venv venv
源 venv/bin/activate</pre>
1.  使用 {{setup_python}} 腳本安裝此項目所需的Python 庫。
<pre>
./setup_python.sh</pre>

### 設定環境變數

設定允許此程式碼所需的一些環境變數
要執行的項目，包括 Kaggle 用戶名和 Kaggle token 金鑰。
您必須擁有Kaggle 帳戶並要求存取Gemma 模型。
您將 Kaggle 使用者名稱和 Kaggle token 金鑰新增至兩個 `.env` 檔案中，
分別由 Web 應用程式和調整程式讀取。
注意：將您的 Kaggle token 金鑰視為密碼並對其進行適當保護。
不要將您的密鑰嵌入公開發布的程式碼中。
設定環境變數：
1.  按照說明取得您的 Kaggle 使用者名稱和 token 金鑰
    in the [Kaggle documentation](https://www.kaggle.com/docs/api#authentication)
1.  依照*取得Gemma*的存取權限來存取Gemma模型
    instructions in the [Gemma Setup](/gemma/docs/setup#get-access) page.
1.  為專案建立環境變數文件，透過建立
    `.env` text file at *each* these location in your clone of the project:
<pre>
k-mail-replier/k_mail_replier/.env
k-gemma-it/.env</pre>
1.  建立 `.env` 文字檔案後，將以下設定新增至 **兩個** 檔案：
<pre>
KAGGLE_USERNAME=&lt;YOUR_KAGGLE_USERNAME_HERE&gt;
KAGGLE_KEY=&lt;YOUR_KAGGLE_KEY_HERE&gt;
</pre>

### 執行並測試應用程式

1.  在終端機視窗中，導覽至`spoken-language-tasks/k-mail-replier/k_mail_replier/`
    directory.
<pre>
cd 口說任務/k-mail-replier/
</pre>
1.  Run the application using the `run_flask_app.sh` script:
<pre>
./run_flask_app.sh</pre>
