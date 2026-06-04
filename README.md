
# 歡迎來到Gemma Cookbook
這是 [Google Gemma](https://ai.google.dev/gemma/) 指南和範例的集合。
> **免責聲明：** Gemma 是由 Google DeepMind 建構的一系列以開發人員為中心的模型。這本食譜是 Google Gemma 的指南和範例的集合。請記住，Gemma 是一個開放模型，當您基於本食譜中的範例進行構建時，可能會產生幻覺。

## 儲存庫結構
* [**教學**](tutorials/)：Gemma 型號和變體的最新測試notebook。
* [**應用**](apps/)：全端演示和複雜的端對端用例。
* [**實驗**](experiments/)：以研究為重點的模型notebooks，包括[TxGemma](experiments/TxGemma)和[MedGemma](experiments/MedGemma)。
* [**Responsible**](responsible/)：用於負責任的人工智慧開發的 notebook。
* [**文件**](docs/)：核心文件、功能與技術指南。
* [**檔案**](.archive/)：所有較舊的notebook和歷史範例。

## 開始使用 Gemma 模型
Gemma 是一系列輕量級生成人工智慧 (AI) 開放模型，採用與創建 Gemini 模型相同的研究和技術構建。 Gemma 型號系列包括：* Gemma\
Gemma 系列的核心型號。  * [Gemma](https://ai.google.dev/gemma/docs/core/model_card)\
    For a variety of text generation tasks and can be further tuned for specific use cases
  * [Gemma 2](https://ai.google.dev/gemma/docs/core/model_card_2)\
    Higher-performing and more efficient, available in 2B, 9B, 27B parameter sizes
  * [Gemma 3](https://ai.google.dev/gemma/docs/core/model_card_3)\
    Longer context window and handling text and image input, available in 1B, 4B, 12B, and 27B parameter sizes
  * [Gemma 3n](https://ai.google.dev/gemma/docs/gemma-3n/model_card) \
    Designed for efficient execution on low-resource devices. Handling text, image, video, and audio input, available in E2B and E4B parameter sizes
  * [Gemma 4](https://ai.google.dev/gemma/docs/core/model_card_4)\
    Well-suited for reasoning, agentic workflows, coding, and multimodal understanding, available in E2B, E4B, 26B A4B, and 31B parameter sizes.
* Gemma 變體
  * [CodeGemma](https://ai.google.dev/gemma/docs/codegemma)\
    Fine-tuned for a variety of coding tasks
  * [數據Gemma](https://ai.google.dev/gemma/docs/datagemma)\
    Fine-tuned for using Data Commons to address AI hallucinations
  * [FunctionGemma](https://ai.google.dev/gemma/docs/functiongemma)\
    Fine-tuned on Gemma 3 270M IT checkpoint for function calling
  * [MedGemma](https://developers.google.com/health-ai-developer-foundations/medgemma)
    The MedGemma collection contains Google's most capable open models for medical text and image comprehension, built on Gemma 3. Developers can use MedGemma to accelerate building healthcare-based AI applications. MedGemma comes in two variants: a 4B multimodal version and a 27B text-only version.
  * [PaliGemma](https://ai.google.dev/gemma/docs/paligemma/model-card)\
    Vision Language Model\
    For a deeper analysis of images and provide useful insights
  * [PaliGemma 2](https://ai.google.dev/gemma/docs/paligemma/model-card-2)\
    VLM which incorporates the capabilities of the Gemma 2 models
  * [經常Gemma](https://ai.google.dev/gemma/docs/recurrentgemma)\
    Based on [Griffin](https://arxiv.org/abs/2402.19427) architecture\
    For a variety of text generation tasks
  * [屏蔽Gemma](https://ai.google.dev/gemma/docs/shieldgemma/model_card)\
    Fine-tuned for evaluating the safety of text prompt input and text output responses against a set of defined safety policies
  * [屏蔽Gemma 2](https://ai.google.dev/gemma/docs/shieldgemma/model_card_2)\
    Fine-tuned on Gemma 3 4B IT checkpoint for image safety classification
  * [T5Gemma](https://deepmind.google/models/gemma/t5gemma)\
    A collection of encoder-decoder models that provide a strong quality-inference efficiency tradeoff
  * [翻譯Gemma](https://huggingface.co/collections/google/translategemma)\
    A collection of open model designed to handle translation tasks across 55 languages
  * [TxGemma](https://deepmind.google/models/gemma/txgemma)\
    A collection of open models designed to improve the efficiency of therapeutic development
  * [金庫Gemma](https://deepmind.google/models/gemma/vaultgemma)\
    An open model trained from the ground up using differential privacy to prevent memorization and leaking of training data examples

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
## 該存儲庫的翻譯
* [繁體中文](https://github.com/doggy8088/gemma-cookbook)
* [Simplified Chinese](https://github.com/xiaoxiong1006/gemma-cookbook)
