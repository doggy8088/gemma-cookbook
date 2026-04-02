# Gemma

這個資料夾依照主題分成數個分類，每一類都聚焦於使用 Gemma 模型的特定面向：

* [推論與服務部署](#推論與服務部署) : 如何載入、執行與部署 Gemma 模型以進行推論
* [提示設計](#提示設計) : 探索各種 prompt 使用技巧
* [RAG（Retrieval Augmented Generation）](#ragretrieval-augmented-generation) : 如何使用 Gemma 建立 RAG 系統
* [微調](#微調) : 深入了解如何針對特定任務與領域微調 Gemma 模型
* [對齊](#對齊) : Gemma 模型的對齊技巧
* [評估](#評估) : 如何評估 Gemma 模型
* [Agentic AI](#agentic-ai) : 如何使用 Gemma 模型打造智慧代理

## 推論與服務部署

| Notebook Name | Description |
:------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[Gemma_1]Basics_with_HF.ipynb]([Gemma_1]Basics_with_HF.ipynb) | 使用 [Hugging Face](https://huggingface.co/) 載入、執行、微調與部署 Gemma。 |
| [[Gemma_1]Common_use_cases.ipynb]([Gemma_1]Common_use_cases.ipynb) | 說明 Gemma 的一些常見使用案例。 |
| [[Gemma_1]Inference with Flax/NNX](https://flax.readthedocs.io/en/latest/guides/gemma.html) | 使用 Flax/NNX framework 對 Gemma 1 進行推論（連到 Flax 文件）。 |
| [[Gemma_1]Inference_on_TPU.ipynb]([Gemma_1]Inference_on_TPU.ipynb) | 使用 JAX/Flax 在 TPU 上對 Gemma 進行基本推論。 |
| [[Gemma_1]Using_with_Ollama.ipynb]([Gemma_1]Using_with_Ollama.ipynb) | 使用 [Ollama](https://www.ollama.com/) 執行 Gemma 模型。 |
| [[Gemma_1]Using_with_OneTwo.ipynb]([Gemma_1]Using_with_OneTwo.ipynb) | 將 Gemma 與 [Google OneTwo](https://github.com/google-deepmind/onetwo) 整合。 |
| [[Gemma_1]data_parallel_inference_in_jax_tpu.ipynb]([Gemma_1]data_parallel_inference_in_jax_tpu.ipynb) | 使用 JAX/Flax 在 TPU 上進行 Gemma 的平行推論。 |
| [[Gemma_2]Constrained_generation.ipynb]([Gemma_2]Constrained_generation.ipynb) | 使用 [LlamaCpp](https://github.com/abetlen/llama-cpp-python/) 與 [Guidance](https://github.com/guidance-ai/guidance/tree/main/) 對 Gemma 模型進行 constrained generation。 |
| [[Gemma_2]DeFi_Protocol_Development.ipynb]([Gemma_2]DeFi_Protocol_Development.ipynb) | 使用 Gemma 2 探索 DeFi protocol 開發（ERC-20 tokens、AMM mechanics、staking patterns）。 |
| [[Gemma_2]Deploy_in_Vertex_AI.ipynb]([Gemma_2]Deploy_in_Vertex_AI.ipynb) | 使用 [Vertex AI](https://cloud.google.com/vertex-ai) 部署 Gemma 模型。 |
| [[Gemma_2]Deploy_with_vLLM.ipynb]([Gemma_2]Deploy_with_vLLM.ipynb) | 使用 [vLLM](https://github.com/vllm-project/vllm) 部署 Gemma 模型。 |
| [[Gemma_2]Game_Design_Brainstorming.ipynb]([Gemma_2]Game_Design_Brainstorming.ipynb) | 在遊戲設計過程中使用 Keras 與 Gemma 進行點子發想。 |
| [[Gemma_2]Gradio_Chatbot.ipynb]([Gemma_2]Gradio_Chatbot.ipynb) | 使用 Gemma 與 Gradio 建立 chatbot。 |
| [[Gemma_2]Guess_the_word.ipynb]([Gemma_2]Guess_the_word.ipynb) | 使用 Keras 與 Gemma 玩猜單字遊戲。 |
| [[Gemma_2]Keras_Quickstart.ipynb]([Gemma_2]Keras_Quickstart.ipynb) | 使用 Keras 的 Gemma 2 預訓練 9B 模型快速開始教學。 |
| [[Gemma_2]Keras_Quickstart_Chat.ipynb]([Gemma_2]Keras_Quickstart_Chat.ipynb) | 使用 Keras 的 Gemma 2 instruction-tuned 9B 模型快速開始教學。本文也在這篇 [blog](https://developers.googleblog.com/en/fine-tuning-gemma-2-with-keras-hugging-face-update/) 中被引用。 |
| [[Gemma_2]Smart_Contract_Auditing.ipynb]([Gemma_2]Smart_Contract_Auditing.ipynb) | 使用 Gemma 2 稽核並重構 Solidity smart contracts。 |
| [[Gemma_2]Synthetic_data_generation.ipynb]([Gemma_2]Synthetic_data_generation.ipynb) | 使用 Gemma 2 進行 synthetic data generation |
| [[Gemma_2]Using_Gemini_and_Gemma_with_RouteLLM.ipynb]([Gemma_2]Using_Gemini_and_Gemma_with_RouteLLM.ipynb) | 使用 [RouteLLM](https://github.com/lm-sys/RouteLLM/) 路由 Gemma 與 Gemini 模型。 |
| [[Gemma_2]Using_with_LLM_Comparator.ipynb](Gemma/[Gemma_2]Using_with_LLM_Comparator.ipynb) | 使用 [LLM Comparator](https://github.com/pair-code/llm-comparator/) 比較 Gemma 與其他 LLM。 |
| [[Gemma_2]Using_with_Langfun_and_LlamaCpp.ipynb]([Gemma_2]Using_with_Langfun_and_LlamaCpp.ipynb) | 使用 [Langfun](https://github.com/google/langfun) 將自然語言與程式設計流暢整合，並搭配 Gemma 2 與 [LlamaCpp](https://github.com/ggerganov/llama.cpp)。 |
| [[Gemma_2]Using_with_Langfun_and_LlamaCpp_Python_Bindings.ipynb]([Gemma_2]Using_with_Langfun_and_LlamaCpp_Python_Bindings.ipynb) | 使用 [Langfun](https://github.com/google/langfun) 結合 Gemma 2 與 [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)，打造順暢的語言與程式互動。 |
| [[Gemma_2]Using_with_LlamaCpp.ipynb]([Gemma_2]Using_with_LlamaCpp.ipynb) | 使用 [LlamaCpp](https://github.com/abetlen/llama-cpp-python/) 執行 Gemma 模型。 |
| [[Gemma_2]Using_with_Llamafile.ipynb]([Gemma_2]Using_with_Llamafile.ipynb) | 使用 [Llamafile](https://github.com/Mozilla-Ocho/llamafile/) 執行 Gemma 模型。 |
| [[Gemma_2]Using_with_LocalGemma.ipynb]([Gemma_2]Using_with_LocalGemma.ipynb) | 使用 [Local Gemma](https://github.com/huggingface/local-gemma/) 執行 Gemma 模型。 |
| [[Gemma_2]Using_with_Mesop.ipynb]([Gemma_2]Using_with_Mesop.ipynb) | 將 Gemma 與 [Google Mesop](https://google.github.io/mesop/) 整合。 |
| [[Gemma_2]Using_with_Ollama_Python.ipynb]([Gemma_2]Using_with_Ollama_Python.ipynb) | 使用 [Ollama Python library](https://github.com/ollama/ollama-python) 執行 Gemma 模型。 |
| [[Gemma_2]Using_with_SGLang.ipynb]([Gemma_2]Using_with_SGLang.ipynb) | 使用 [SGLang](https://github.com/sgl-project/sglang/) 執行 Gemma 模型。 |
| [[Gemma_2]Using_with_Xinference.ipynb]([Gemma_2]Using_with_Xinference.ipynb) | 使用 [Xinference](https://github.com/xorbitsai/inference/) 執行 Gemma 模型。 |
| [[Gemma_2]Using_with_mistral_rs.ipynb]([Gemma_2]Using_with_mistral_rs.ipynb) | 使用 [mistral.rs](https://github.com/EricLBuehler/mistral.rs/) 執行 Gemma 模型。 |
| [[Gemma_2]for_Japan_using_Transformers_and_PyTorch.ipynb]([Gemma_2]for_Japan_using_Transformers_and_PyTorch.ipynb) | [Gemma 2 for Japan](https://blog.google/intl/ja-jp/company-news/technology/gemma-2-2b/) |
| [[Gemma_2]on_Groq.ipynb]([Gemma_2]on_Groq.ipynb) | 使用由 [Groq](https://groq.com/) 託管的免費 Gemma 2 9B IT 模型（速度非常快）。 |
| [[Gemma_3]Inference_images_and_videos.ipynb]([Gemma_3]Inference_images_and_videos.ipynb) | 使用 Gemma 3 4B IT 模型對圖片與影片進行推論。 |
| [[Gemma_3]Using_with_Ollama_Python_Inference_with_Images.ipynb]([Gemma_3]Using_with_Ollama_Python_Inference_with_Images.ipynb) | 使用 [Ollama Python library](https://github.com/ollama/ollama-python) 對 Gemma 3 進行圖片推論。 |
| [[Gemma_3]Using_with_Transformersjs.ipynb]([Gemma_3]Using_with_Transformersjs.ipynb) | 使用 [Transformers.js](https://github.com/huggingface/transformers.js) 執行 Gemma 3。 |
| [[Gemma_3]Activation_Hacking.ipynb]([Gemma_3]Activation_Hacking.ipynb) | 檢查並修改內部狀態，包括 residual stream、MLP activations 與 attention mechanisms。 |
| [[Gemma_3]Chess.ipynb]([Gemma_3]Chess.ipynb) | Gemma \| Chess：學習、分析並探索全新維度。 |
| [[Gemma_3]Gradio_LlamaCpp_Chatbot.ipynb]([Gemma_3]Gradio_LlamaCpp_Chatbot.ipynb) | 使用 Llama.cpp 與 Gradio，以 Gemma 3 QAT text model 建立 chatbot。 |
| [[Gemma_3]Speculative_Decoding.ipynb]([Gemma_3]Speculative_Decoding.ipynb) | 使用 speculative decoding 讓 Gemma 模型推論速度提升 2 到 3 倍。 |
| [[Gemma_3]Visual_Document_Extraction_to_JSON.ipynb]([Gemma_3]Visual_Document_Extraction_to_JSON.ipynb) | 使用原生多模態的 Gemma 3 4B-IT 模型，示範從圖片進行 zero-shot OCR 與結構化 JSON 資料擷取。 |
| [[Gemma_3n]Audio_understanding_with_HF.ipynb]([Gemma_3n]Audio_understanding_with_HF.ipynb) | 使用音訊輸入執行 Gemma 3n |
| [[Gemma_3n]Multimodal_understanding_with_HF.ipynb]([Gemma_3n]Multimodal_understanding_with_HF.ipynb) | 使用圖片與音訊輸入執行 Gemma 3n |
| [[Gemma_3n]MatFormer_Lab.ipynb]([Gemma_3n]MatFormer_Lab.ipynb) | 使用 MatFormers 與 Mix-n-Match 執行 Gemma 3n |
| [[Gemma_3n]Using_with_Transformersjs.ipynb]([Gemma_3n]Using_with_Transformersjs.ipynb) | 使用 [Transformers.js](https://github.com/huggingface/transformers.js) 執行 Gemma 3n。 |

## 提示設計
| Notebook Name | Description |
| :------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[Gemma_1]Advanced_Prompting_Techniques.ipynb]([Gemma_1]Advanced_Prompting_Techniques.ipynb) | 說明 Gemma 的進階 prompt 技巧。 |
| [[Gemma_2]LangChain_chaining.ipynb]([Gemma_2]LangChain_chaining.ipynb) | 說明如何搭配 Gemma 使用 LangChain chaining。 |
| [[Gemma_2]Prompt_chaining.ipynb]([Gemma_2]Prompt_chaining.ipynb) | 說明如何使用 Gemma 進行 prompt chaining 與迭代式生成。 |
| [[Gemma_3]In-context_Learning.ipynb]([Gemma_3]In-context_Learning.ipynb) | 示範如何利用 Gemma 3 的長 context window 進行 in-context learning |

## RAG（Retrieval Augmented Generation）
| Notebook Name | Description |
| :------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[Gemma_1]Minimal_RAG.ipynb]([Gemma_1]Minimal_RAG.ipynb) | 使用 [Google UniSim](https://github.com/google/unisim) 與 [Hugging Face](https://huggingface.co/) 建立 Gemma RAG 系統的最小範例。 |
| [[Gemma_1]RAG_with_ChromaDB.ipynb]([Gemma_1]RAG_with_ChromaDB.ipynb) | 使用 [ChromaDB](https://www.trychroma.com/) 與 [Hugging Face](https://huggingface.co/) 建立 Gemma 的 Retrieval Augmented Generation（RAG）系統。 |
| [[Gemma_2]RAG_LlamaIndex.ipynb]([Gemma_2]RAG_LlamaIndex.ipynb) | 使用 Gemma 與 [LlamaIndex](https://www.llamaindex.ai/) 的 RAG 範例。 |
| [[Gemma_2]RAG_PDF_Search_in_multiple_documents_on_Colab.ipynb]([Gemma_2]RAG_PDF_Search_in_multiple_documents_on_Colab.ipynb) | 在 Google Colab 上使用 Gemma 2 2B，於多份文件中進行 RAG PDF 搜尋。 |
| [[Gemma_2]Using_with_Elasticsearch_and_LangChain.ipynb]([Gemma_2]Using_with_Elasticsearch_and_LangChain.ipynb) | 示範如何搭配 [Elasticsearch](https://www.elastic.co/elasticsearch/)、[Ollama](https://www.ollama.com/) 與 [LangChain](https://www.langchain.com/) 使用 Gemma。 |
| [[Gemma_2]Using_with_Firebase_Genkit_and_Ollama.ipynb]([Gemma_2]Using_with_Firebase_Genkit_and_Ollama.ipynb) | 示範如何搭配 [Firebase Genkit](https://firebase.google.com/docs/genkit/) 與 [Ollama](https://www.ollama.com/) 使用 Gemma |
| [[Gemma_2]Using_with_LangChain.ipynb]([Gemma_2]Using_with_LangChain.ipynb) | 示範如何搭配 [LangChain](https://www.langchain.com/) 使用 Gemma。 |
| [[Gemma_3]Local_Agentic_RAG.ipynb]([Gemma_3]Local_Agentic_RAG.ipynb) | 使用 [FastEmbed](https://github.com/qdrant/fastembed)、[Ollama- Gemma3](https://ollama.com/models) 與 [Qdrant Vector database](https://cloud.qdrant.io)，在完全不依賴外部 APIs 的情況下建立本地 Agentic RAG |
| [[Gemma_3]RAG_with_EmbeddingGemma.ipynb]([Gemma_3]RAG_with_EmbeddingGemma.ipynb) | 使用 [EmbeddingGemma](https://ai.google.dev/gemma/docs/embeddinggemma) 建立簡單 RAG |

## 微調
| Notebook Name | Description |
|:-----------------------------------------------------------------------------------------------------------------------------------| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[Gemma_1]Finetune_distributed.ipynb]([Gemma_1]Finetune_distributed.ipynb) | 與 Gemma 7B 對話，並將其微調成會以海盜語氣回覆。 |
| [[Gemma_1]Finetune_with_LLaMA_Factory.ipynb]([Gemma_1]Finetune_with_LLaMA_Factory.ipynb) | 使用 [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) 微調 Gemma。 |
| [[Gemma_1]Finetune_with_XTuner.ipynb]([Gemma_1]Finetune_with_XTuner.ipynb) | 使用 [XTuner](https://github.com/InternLM/xtuner) 微調 Gemma。 |
| [[Gemma_2]Custom_Vocabulary.ipynb]([Gemma_2]Custom_Vocabulary.ipynb) | 示範如何在 Gemma 中使用自訂詞彙 `&lt;unused[0-98]&gt;` tokens。 |
| [[Gemma_2]Finetune_with_Axolotl.ipynb]([Gemma_2]Finetune_with_Axolotl.ipynb) | 使用 [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) 微調 Gemma。 |
| [[Gemma_2]Finetune_with_CALM.ipynb]([Gemma_2]Finetune_with_CALM.ipynb) | 使用 [CALM](https://github.com/google-deepmind/calm) 微調 Gemma。 |
| [[Gemma_2]Finetune_with_Function_Calling.ipynb]([Gemma_2]Finetune_with_Function_Calling.ipynb) | 使用 [PyTorch/XLA](https://github.com/pytorch/xla) 為 function calling 微調 Gemma。 |
| [[Gemma_2]Finetune_with_JORA.ipynb]([Gemma_2]Finetune_with_JORA.ipynb) | 使用 [JORA](https://github.com/aniquetahir/JORA) 微調 Gemma。 |
| [[Gemma_2]Finetune_with_LORA.ipynb]([Gemma_2]Finetune_with_LORA.ipynb) | 使用 LORA 微調 Gemma。 |
| [[Gemma_2]Finetune_with_LitGPT.ipynb]([Gemma_2]Finetune_with_LitGPT.ipynb) | 使用 [LitGPT](https://github.com/Lightning-AI/litgpt) 微調 Gemma。 |
| [[Gemma_2]Finetune_with_Torch_XLA.ipynb]([Gemma_2]Finetune_with_Torch_XLA.ipynb) | 使用 [PyTorch/XLA](https://github.com/pytorch/xla) 微調 Gemma。 |
| [[Gemma_2]Finetune_with_Unsloth.ipynb]([Gemma_2]Finetune_with_Unsloth.ipynb) | 使用 [Unsloth](https://unsloth.ai/blog/gemma) 微調 Gemma。 |
| [[Gemma_2]Translator_of_Old_Korean_Literature.ipynb]([Gemma_2]Translator_of_Old_Korean_Literature.ipynb) | 使用 Keras 與 Gemma 翻譯韓國古典文學。 |
| [[Gemma_3]Full_Model_Finetune_using_HF.ipynb]([Gemma_3]Full_Model_Finetune_using_HF.ipynb) | 使用 Hugging Face Transformers 與 TRL，在手機遊戲 NPC dataset 上進行完整模型微調 |
| [[Gemma_3n]Finetuned_LoRA_Unsloth_on_Mental_Health_dataset.ipynb]([Gemma_3n]Finetuned_LoRA_Unsloth_on_Mental_Health_dataset.ipynb) | 使用 [Unsloth](https://unsloth.ai/blog/gemma) 在心理健康諮商對話資料集上，於本地對 Gemma-3N（4B）模型進行 LoRA 微調，打造情緒急救助理。 |

## 對齊
| Notebook Name | Description |
| :------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[Gemma_2]Aligning_DPO.ipynb]([Gemma_2]Aligning_DPO.ipynb) | 示範如何使用 [Hugging Face TRL](https://huggingface.co/docs/trl/en/index) 與 DPO（Direct Preference Optimization）對齊 Gemma 模型。 |

## 評估
| Notebook Name | Description |
| :------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[Gemma_2]evaluation.ipynb]([Gemma_2]evaluation.ipynb) | 示範如何使用 Eleuther AI 的 LM evaluation harness 對 Gemma 進行模型評估。 |

## Agentic AI
| Notebook Name | Description |
| :------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------- |
| [[Gemma_2]Agentic_AI.ipynb]([Gemma_2]Agentic_AI.ipynb) | 示範如何使用 Gemma 2 建立 Agentic AI。 |
| [[Gemma_2]Function_Calling_with_Groq_Langchain.ipynb]([Gemma_2]Function_Calling_with_Groq_Langchain.ipynb) | 示範如何結合 Langchain、groq 與 Gemma2 建立簡單 agent。 |
| [[Gemma_3]Meme_Generator.ipynb]([Gemma_3]Meme_Generator.ipynb) | 使用 Gemma 3 4B IT model 的 Meme Generator |
| [[Gemma_3]Function_Calling_Routing_and_Monitoring_using_Gemma_Google_Genai.ipynb]([Gemma_3]Function_Calling_Routing_and_Monitoring_using_Gemma_Google_Genai.ipynb) | 實作並監控 Agentic RAG 工作流程 |
| [[Gemma_3]Function_Calling_with_HF.ipynb]([Gemma_3]Function_Calling_with_HF.ipynb) | 示範如何透過 [Hugging Face](https://huggingface.co/) 搭配 Gemma 3 使用 function calling。 |
| [[Gemma_3]Function_Calling_with_HF_document_summarizer.ipynb]([Gemma_3]Function_Calling_with_HF_document_summarizer.ipynb ) | 示範如何使用 Gemma 3、Hugging Face 與 function calling 建立文件摘要器。 |
| [[Gemma_3]Local_Agentic_RAG.ipynb]([Gemma_3]Local_Agentic_RAG.ipynb) | 使用 [FastEmbed](https://github.com/qdrant/fastembed)、[Ollama- Gemma3](https://ollama.com/models) 與 [Qdrant Vector database](https://cloud.qdrant.io)，在完全不依賴外部 APIs 的情況下建立本地 Agentic RAG |
