# Gemma 研究

本目錄包含使用 Google 的 Gemma 模型的研究實驗和範例。
## 專案

*   **[VaultGemma](#vaultgemma)**：具有差異隱私的注重隱私的fine-tuning。
*   **[T5Gemma](#t5gemma)**：Gemma 的編碼器-解碼器變體。
*   **[TranslateGemma](#translategemma)**：基於Gemma 3建構的翻譯模型

---

## 避難所Gemma

VaultGemma 是 Google Gemma 模型系列的注重隱私的變體，專為安全 fine-tuning 和具有差異隱私保證的部署而設計。此實作示範如何使用 LoRA（低階適應）和 Opacus 差分隱私對醫療資料上的 VaultGemma 1B 進行微調。
### 特徵

- **4 位元量化**：使用 BitsAndBytes 進行記憶體高效訓練
- **LoRA 微調**：可訓練參數<2% 的參數高效能自適應
- **差異隱私**：具有可設定 ε 和 δ 預算的隱私保護訓練
- **醫療問答**：針對醫療保健應用在醫療抽認卡 dataset 上進行微調

### 儲存庫結構

此儲存庫包含培訓和inference的程式碼：
* [微調](#fine-tuning)：如何微調差異隱私的 VaultGemma
* [推論](#inference)：如何載入並執行微調的 VaultGemma模型

### 微調

| notebook 名稱 | 描述 |:-------------- | ----------- |
| [[VaultGemma]FineTuning_Inference_Huggingface.ipynb]([VaultGemma]FineTuning_Inference_Huggingface.ipynb) | 使用 LoRA 適配器和差異隱私的醫療資料 fine-tuning VaultGemma 1B 的完整管道，以 inference 範例 |
#### 培訓特色
- 醫療草甸醫療抽認卡dataset
- 4 位元 NF4 量化可減少記憶體佔用
- LoRA 針對所有投影層的轉接器
- Opacus 差分隱私（ε=3.0，δ=1e-5）
- 帶有預熱的餘弦學習率計劃
- 根據丟失閾值自動checkpointing

### 推論

相同的 notebook 包括 inference 代碼：- 載入微調LoRA適配器
- 產生對醫療問題的答复
- 處理單一或批次查詢
- 調整生成參數（溫度、top_p）

#### 快速入門

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

### 要求

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

此實作提供了 (ε, δ)-差分隱私保證：- **目標ε**：3.0（可設定）
- **目標 δ**：1e-5（dataset 尺寸的倒數）
- **梯度裁切**：最大範數 1.0
- **隱私會計**：透過 Opacus 自動進行 epsilon 跟踪

---

## T5Gemma

T5Gemma（又稱編碼器-解碼器Gemma）是一系列編碼器-解碼器大語言模型，透過將預先訓練的僅解碼器模型改編成編碼器-解碼器架構而開發。
### 筆記型電腦

| notebook 名稱 | 描述 || :--- | :--- |
| [[T5Gemma]範例.ipynb]([T5Gemma]Example.ipynb) | 使用Flax 和Hugging Face 進行採樣和fine-tuning T5Gemma 指南 || [[T5Gemma_2]範例.ipynb]([T5Gemma_2]Example.ipynb) | 引導至 inference 與 T5Gemma 2 270m-270m 透過Hugging Face |
### 特徵

- **編碼器-解碼器架構**：將僅解碼器 Gemma 模型調整為 T5 風格架構。
- **秤**：
- **Gemma 2 級**：2B-2B、9B-2B 和 9B-9B。 - **T5 比例**：小號、基本號、大號、XL 和 ML。- **框架**：為 **Hugging Face** (PyTorch) 和 **Flax** (Kauldron) 提供範例。
- **任務**：
- **採樣**：基本文字產生範例。 - **微調**：使用 MTNT dataset 進行機器翻譯（英語到法語）的 fine-tuning 範例。
### 要求

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

## 翻譯Gemma

TranslateGemma 是 Google 的一系列輕量級、最先進的開放翻譯模型，基於 Gemma 3 系列模型。
TranslateGemma 模型旨在處理 55 種語言的翻譯任務。它們的尺寸相對較小，因此可以將它們部署在資源有限的環境中，例如筆記型電腦、桌上型電腦或您自己的雲端基礎設施，從而實現對最先進翻譯模型的民主化訪問，並幫助促進每個人的創新。
### 筆記型電腦

| notebook 名稱 | 描述 || :--- | :--- |
| [[翻譯Gemma]範例.ipynb]([TranslateGemma]Example.ipynb) | Guide to inference with TranslateGemma via Hugging Face |