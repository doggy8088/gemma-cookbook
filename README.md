
# 歡迎來到Gemma Cookbook
這是 [Google Gemma](https://ai.google.dev/gemma/) 指南和範例的集合。
> **免責聲明：** Gemma 是由 Google DeepMind 建構的一系列以開發人員為中心的模型。這本食譜是 Google Gemma 的指南和範例的集合。請記住，Gemma 是一個開放模型，當您基於本食譜中的範例進行構建時，可能會產生幻覺。

## 儲存庫結構
* [**教學**](tutorials/)：Gemma 模型和變體的最新測試 notebook。
* [**應用**](apps/)：全端演示和複雜的端對端用例。
* [**實驗**](experiments/)：以研究為主的模型 notebooks，包括 [TxGemma](experiments/TxGemma) 和 [MedGemma](experiments/MedGemma)。
* [**負責任的 AI**](responsible/)：用於負責任人工智慧開發的 notebook。
* [**文件**](docs/)：核心文件、功能與技術指南。
* [**檔案**](.archive/)：所有較舊的notebook和歷史範例。

## 開始使用 Gemma 模型
Gemma 是一系列輕量級生成式人工智慧 (AI) 開放模型，採用與建立 Gemini 模型相同的研究和技術構建。Gemma 模型家族包括：
* Gemma\
  Gemma 家族的核心模型。
  * [Gemma](https://ai.google.dev/gemma/docs/core/model_card)\
    適用於各種文字生成任務，並可針對特定使用場景進行進一步微調
  * [Gemma 2](https://ai.google.dev/gemma/docs/core/model_card_2)\
    效能更高、效率更佳，提供 2B、9B、27B 參數大小
  * [Gemma 3](https://ai.google.dev/gemma/docs/core/model_card_3)\
    更長的 context window，且支援文字與影像輸入，提供 1B、4B、12B 與 27B 參數大小
  * [Gemma 3n](https://ai.google.dev/gemma/docs/gemma-3n/model_card) \
    專為低資源裝置上的高效執行而設計。支援文字、影像、影片和音訊輸入，提供 E2B 與 E4B 參數大小
  * [Gemma 4](https://ai.google.dev/gemma/docs/core/model_card_4)\
    非常適合推理、agentic 工作流、程式碼撰寫和多模態理解，提供 E2B、E4B、26B A4B 與 31B 參數大小。
* Gemma 變體
  * [CodeGemma](https://ai.google.dev/gemma/docs/codegemma)\
    專為各種程式碼撰寫任務進行微調
  * [DataGemma](https://ai.google.dev/gemma/docs/datagemma)\
    專為使用 Data Commons 來解決 AI 幻覺問題進行微調
  * [FunctionGemma](https://ai.google.dev/gemma/docs/functiongemma)\
    在 Gemma 3 270M IT checkpoint 上進行微調，適用於 function calling
  * [MedGemma](https://developers.google.com/health-ai-developer-foundations/medgemma)
    MedGemma 系列包含 Google 最頂尖的醫療文字與影像理解開放模型，基於 Gemma 3 構建。開發者可以使用 MedGemma 來加速構建醫療領域的 AI 應用。MedGemma 提供兩種版本：4B 多模態版本與 27B 僅限文字版本。
  * [PaliGemma](https://ai.google.dev/gemma/docs/paligemma/model-card)\
    視覺語言模型 (VLM)\
    用於對影像進行更深層的分析並提供實用的洞察
  * [PaliGemma 2](https://ai.google.dev/gemma/docs/paligemma/model-card-2)\
    結合了 Gemma 2 模型功能的視覺語言模型 (VLM)
  * [RecurrentGemma](https://ai.google.dev/gemma/docs/recurrentgemma)\
    基於 [Griffin](https://arxiv.org/abs/2402.19427) 架構\
    適用於各種文字生成任務
  * [ShieldGemma](https://ai.google.dev/gemma/docs/shieldgemma/model_card)\
    專為評估文字 prompt 輸入與文字輸出回應是否符合一組定義的安全政策而進行微調
  * [ShieldGemma 2](https://ai.google.dev/gemma/docs/shieldgemma/model_card_2)\
    在 Gemma 3 4B IT checkpoint 上進行微調，適用於影像安全分類
  * [T5Gemma](https://deepmind.google/models/gemma/t5gemma)\
    一系列編碼器-解碼器模型，在品質與推論效率之間取得了絕佳的權衡
  * [TranslateGemma](https://huggingface.co/collections/google/translategemma)\
    一系列專為處理 55 種語言之間的翻譯任務而設計的開放模型
  * [TxGemma](https://deepmind.google/models/gemma/txgemma)\
    一系列專為提高療效開發效率而設計的開放模型
  * [VaultGemma](https://deepmind.google/models/gemma/vaultgemma)\
    一個從頭開始使用差異隱私（differential privacy）進行訓練的開放模型，以防止記憶和洩漏訓練資料範例

您可以在 Hugging Face Hub、Kaggle、Google Cloud Vertex AI Model Garden 和 [ai.nvidia.com](https://ai.nvidia.com) 上找到 Gemma 型號。
## 其他資源
* [MedGemma Google-Health](https://github.com/Google-Health/medgemma/tree/main/notebooks) ：Google-Health 有額外的 notebook 用於使用 MedGemma
* [Gemma on Google Cloud](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/open-models) ：GCP 開放模式有額外的 notebook 用於使用 Gemma

## 獲得協助
在[開發者論壇](https://discuss.ai.google.dev/c/gemma/10) 上提出Gemma 食譜相關問題，或在GitHub 上開啟[問題](https://github.com/google-gemini/gemma-cookbook/issues)。
## 願望清單
如果您想查看針對特定功能/整合實作的其他食譜，請使用 [「功能請求」範本](https://github.com/google-gemini/gemma-cookbook/issues/new?template=feature_request.yml) 開啟新問題。
如果您想為Gemma Cookbook專案做出貢獻，歡迎您在[「願望清單」](https://github.com/google-gemini/gemma-cookbook/labels/wishlist)中選擇任何想法並實施它。
## 貢獻
隨時歡迎您的貢獻。請在實施前閱讀[貢獻](https://github.com/google-gemini/gemma-cookbook/blob/main/CONTRIBUTING.md)。
感謝您與Gemma一起開發！我們很高興看到您的創造。
## 本儲存庫翻譯版本
* [繁體中文](https://github.com/doggy8088/gemma-cookbook)
* [簡體中文](https://github.com/xiaoxiong1006/gemma-cookbook)
