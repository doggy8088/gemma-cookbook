# 教學

適用於 Gemma 型號和變體的筆記型電腦。

| notebook 名稱 | 描述 ||:--| --- |
| [代理_RAG.ipynb](Agentic_RAG.ipynb) | 建立一個 Agentic RAG 系統，聰明地決定何時呼叫函數，使用基於 Qdrant 的 RAG 管道，並回退到 Google 搜尋。使用 OPIK 進行追蹤和監控。 || [Image_Segmentation.ipynb](Image_Segmentation.ipynb) | Gemma 4 的影像分割任務 || [RAG_with_EmbeddingGemma.ipynb](RAG_with_EmbeddingGemma.ipynb) | 使用 [EmbeddingGemma](https://ai.google.dev/gemma/docs/embeddinggemma) 建立簡單的RAG |
## 推論能力

探索 Gemma 跨不同模式的功能：
| notebook 名稱 | 描述 ||:--| --- |
| [內文 - 基本](../docs/capabilities/text/basic.ipynb) | 基本文本生成和 prompting Gemma 4. || [文字-函數呼叫](../docs/capabilities/text/function-calling-gemma4.ipynb) | 利用 Gemma 4 進行工具使用和函數呼叫。 || [視覺-圖像](../docs/capabilities/vision/image.ipynb) | 使用 Gemma 進行視覺理解和字幕 4. || [視覺-影片](../docs/capabilities/vision/video.ipynb) | Video understanding and analysis with Gemma 4. || [音訊](../docs/capabilities/audio.ipynb) | 探索音頻處理和理解。 || [思考](../docs/capabilities/thinking.ipynb) | 推論能力。 |
## 微調

fine-tuning Gemma 型號範例：
| notebook 名稱 | 描述 ||:--| --- |
| [使用QLoRA進行文字微調](../docs/core/huggingface_text_finetune_qlora.ipynb) | 使用QLoRA 有效微調Gemma 4 的文字任務。 || [使用QLoRA進行視覺微調](../docs/core/huggingface_vision_finetune_qlora.ipynb) | 使用QLoRA 有效微調Gemma 4 的視覺任務。 |