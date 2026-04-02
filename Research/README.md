# Gemma Research

這個目錄收錄使用 Google Gemma 模型的研究實驗與範例。

## 專案

*   **[VaultGemma](#vaultgemma)**：聚焦隱私、結合 differential privacy 的微調。
*   **[T5Gemma](#t5gemma)**：Gemma 的 encoder-decoder 變體。
*   **[TranslateGemma](#translategemma)**：建立於 Gemma 3 之上的翻譯模型

---

## VaultGemma

VaultGemma 是 Google Gemma 模型家族中以隱私為重點的變體，設計目的是在 differential privacy 保證下安全地進行微調與部署。這份實作示範如何使用 LoRA（Low-Rank Adaptation）與 Opacus，在醫療資料上微調 VaultGemma 1B。

### 功能特色

- **4-bit Quantization**：使用 BitsAndBytes 進行節省記憶體的訓練
- **LoRA Fine-tuning**：以少於 2% 的可訓練參數完成高參數效率的適配
- **Differential Privacy**：提供可設定 ε 與 δ 預算的隱私保護訓練
- **Medical Q&A**：以醫療 flashcard dataset 微調，適用於 healthcare 應用

### Repository Structure

這個目錄同時包含訓練與推論的程式碼：

* [Fine-tuning](#fine-tuning)：如何使用 differential privacy 微調 VaultGemma
* [Inference](#inference)：如何載入並執行已微調的 VaultGemma 模型

### Fine-tuning

| Notebook Name | Description |
:-------------- | ----------- |
| [[VaultGemma]FineTuning_Inference_Huggingface.ipynb]([VaultGemma]FineTuning_Inference_Huggingface.ipynb) | 使用 LoRA adapters 與 differential privacy，在醫療資料上微調 VaultGemma 1B 的完整流程，並附帶推論範例 |

#### 訓練特色
- Medical Meadow Medical Flashcards dataset
- 使用 4-bit NF4 quantization 降低記憶體占用
- LoRA adapters 套用到所有 projection layers
- Opacus differential privacy（ε=3.0、δ=1e-5）
- 含 warmup 的 cosine learning rate schedule
- 依 loss 門檻自動 checkpointing

### Inference

同一份 notebook 也包含以下推論程式碼：
- 載入已微調的 LoRA adapters
- 生成醫療問題的回應
- 處理單筆或批次查詢
- 調整 generation parameters（`temperature`、`top_p`）

#### 快速開始

```python
from transformers import AutoModelForCausalLM, GemmaTokenizer
from peft import PeftModel

# Load model and adapters
model = AutoModelForCausalLM.from_pretrained("google/vaultgemma-1b")
tokenizer = GemmaTokenizer.from_pretrained("google/vaultgemma-1b")
peft_model = PeftModel.from_pretrained(model, "path/to/adapters")

# Generate response
question = "What are the symptoms of diabetes?"
response = generate_response(question)
```

### Requirements

```
torch
transformers
peft
opacus
datasets
bitsandbytes
kagglehub
```

### 隱私保證

這份實作提供（ε, δ）-differential privacy 保證：
- **Target ε**：3.0（可調整）
- **Target δ**：1e-5（資料集大小的倒數）
- **Gradient clipping**：最大 norm 為 1.0
- **Privacy accounting**：透過 Opacus 自動追蹤 epsilon

---

## T5Gemma

T5Gemma（又稱 encoder-decoder Gemma）是一個 encoder-decoder 大型語言模型家族，做法是將預先訓練的 decoder-only 模型改造成 encoder-decoder 架構。

### Notebooks

| Notebook Name | Description |
| :--- | :--- |
| [[T5Gemma]Example.ipynb]([T5Gemma]Example.ipynb) | 使用 Flax 與 Hugging Face 對 T5Gemma 進行 sampling 與微調的指南 |
| [[T5Gemma_2]Example.ipynb]([T5Gemma_2]Example.ipynb) | 透過 Hugging Face 對 T5Gemma 2 270m-270m 進行推論的指南 |

### 功能特色

- **Encoder-Decoder Architecture**：將 decoder-only 的 Gemma 模型改造成 T5 風格架構。
- **Scales**：
    - **Gemma 2 scale**：2B-2B、9B-2B、9B-9B。
    - **T5 scale**：Small、Base、Large、XL、ML。
- **Frameworks**：同時提供 **Hugging Face**（PyTorch）與 **Flax**（Kauldron）範例。
- **Tasks**：
    - **Sampling**：基本文字生成範例。
    - **Fine-tuning**：使用 MTNT dataset 進行英翻法機器翻譯微調的範例。

### Requirements

```
gemma
kauldron
etils
optax
treescope
kagglehub
transformers
datasets
```

---

## TranslateGemma

TranslateGemma 是 Google 推出的輕量、最先進開放翻譯模型家族，建立於 Gemma 3 模型家族之上。

TranslateGemma 模型設計用於處理 55 種語言的翻譯任務。由於模型相對精巧，因此能部署在筆電、桌機或自建 cloud infrastructure 等資源有限的環境中，讓更多人能取得最先進翻譯模型，也有助於促進更廣泛的創新。

### Notebooks

| Notebook Name | Description |
| :--- | :--- |
| [[TranslateGemma]Example.ipynb]([TranslateGemma]Example.ipynb) | 透過 Hugging Face 使用 TranslateGemma 進行推論的指南 |
