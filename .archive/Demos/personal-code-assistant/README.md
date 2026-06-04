# Gemma 個人人工智慧程式碼助理 |使用 Google AI 進行構建

透過此程式碼項目，您可以透過將模型包裝在 Web 服務中並建立 Visual Studio Code extension 來與其通信，從而使用 Gemma 創建自己的個人 AI 編碼助理。
此項目包含2個子項目：
- **gemma-web-service** - 一個 Gemma 2 2B 模型，封裝在一個用 Python 和 FastAPI library 寫的簡單 Web 服務中。
- **pipet-code-agent-2** - Visual Studio Code extension 用 Node.js 編寫，連接到 Gemma 服務以處理程式碼產生和其他請求。
