# 使用MediaPipe LLM Inference API在瀏覽器中執行微調的Gemma 3 270M 模型

此應用程式示範如何使用直接在瀏覽器中執行的經過微調的 Gemma 3 270M 模型從文字輸入產生表情符號。對於此演示，您只需更改一行程式碼以指向您的 MediaPipe 任務模型包。
## 執行演示
1. 下載此目錄中的應用程式文件，並將您的 .task 模型包包含在本機應用程式資料夾中。
2. 在 worker.js 檔案中，更新`modelPath` 以指向.task 檔案。
3. 開啟電腦上的終端機並導航 (`cd`) 到應用程式資料夾。
4. 執行`npx serve`啟動本機伺服器。
5. 在瀏覽器中開啟提供的 `localhost` 位址以執行該應用程式。

## 它是如何運作的
該演示設置了一個簡單的 Web 伺服器來託管前端，用戶可以在其中輸入文字prompt。這會在 Web Worker 中啟動生成過程，以避免阻塞主 UI 執行緒。工作人員使用 MediaPipe Tasks GenAI 套件的捆綁版本 ([@mediapipe/tasks-genai](https://www.npmjs.com/package/@mediapipe/tasks-genai)) 從模型產生回應並將其發送回使用者。
**要求：** 支援 [WebGPU 支援](https://caniuse.com/webgpu) 的瀏覽器
## 資源
* [notebook：微調Gemma 3 270M](https://github.com/google-gemini/gemma-cookbook/blob/main/Demos/Emoji-Gemma-on-Web/resources/Fine_tune_Gemma_3_270M_for_emoji_generation.ipynb)
* [notebook：轉換Gemma 3 270M 以與MediaPipe一起使用](https://github.com/google-gemini/gemma-cookbook/blob/main/Demos/Emoji-Gemma-on-Web/resources/Convert_Gemma_3_270M_to_LiteRT_for_MediaPipe_LLM_Inference_API.ipynb)
* [MediaPipe LLM 推論 Web 文件](https://ai.google.dev/edge/mediapipe/solutions/genai/llm_inference/web_js)
