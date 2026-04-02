# 使用 Transformers.js 在瀏覽器中執行微調後的 Gemma 3 270M 模型

這個 app 示範如何在瀏覽器中直接執行微調後的 Gemma 3 270M 模型，根據文字輸入產生 emoji。對這個 demo 而言，你只需要改一行程式碼，讓它指向你的 ONNX 模型。

## 執行 demo
1. 下載本目錄中的 app 檔案。
2. 在 `worker.js` 檔案中，更新 `pipeline()` 函式呼叫中的 model 字串，讓它指向 Hugging Face Hub 上的模型。
    1. 或者，你也可以下載模型檔，並將其放到新的子目錄中，例如 `app-transformersjs/myemoji-gemma-3-270m-it-onnx/`，以便完全離線使用。
3. 在電腦上開啟 terminal，並切換（`cd`）到 app 資料夾。
4. 執行 `npx serve` 啟動本機 server。
5. 在瀏覽器中開啟提供的 `localhost` 位址，即可執行 app。

**Requirements:** 支援 [WebGPU](https://caniuse.com/webgpu) 的瀏覽器

## 運作方式
這個 demo 會先架設一個簡單的 web server，提供 frontend 讓使用者輸入文字 prompt。接著會在 web worker 中啟動生成流程，以避免阻塞主 UI thread。worker 使用 [Transformers.js](https://huggingface.co/docs/transformers.js/index) 從模型產生回應後再回傳給使用者。

## 資源
* [Notebook: Fine-tune Gemma 3 270M](https://github.com/google-gemini/gemma-cookbook/blob/main/Demos/Emoji-Gemma-on-Web/resources/Fine_tune_Gemma_3_270M_for_emoji_generation.ipynb)
* [Notebook: Convert Gemma 3 270M to ONNX](https://github.com/google-gemini/gemma-cookbook/blob/main/Demos/Emoji-Gemma-on-Web/resources/Convert_Gemma_3_270M_to_ONNX.ipynb)
* [Hugging Face Transformers.js documentation](https://huggingface.co/docs/transformers.js/index)
