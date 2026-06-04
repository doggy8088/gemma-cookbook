# Personal AI Code Assistant with Gemma | Build with Google AI

這個程式碼專案可讓你透過 web service 包裝 Gemma 模型，並建立一個與之通訊的 Visual Studio Code extension，打造屬於你自己的個人 AI coding assistant。

這個專案包含 2 個子專案：

- **gemma-web-service** - 以 Python 與 FastAPI library 撰寫的簡易 web service，內含一個 Gemma 2 2B 模型。
- **pipet-code-agent-2** - 以 Node.js 撰寫的 Visual Studio Code extension，可連接 Gemma service 來處理程式碼生成與其他請求。
