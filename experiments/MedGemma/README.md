# MedGemma

MedGemma 系列包含 Google 最強大的醫學文字和圖像理解開放模型，建構於 Gemma 3 之上。開發人員可以使用 MedGemma 加速建立基於醫療保健的 AI 應用程式。 MedGemma 有兩種變體：4B 多模式版本和 27B 純文字版本。

該資料夾分為幾個類別，每個類別都專注於使用 MedGemma 模型的特定方面：
* [推論](#inference) : 如何載入與執行inference的MedGemma模型

## 推論

| notebook 名稱 | 描述 |:-------------- | ----------- |
| [[MedGemma]Inference_using_HuggingFace.ipynb]([MedGemma]Inference_using_HuggingFace.ipynb) | 一個簡單的人工智慧工具，可以檢查胸部 X 光影像，根據可見的肺部模式和體徵，使用 MedGemma 來預測該人是否可能是吸煙者或非吸煙者 |