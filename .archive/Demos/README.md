# 展示複雜的端對端用例

此資料夾包含「Build with AI」影片系列的配套 notebooks，以及來自行動應用程式演示的程式碼範例。在這裡，您將找到實用範例和可立即執行的程式碼，幫助您將人工智慧驅動的功能變為現實。
## 隨附notebooks 觀看「Build with AI」影片系列
| 資料夾 | 描述 || ----------------------------------------------------------- | ----------- |
| [商務郵件助理](business-email-assistant/) | [帶有Gemma的商業電子郵件人工智慧助理](https://www.youtube.com/watch?v=YxhzozLH1Dk)<br>該專案解決了將發送給麵包店的電子郵件中的訂單資訊提取為結構化資料的特定問題，以便可以將其快速添加到訂單處理系統中。 || [個人代碼助理](personal-code-assistant/) | [帶有Gemma的個人人工智慧程式碼助理](https://www.youtube.com/watch?v=Zpo7UTvg_9E)<br>這個專案向您展示如何建立自己的網路服務來託管Gemma並將其連接到 MicrosoftVisual Studio Codeextension，以便在編碼時更方便地使用模型。 || [口說任務](spoken-language-tasks/) | [帶有Gemma的口語人工智慧助理](https://www.youtube.com/watch?v=M4HGJehH4r0)<br>學習如何調整模型以特定語言執行特定任務，而不需要大量資料或訓練時間。 |
## 行動應用程式演示
| 資料夾 | 描述 || ----------------------------------------------------------- | ----------- |
| [Android 上Gemma](Gemma-on-Android/) | Android 應用程式使用MediaPipe LLM Inference API 部署微調的Gemma-2B-it 模型。 || [Android 上PaliGemma](PaliGemma-on-Android/) | Android 上的推論 PaliGemma 使用 Hugging Face 和 Gradio 用戶端 API 執行零樣本物件偵測、圖像字幕和視覺問答等任務。 |
## 網頁應用程式演示
| 資料夾 | 描述 || ----------------------------------------------------------- | ----------- |
| [PaliGemma 2 網路](PaliGemma2-on-Web/) | 使用其 ONNX 權重和 Transformers.js 在網路上推論 PaliGemma 2 來執行物件偵測、影像字幕、OCR 和視覺問答等任務。 || [Gemma 3 網路](Gemma3-on-Web/) | 使用其 ONNX 權重和 Transformers.js 在網路上執行 Gemma 3 270M 模型，專注於聊天功能以及 system prompt 的客製化。 || [網路上的表情符號Gemma](Emoji-Gemma-on-Web/) | 了解如何微調 Gemma 3 270M 模型以進行表情符號翻譯，並使用 MediaPipe LLM Inference API 或 Transformers.js 在瀏覽器用戶端執行它。 |
## Cloud Run 演示
| 資料夾 | 描述 || ----------------------------------------------------------- | ----------- |
| [Gemma 雲端運作](Gemma-on-Cloudrun/) | 此資料夾包含一個 Dockerfile，用於在 Cloud Run 上建置和部署 Gemma 驅動的應用程序，其中包括 Gemini APIs。 |
