# 表情符號生成器網頁應用程式
該演示執行一個 [Gemma 3 270M IT](https://huggingface.co/google/gemma-3-270m-it) 模型，該模型經過微調，可直接在瀏覽器中進行文字到表情符號的翻譯。 Gemma 3 由 Web AI frameworks 支持，使部署變得容易。使用以下任一方式執行應用程式：
* **[MediaPipe LLM Inference API](./app-mediapipe)** - 需要 `.task` 捆綁包中的 LiteRT 模型
* **[Transformers.js](./app-transformersjs)** - 需要 `.onnx` 型號

如果您沒有微調模型，請查看下面的資源。
![Alt text](./emoji-generator-web-app.gif)

在 [Hugging Face](https://goo.gle/emoji-gemma-demo) 上預覽應用程式。
## 資源

您可以將 Google Colab 中的這些 notebook 用於 fine-tuning 並針對網路最佳化 Gemma 3 270M。要微調表情符號翻譯任務的模型，您可以建立自己的dataset或使用我們的[預製dataset](./resources/Emoji%20Translation%20Dataset%20-%20Dataset.csv)。
| notebook | 描述 || ------------- |-------------|
| [微調Gemma 3 270M](./resources/Fine_tune_Gemma_3_270M_for_emoji_generation.ipynb) | 使用量化低階適應微調 Gemma 以進行表情符號翻譯 (QLoRA) || [轉換為MediaPipe](./resources/Convert_Gemma_3_270M_to_LiteRT_for_MediaPipe_LLM_Inference_API.ipynb) | 將經過微調的 Gemma 3 270M 模型量化並轉換為 `.litert`，然後捆綁到 `.task` 文件中以與 LLM 推論 API 一起使用 || [轉換為 ONNX](./resources/Convert_Gemma_3_270M_to_ONNX.ipynb) | 將經過微調的Gemma 3 270M 模型量化並轉換為`.onnx`，以便透過ONNX Runtime 與Transformers.js 一起使用 |