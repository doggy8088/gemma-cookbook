# 歡迎來到 Gemma Cookbook
這是收錄 [Google Gemma](https://ai.google.dev/gemma/) 指南與範例的文件集合。

> **免責聲明：** Gemma 是由 Google DeepMind 建立、面向開發者的模型家族。這份 cookbook 收錄的是 Google Gemma 的指南與範例。請留意，Gemma 屬於開放模型，在你依照本 cookbook 的範例進行開發時，仍可能出現 hallucination。

## 開始使用 Gemma 模型
Gemma 是一個輕量級、生成式人工智慧（AI）的開放模型家族，建立於與 Gemini 模型相同的研究與技術基礎之上。Gemma 模型家族包含：
* Gemma\
  Gemma 模型家族的核心模型。
  * [Gemma](https://ai.google.dev/gemma/docs/core/model_card)\
    適用於各式文字生成任務，並可依特定使用情境進一步微調
  * [Gemma 2](https://ai.google.dev/gemma/docs/core/model_card_2)\
    效能更高、效率更佳，提供 2B、9B、27B 參數規模
  * [Gemma 3](https://ai.google.dev/gemma/docs/core/model_card_3)\
    具備更長的 context window，可處理文字與圖片輸入，提供 1B、4B、12B、27B 參數規模
  * [Gemma 3n](https://ai.google.dev/gemma/docs/gemma-3n/model_card) \
    專為低資源裝置上的高效率執行而設計，可處理文字、圖片、影片與音訊輸入，提供 E2B 與 E4B 參數規模
  * [Gemma 4](https://ai.google.dev/gemma/docs/core/model_card_4)\
    特別適合理解推理、agentic 工作流程、程式開發與多模態理解，提供 E2B、E4B、26B A4B 與 31B 參數規模
* Gemma 變體模型
  * [CodeGemma](https://ai.google.dev/gemma/docs/codegemma)\
    針對各式程式設計任務完成微調
  * [DataGemma](https://ai.google.dev/gemma/docs/datagemma)\
    透過 Data Commons 微調，以降低 AI hallucination 問題
  * [FunctionGemma](https://ai.google.dev/gemma/docs/functiongemma)\
    以 Gemma 3 270M IT checkpoint 為基礎，針對 function calling 完成微調
  * [MedGemma](https://developers.google.com/health-ai-developer-foundations/medgemma)
    MedGemma 集合是 Google 目前能力最強的醫療文字與影像理解開放模型，建立於 Gemma 3 之上。開發者可以利用 MedGemma 加速打造醫療保健 AI 應用。MedGemma 提供兩種變體：4B 多模態版本與 27B 純文字版本。
  * [PaliGemma](https://ai.google.dev/gemma/docs/paligemma/model-card)\
    視覺語言模型（VLM）\
    可更深入分析圖片並提供有用洞察
  * [PaliGemma 2](https://ai.google.dev/gemma/docs/paligemma/model-card-2)\
    結合 Gemma 2 模型能力的 VLM
  * [RecurrentGemma](https://ai.google.dev/gemma/docs/recurrentgemma)\
    基於 [Griffin](https://arxiv.org/abs/2402.19427) 架構\
    適用於各式文字生成任務
  * [ShieldGemma](https://ai.google.dev/gemma/docs/shieldgemma/model_card)\
    針對文字 prompt 輸入與文字輸出回應的安全性評估完成微調，依據已定義的安全政策進行判定
  * [ShieldGemma 2](https://ai.google.dev/gemma/docs/shieldgemma/model_card_2)\
    以 Gemma 3 4B IT checkpoint 為基礎，針對影像安全分類完成微調
  * [T5Gemma](https://deepmind.google/models/gemma/t5gemma)\
    一組 encoder-decoder 模型，在品質與推論效率之間提供優異權衡
  * [TranslateGemma](https://huggingface.co/collections/google/translategemma)\
    一組為 55 種語言翻譯任務設計的開放模型
  * [TxGemma](https://deepmind.google/models/gemma/txgemma)\
    一組為提升治療開發效率而設計的開放模型
  * [VaultGemma](https://deepmind.google/models/gemma/vaultgemma)\
    從頭以 differential privacy 訓練的開放模型，可避免記憶與洩漏訓練資料範例

你可以在 Hugging Face Hub、Kaggle、Google Cloud Vertex AI Model Garden，以及 [ai.nvidia.com](https://ai.nvidia.com) 找到 Gemma 模型。

## Notebook 目錄
* [Gemma](Gemma/README.md)
* [CodeGemma](CodeGemma/README.md)
* [FunctionGemma](FunctionGemma/README.md)
* [PaliGemma](PaliGemma/README.md)
* [MedGemma](MedGemma/README.md)
* [Google-Health 上的 MedGemma](https://github.com/Google-Health/medgemma/tree/main/notebooks) : Google-Health 另外提供使用 MedGemma 的 notebooks
* [TxGemma](TxGemma/README.md)
* [工作坊與技術演講](Workshops/README.md)
* [Research](Research/)：聚焦研究模型的 notebooks
* [複雜端到端使用案例展示](Demos/README.md)
* [Google Cloud 上的 Gemma](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/open-models) : GCP open models 另外提供使用 Gemma 的 notebooks

## 取得協助
如果你有 Gemma Cookbook 相關問題，歡迎到 [developer forum](https://discuss.ai.google.dev/c/gemma/10) 提問，或在 GitHub 開啟 [issue](https://github.com/google-gemini/gemma-cookbook/issues)。

## Wish List
如果你想看到針對特定功能或整合情境的更多 cookbook，請使用 [“Feature Request” template](https://github.com/google-gemini/gemma-cookbook/issues/new?template=feature_request.yml) 開啟新 issue。

如果你想為 Gemma Cookbook 專案做出貢獻，歡迎從 [“Wish List”](https://github.com/google-gemini/gemma-cookbook/labels/wishlist) 挑選任何想法並加以實作。

## 貢獻
歡迎任何貢獻。開始實作前，請先閱讀 [contributing](https://github.com/google-gemini/gemma-cookbook/blob/main/CONTRIBUTING.md)。

感謝你使用 Gemma 進行開發，我們很期待看到你的成果。
