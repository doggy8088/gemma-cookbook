# MedGemma

MedGemma 集合是 Google 目前能力最強的醫療文字與影像理解開放模型，建立於 Gemma 3 之上。開發者可以利用 MedGemma 加速打造醫療保健 AI 應用。MedGemma 提供兩種變體：4B 多模態版本與 27B 純文字版本。

這個資料夾依照主題分成數個分類，每一類都聚焦於使用 MedGemma 模型的特定面向：

* [推論](#推論) : 如何載入並執行 MedGemma 模型以進行推論

## 推論

| Notebook Name | Description |
:-------------- | ----------- |
| [[MedGemma]Inference_using_HuggingFace.ipynb]([MedGemma]Inference_using_HuggingFace.ipynb) | 一個簡單的 AI 工具，利用 MedGemma 根據可見的肺部紋理與徵象分析胸部 X 光影像，預測受測者較可能為吸菸者或非吸菸者 |
