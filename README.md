# 歡迎來到 Gemma Cookbook

這是一系列關於 [Google Gemma](https://ai.google.dev/gemma/) 的指南和範例。

## 開始使用 Gemma 模型

Gemma 是一個輕量級、最先進的開放模型系列，使用與建構 Gemini 模型相同的研究和技術。Gemma 模型系列包括:

* [base Gemma](https://ai.google.dev/gemma/docs/model_card)
* [程式碼 Gemma](https://ai.google.dev/gemma/docs/codegemma)
* [Pali Gemma](https://ai.google.dev/gemma/docs/paligemma)
* [Recurrent Gemma](https://ai.google.dev/gemma/docs/recurrentgemma)

你可以在 GitHub、Hugging Face 模型、Kaggle、Google Cloud Vertex AI Model Garden 和 [ai.nvidia.com](ai.nvidia.com) 找到 Gemma 模型。

## 目錄

 Name                                                                                                           | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemma**                                                                                                      |
| [Gemma_Basics_with_HF.ipynb](Gemma/Gemma_Basics_with_HF.ipynb)                                                 | 使用 [Hugging Face](https://huggingface.co/) 載入、執行、微調和部署 Gemma。                                                                      |
| [Guess_the_word.ipynb](Gemma/Guess_the_word.ipynb)                                                             | 使用 Keras 與 Gemma 玩猜字遊戲。                                                                                                        |
| [Game_Design_Brainstorming.ipynb](Gemma/Game_Design_Brainstorming.ipynb)                                       | 使用 Keras 與 Gemma 在遊戲設計過程中進行頭腦風暴。                                                                                            |
| [Translator_of_Old_Korean_Literature.ipynb](Gemma/Translator_of_Old_Korean_Literature.ipynb)                   | 使用 Keras 與 Gemma 翻譯古代韓國文學。                                                                                                |
| [Run_with_Ollama.ipynb](Gemma/Run_with_Ollama.ipynb)                                                           | 使用 [Ollama](https://www.ollama.com/) 執行 Gemma 模型。                                                                                                |
| [Deploy_with_vLLM.ipynb](Gemma/Deploy_with_vLLM.ipynb)                                                         | 使用 [vLLM](https://github.com/vllm-project/vllm) 部署 Gemma 模型。                                                                                 |
| [RAG_with_ChromaDB.ipynb](Gemma/RAG_with_ChromaDB.ipynb)                                                       | 使用 [ChromaDB](https://www.trychroma.com/) 和 [Hugging Face](https://huggingface.co/) 與 Gemma 建構檢索增強生成（RAG）系統。 |
| [Minimal_RAG.ipynb](Gemma/Minimal_RAG.ipynb)                                                                   | 使用 [Google UniSim](https://github.com/google/unisim) 和 [Hugging Face](https://huggingface.co/) 與 Gemma 建構 RAG 系統的最小範例。 |
| [Integrate_with_Mesop.ipynb](Gemma/Integrate_with_Mesop.ipynb)                                                 | 與 [Google Mesop](https://google.github.io/mesop/) 整合 Gemma。                                                                                    |
| [Integrate_with_OneTwo.ipynb](Gemma/Integrate_with_OneTwo.ipynb)                                               | 與 [Google OneTwo](https://github.com/google-deepmind/onetwo) 整合 Gemma。                                                                         |
| [Finetune_with_Axolotl.ipynb](Gemma/Finetune_with_Axolotl.ipynb)                                               | 使用 [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) 微調 Gemma。                                                                     |
| [Finetune_with_XTuner.ipynb](Gemma/Finetune_with_XTuner.ipynb)                                                 | 使用 [XTuner](https://github.com/InternLM/xtuner) 微調 Gemma。                                                                                       |
| [Finetune_with_LLaMA_Factory.ipynb](Gemma/Finetune_with_LLaMA_Factory.ipynb)                                   | 使用 [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) 微調 Gemma。                                                                          |
| **PaliGemma**                                                                                                  |
| [Image_captioning_using_PaliGemma.ipynb](PaliGemma/Image_captioning_using_PaliGemma.ipynb)                     | 使用 Keras 與 PaliGemma 生成圖像標題。                                                                                                    |
| [Image_captioning_using_finetuned_PaliGemma.ipynb](PaliGemma/Image_captioning_using_finetuned_PaliGemma.ipynb) | 使用 [Hugging Face](https://huggingface.co/) 比較不同版本 PaliGemma 的圖像標題結果。                                    |
| [Finetune_PaliGemma_for_image_description.ipynb](PaliGemma/Finetune_PaliGemma_for_image_description.ipynb)     | 使用 [JAX](https://github.com/google/jax) 微調 PaliGemma 以進行圖像描述。

## WIP 筆記本

| 描述                   |
| ---------------------- |
| Langchain 整合         |
| LlamaIndex 整合        |
| 常見使用案例           |
| 提示鏈接               |
| 高級提示               |

## 獲取幫助

在新的 [Build with Google AI Forum](https://discuss.ai.google.dev/) 上詢問有關 Gemma Cookbook 的問題，或在 GitHub 上開一個 [issue](https://github.com/google-gemini/gemma-cookbook/issues)。

## 願望清單

如果你想看到為特定功能/整合實現的額外秘訣，請通過在[願望清單](https://github.com/google-gemini/gemma-cookbook/blob/main/WISHLIST.md)中添加你的功能請求來向我們發送 pull request。

如果你想對 Gemma Cookbook 專案做出貢獻，歡迎挑選[願望清單](https://github.com/google-gemini/gemma-cookbook/blob/main/WISHLIST.md)中的任何想法並實現它。

## 貢獻

貢獻永遠是受歡迎的。請在實作之前閱讀[貢獻](https://github.com/google-gemini/gemma-cookbook/blob/main/CONTRIBUTING.md)。

感謝您使用 Gemma 開發！我們很期待看到您建立的內容。

