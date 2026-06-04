# 使用 MediaPipe LLM Inference API 在瀏覽器中執行微調後的 Gemma 3 270M 模型

這個 app 示範如何在瀏覽器中直接執行微調後的 Gemma 3 270M 模型，根據文字輸入產生 emoji。對這個 demo 而言，你只需要改一行程式碼，讓它指向你的 MediaPipe Task model bundle。

## 執行 demo
1. 下載本目錄中的 app 檔案，並將你的 `.task` model bundle 放進本機 app 資料夾。
2. 在 `worker.js` 檔案中，更新 `modelPath`，讓它指向該 `.task` 檔案。
3. 在電腦上開啟 terminal，並切換（`cd`）到 app 資料夾。
4. 執行 `npx serve` 啟動本機 server。
5. 在瀏覽器中開啟提供的 `localhost` 位址，即可執行 app。

## 運作方式
這個 demo 會先架設一個簡單的 web server，提供 frontend 讓使用者輸入文字 prompt。接著會在 web worker 中啟動生成流程，以避免阻塞主 UI thread。worker 使用隨附的 MediaPipe Tasks GenAI package（[@mediapipe/tasks-genai](https://www.npmjs.com/package/@mediapipe/tasks-genai)）版本，從模型產生回應後再回傳給使用者。

**Requirements:** 支援 [WebGPU](https://caniuse.com/webgpu) 的瀏覽器

## 資源
* [Notebook: Fine-tune Gemma 3 270M](https://github.com/google-gemini/gemma-cookbook/blob/main/Demos/Emoji-Gemma-on-Web/resources/Fine_tune_Gemma_3_270M_for_emoji_generation.ipynb)
* [Notebook: Convert Gemma 3 270M for use with MediaPipe](https://github.com/google-gemini/gemma-cookbook/blob/main/Demos/Emoji-Gemma-on-Web/resources/Convert_Gemma_3_270M_to_LiteRT_for_MediaPipe_LLM_Inference_API.ipynb)
* [MediaPipe LLM Inference Web documentation](https://ai.google.dev/edge/mediapipe/solutions/genai/llm_inference/web_js)
