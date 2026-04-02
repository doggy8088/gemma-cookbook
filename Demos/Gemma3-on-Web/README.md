### 由 [Sitam Meur](https://linkedin.com/in/sitammeur) 開發。

# 使用 ONNX 與 Transformers.js 在瀏覽器中對 Gemma 3 執行推論

這是一個簡單的 web app，示範如何在瀏覽器中使用 [Transformers.js](https://huggingface.co/docs/transformers.js) 與 ONNX Runtime Web 執行 [Gemma 3 270M](https://huggingface.co/onnx-community/gemma-3-270m-it-ONNX) 模型。應用程式允許使用者與 Gemma 3 270M 模型對話，並即時取得回應。

## 專案結構

專案結構如下：

- `assets/`：包含最終應用程式截圖的目錄。

- `public/`：圖片、icons、fonts 等靜態資產。

- `src/`：應用程式核心原始碼。

  - `components/`：可重複使用的 React components。

    - `icons/`：應用程式使用的 icon components。

      - `ArrowRightIcon.jsx`：向右箭頭 icon component。
      - `BotIcon.jsx`：Bot icon component。
      - `StopIcon.jsx`：停止 icon component。
      - `UserIcon.jsx`：使用者 icon component。

    - `Chat.jsx`：顯示聊天訊息的 Chat component。
    - `Progress.jsx`：顯示進度條的 Progress component。

  - `styles/`：應用程式樣式用的 CSS 檔案。

    - `index.css`：應用程式的全域 CSS 樣式。
    - `Chat.css`：聊天介面的 CSS 樣式。

  - `worker.js`：用來執行 Gemma 3 模型的 Transformers.js worker。
  - `App.jsx`：應用程式的主要 React component。
  - `main.jsx`：應用程式進入點。

- `.gitignore`：指定哪些檔案與目錄應由 Git 忽略。
- `README.md`：專案文件與 setup 說明。
- `index.html`：應用程式主要 HTML 檔。
- `package.json`：專案 dependencies 與 script 設定。
- `tailwind.config.js`：Tailwind CSS 設定檔。
- `vite.config.js`：專案的 Vite 設定檔。

## 使用技術

- **HTML**：建立 web pages 的標準標記語言。
- **Tailwind CSS**：用於 web app 樣式設計的 utility-first CSS framework。
- **JavaScript**：建構 web app 的高階程式語言。
- **React**：建立使用者介面的 JavaScript library。
- **Transformers.js**：在瀏覽器中執行 Hugging Face 模型的 JavaScript library。

## 快速開始

若要開始使用這個專案，請依照以下步驟：

1. 複製 repository：`git clone https://github.com/google-gemini/gemma-cookbook.git`
2. 切換目錄：`cd gemma-cookbook/Demos/Gemma3-on-Web`
3. 安裝必要 dependencies：`npm install`
4. 啟動應用程式：`npm run dev`

接著在瀏覽器開啟本機位址 `http://localhost:5173/`，即可查看 web application。

> [!NOTE]  
> 第一次執行時，載入模型 weights 大約需要 10 到 15 分鐘。

## 結果

![result](assets/demo1.png)

**注意：** 若要查看結果，請參考 repository 中的 `assets` 資料夾。

## 資源與參考資料

1. [Google for Developers Article](https://developers.googleblog.com/en/introducing-gemma-3-270m/)
2. [Hugging Face ONNX Model](https://huggingface.co/onnx-community/gemma-3-270m-it-ONNX)
3. [Transformers.js GitHub](https://github.com/huggingface/transformers.js)
4. [ONNX Community](https://huggingface.co/onnx-community)
