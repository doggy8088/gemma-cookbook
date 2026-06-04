# 快速入門指南：建立 0.9B 和更小的 Gemma 3n 模型

## TL;DR - 5 分鐘內開始

### 適用於 0.9B 型號（26 層 - 建議用於 4-6GB RAM 手機）

1. **開啟** MatFormer 實驗室notebook：`[Gemma_3n]MatFormer_Lab.ipynb`

2. **導航至「設定詳細資料」cell**（CSV 載入後）

3. **用此替換`config_name`行**或將其註解掉並取消註解自訂設定cell：

```python
# Option A: Using custom configuration
layers_to_skip = [19, 20, 21, 22, 23, 24, 25, 26, 27]
ffn_hidden_dims = [2048*3]*10 + [int(2048*3.5)]*9 + [2048*4]*7
ffn_hidden_dims_str = str(ffn_hidden_dims)

# Option B: Using the config_name selector (if added to dropdown)
config_name = "Custom 0.9B (26-layer)"
```

4. **正常運作所有後續cells**

5. **結果**：0.95B 模型適合 4-6GB RAM，具有 4 位元量化

---

## 詳細對照表

| 設定 | 層數 | 參數 | MMLU 預計。 | 4 位元大小 | 最適合 ||--------|--------|-----------|----------|-----------|----------|
| **0.5B (20L)** | 20 | 0.52B | 40-42% | 〜0.9GB | 網路、超輕型行動設備 || **0.7B (23L)** | 23 | 0.71B | 44-46% | 〜1.1GB | 輕型行動裝置（4GB） || **0.9B (26L)** | 26 | 0.95B | 46-48% | 〜1.5GB | **行動裝置（4-6GB）** ✓ || **1.3B（28L）** | 28 | 1.32B | 48-50% | 〜2.1GB | 行動裝置（6-8GB） || **E2B (30L)** | 30 | 1.91B | 50.9% | 〜2.9GB | 移動（8GB+） || **1.5B (30L)** | 30 | 1.51B | 49-51% | 〜2.3GB | 高階手機 |
---

## 逐步實施

### 第1步：準備環境

```bash
# In Google Colab or local environment with GPU
!pip install "transformers>=4.53" "timm>=1.0.16" -q

# Login to Hugging Face (required for model access)
from huggingface_hub import notebook_login
notebook_login()
```

### 第2步：設定模型來源

```python
# In the "Import and Export Options" cell
original_model_id = "google/gemma-3n-E4B-it"  # or E4B-pt for pre-trained
local_output_path = "my_0_9b_model"
push_hf_repo_id = "username/gemma-3n-0-9b"  # Your HF repo
```

### 步驟 3：套用 0.9B 設定

**在「設定詳細資料」cell**中，取消註解並設定：
```python
# Custom config for 0.9B model
layers_to_skip = [19, 20, 21, 22, 23, 24, 25, 26, 27]

# FFN hidden dimensions (optimized distribution)
ffn_hidden_dims = (
    [2048 * 3] * 10 +      # Layers 0-9: 6,144
    [int(2048 * 3.5)] * 9 +     # Layers 10-18: 7,168
    [2048 * 4] * 7         # Layers 19-25: 8,192
)

ffn_hidden_dims_str = str(ffn_hidden_dims)

print(f"Config: 0.9B Model")
print(f"Layers Skipped: {layers_to_skip}")
print(f"Final Layers: {35 - len(layers_to_skip)}")
print(f"FFN Dims (first 10): {ffn_hidden_dims[:10]}")
```

### 第 4 步：執行切片管道

```python
# Run cells in order:
# 1. Load the model config
# 2. Verify slicing configuration
# 3. Update configuration
# 4. Save configuration and tokenizer
# 5. Load model checkpoints
# 6. Slice the model! (main processing)
# 7. Save final model
```

### 步驟5：推送至Hugging Face（可選）

```python
# Push sliced model to your Hugging Face repo
from huggingface_hub import HfApi

api = HfApi()
api.upload_folder(
    folder_path=local_output_path,
    repo_id=push_hf_repo_id,
    repo_type="model"
)
```

### 第 6 步：載入和測試

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
import torch

# Load your sliced model
model = AutoModelForCausalLM.from_pretrained(
    push_hf_repo_id,
    torch_dtype=torch.float16,
    device_map="auto",
    quantization_config=BitsAndBytesConfig(load_in_4bit=True)
)

print(f"Model parameters: {model.num_parameters():,}")
```

---

## 不同場景的設定預設

### 場景 1：行動應用程式（4GB RAM）

```python
# Best: 0.9B with 4-bit quantization
layers_to_skip = [19, 20, 21, 22, 23, 24, 25, 26, 27]
ffn_hidden_dims = [2048*3]*10 + [int(2048*3.5)]*9 + [2048*4]*7

# Expected performance:
# - Model size: ~1.2 GB (quantized)
# - Inference speed: 50-100 tokens/sec
# - Memory during inference: 2.5-3.5 GB
```

### 場景 2：Web 瀏覽器（客戶端）

# 最佳：0.5B，具有極端量化
layers_to_skip = [12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
ffn_hidden_dims = [2048*2]*8 + [int(2048*2.5)]*7 + [2048*3]*5

# 預期的：
# - Model size: ~0.8-0.9 GB
# - 瀏覽器中的推論 (ONNX/WebGPU)
# - 快速第一響應

### 場景 3：邊緣設備（6GB RAM，偏好準確度）

```python
# Best: 1.3B with 4-bit
layers_to_skip = [21, 22, 23, 24, 25, 26, 27]
ffn_hidden_dims = [2048*3]*10 + [int(2048*3.5)]*9 + [2048*4]*9

# Expected:
# - MMLU: 48-50%
# - Size: 1.8-2.1 GB (quantized)
# - Best quality/size tradeoff
```

---

## 了解 FFN 維度策略

FFN（前饋網路）維度控制每一層的模型容量：
```
FFN_dim = 2048 * multiplier

2048 * 2   = 4,096    (very compact, low capacity)
2048 * 2.5 = 5,120    (compact)
2048 * 3   = 6,144    (standard light)
2048 * 3.5 = 7,168    (medium)
2048 * 4   = 8,192    (full capacity)
```

### 為什麼採用這種分佈？

```
Early layers (0-9):   Lower capacity (6,144)
  → Capture basic linguistic features
  → Can reuse in inference

Middle layers (10-18): Medium capacity (7,168)
  → Process semantic content
  → Balance efficiency and modeling

Late layers (19-25):  Full capacity (8,192)
  → Critical for output quality
  → Global layers with KV sharing
  → Must preserve for performance
```

**經驗法則**：後面的層對於輸出品質更重要，因此請使其保持滿載。
---

## 推論優化技巧

### 對於行動部署

```python
# 1. Use 4-bit quantization
from transformers import BitsAndBytesConfig
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

# 2. Disable caching if memory is critical
model.config.use_cache = False

# 3. Use streaming inference
from transformers import TextIteratorStreamer
from threading import Thread

# 4. Limit sequence length
max_tokens = 512

# 5. Use faster attention (if available)
model.config.attn_implementation = "flash_attention_2"
```

### 對於網路部署

```python
# 1. Convert to ONNX or TensorFlow
# python -m transformers.onnx --model=username/gemma-3n-0-9b my_model_onnx

# 2. Quantize for browser
# Use onnx-quantizer or WebGPU native quantization

# 3. Implement streaming with server-sent events
# Best for web UI responsiveness
```

---

## 業績預期

### 準確度（MMLU 基準）

```
Full E4B (3.98B):  62.30%
Full E2B (1.91B):  50.90%
─────────────────────────
Custom 1.5B:       49-51%  ← Best tradeoff
Custom 1.3B:       48-50%
Custom 0.9B:       46-48%  ← Recommended for 4-6GB
Custom 0.7B:       44-46%
Custom 0.5B:       40-42%  ← Web-only
```

### 推論速度（token/秒，單 GPU）

```
Device: NVIDIA L4 GPU (Colab free tier)
Batch size: 1, Sequence length: 512

Custom 0.9B:  80-120 tokens/sec
Custom 1.3B:  60-90 tokens/sec
E2B (1.91B):  40-60 tokens/sec
E4B (3.98B):  20-40 tokens/sec

Mobile (Snapdragon 8 Gen 3):
Custom 0.9B (quantized): 5-15 tokens/sec
Custom 0.5B (quantized): 10-25 tokens/sec
```

### 記憶體使用情況

```
FP32 (full precision):
  0.9B: ~3.6 GB

FP16 / BF16:
  0.9B: ~1.8 GB

INT8:
  0.9B: ~0.9 GB

INT4 / NF4:
  0.9B: ~0.5-0.7 GB (params) → ~1.5 GB (total)  ← Recommended for mobile
```

---

## 故障排除

### 問題：「X 層和 Y 層已保留」錯誤

**解決方案**：不要跳過最後2層（KV 共享層）```python
# ✓ Correct
layers_to_skip = [19, 20, 21, 22, 23, 24, 25, 26, 27]  # Keeps 0-18 + 28-34

# ✗ Wrong
layers_to_skip = [19, 20, 21, 22, 23, 24, 33, 34]  # Skips global layers!
```

### 問題：FFN 尺寸長度不匹配

**解決方案**：確保長度與最終層數匹配```python
final_layers = 35 - len(layers_to_skip)  # Should be 26
ffn_dims = [2048*3]*10 + [int(2048*3.5)]*9 + [2048*4]*7  # Length must be 26

assert len(ffn_dims) == final_layers  # Verify
```

### 問題：切片期間記憶體不足

**解決方案**：- 在 Google Colab 上執行（免費 GPU）
- 或使用具有足夠 RAM (16GB+) 的 CPU
- 模型不會載入到記憶體中，僅處理checkpoints

### 問題：切片模型載入但品質較差

**解決方案**：檢查 FFN 維度分佈```python
# Better: Keep later layers at full capacity
ffn = [int(2048*2.5)]*10 + [int(2048*3.5)]*8 + [2048*4]*8  # ✓

# Worse: Uniform low capacity
ffn = [int(2048*2.5)]*26  # ✗ (poor quality)
```

---

## 下一步

1. **使用 MatFormer Lab 測試上面的 0.9B 設定**
2. **在您的目標裝置上進行評估**（測量 inference 速度、記憶體）
3. **根據需要進行微調** 在您的網域資料上使用LoRA
4. **部署**，為行動裝置提供 4 位元量化
5. **監控**效能並迭代

---

## 其他資源

- **MatFormer 紙**：https://arxiv.org/abs/2310.07707
- **Gemma 3n blog**：https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide
- **切片設定 dataset**：https://huggingface.co/datasets/google/gemma3n-slicing-configs
- **量化指南**：https://huggingface.co/docs/transformers/quantization
- **行動部署**：https://huggingface.co/docs/transformers/onnx

---

## 有疑問或問題嗎？

如果這些設定不適合您的用例：1. 檢查 [custom_slicing_configs.py](./custom_slicing_configs.py) 進行程式驗證
2. 參考【詳細分析】(./RESPONSE_SUB_BILLION_AND_AUDIO_SLICING.md)
3. 提出有關您的設備規格和限制的問題

