# Quick Start Guide: 建立 0.9B 與更小的 Gemma 3n Models

## TL;DR - 5 分鐘快速上手

### 針對 0.9B 模型（26 layers，建議用於 4-6GB RAM Mobile）

1. **開啟** MatFormer Lab notebook：`[Gemma_3n]MatFormer_Lab.ipynb`

2. **找到 "Config details" cell**（位於 CSV 載入之後）

3. **將 `config_name` 那行替換成**下列內容，或把它註解後啟用 custom config cell：

```python
# Option A: Using custom configuration
layers_to_skip = [19, 20, 21, 22, 23, 24, 25, 26, 27]
ffn_hidden_dims = [2048*3]*10 + [int(2048*3.5)]*9 + [2048*4]*7
ffn_hidden_dims_str = str(ffn_hidden_dims)

# Option B: Using the config_name selector (if added to dropdown)
config_name = "Custom 0.9B (26-layer)"
```

4. **照常執行後續所有 cells**

5. **結果**：得到搭配 4-bit quantization 可放入 4-6GB RAM 的 0.95B 模型

---

## 詳細 Comparison Table

| Config | Layers | Parameters | MMLU Est. | 4-bit Size | Best For |
|--------|--------|-----------|----------|-----------|----------|
| **0.5B (20L)** | 20 | 0.52B | 40-42% | ~0.9 GB | Web、超輕量 mobile |
| **0.7B (23L)** | 23 | 0.71B | 44-46% | ~1.1 GB | 輕量 mobile（4GB） |
| **0.9B (26L)** | 26 | 0.95B | 46-48% | ~1.5 GB | **Mobile（4-6GB）** ✓ |
| **1.3B (28L)** | 28 | 1.32B | 48-50% | ~2.1 GB | Mobile（6-8GB） |
| **E2B (30L)** | 30 | 1.91B | 50.9% | ~2.9 GB | Mobile（8GB+） |
| **1.5B (30L)** | 30 | 1.51B | 49-51% | ~2.3 GB | High-end mobile |

---

## Step-by-Step Implementation

### Step 1: 準備環境

```bash
# In Google Colab or local environment with GPU
!pip install "transformers>=4.53" "timm>=1.0.16" -q

# Login to Hugging Face (required for model access)
from huggingface_hub import notebook_login
notebook_login()
```

### Step 2: 設定 Model Source

```python
# In the "Import and Export Options" cell
original_model_id = "google/gemma-3n-E4B-it"  # or E4B-pt for pre-trained
local_output_path = "my_0_9b_model"
push_hf_repo_id = "username/gemma-3n-0-9b"  # Your HF repo
```

### Step 3: 套用 0.9B Configuration

**在 "Config details" cell 中**，取消註解並設定：

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

### Step 4: 執行 Slicing Pipeline

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

### Step 5: 推送到 Hugging Face（選用）

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

### Step 6: 載入並測試

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

## 不同情境的 Configuration Presets

### Scenario 1: Mobile App（4GB RAM）

```python
# Best: 0.9B with 4-bit quantization
layers_to_skip = [19, 20, 21, 22, 23, 24, 25, 26, 27]
ffn_hidden_dims = [2048*3]*10 + [int(2048*3.5)]*9 + [2048*4]*7

# Expected performance:
# - Model size: ~1.2 GB (quantized)
# - Inference speed: 50-100 tokens/sec
# - Memory during inference: 2.5-3.5 GB
```

### Scenario 2: Web Browser（Client-side）

```python
# Best: 0.5B with extreme quantization
layers_to_skip = [12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
ffn_hidden_dims = [2048*2]*8 + [int(2048*2.5)]*7 + [2048*3]*5

# Expected:
# - Model size: ~0.8-0.9 GB
# - Inference in browser (ONNX/WebGPU)
# - Fast first response
```

### Scenario 3: Edge Device（6GB RAM，偏好準確度）

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

## 理解 FFN Dimension 策略

FFN（Feed-Forward Network）dimension 會控制每一層的模型容量：

```
FFN_dim = 2048 * multiplier

2048 * 2   = 4,096    (非常精簡，容量低)
2048 * 2.5 = 5,120    (精簡)
2048 * 3   = 6,144    (標準輕量)
2048 * 3.5 = 7,168    (中等)
2048 * 4   = 8,192    (完整容量)
```

### 為什麼這樣分布？

```
前段 layers（0-9）：   較低容量（6,144）
  → 捕捉基礎語言特徵
  → 可重用於 inference

中段 layers（10-18）： 中等容量（7,168）
  → 處理語意內容
  → 在效率與建模能力之間取得平衡

後段 layers（19-25）： 完整容量（8,192）
  → 對輸出品質至關重要
  → 屬於具 KV sharing 的 global layers
  → 必須保留以維持效能
```

**經驗法則**：越後面的 layers 對輸出品質越重要，因此應保留完整容量。

---

## Inference Optimization Tips

### 針對 Mobile Deployment

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

### 針對 Web Deployment

```python
# 1. Convert to ONNX or TensorFlow
# python -m transformers.onnx --model=username/gemma-3n-0-9b my_model_onnx

# 2. Quantize for browser
# Use onnx-quantizer or WebGPU native quantization

# 3. Implement streaming with server-sent events
# Best for web UI responsiveness
```

---

## 效能預期

### 準確度（MMLU benchmark）

```
Full E4B (3.98B):  62.30%
Full E2B (1.91B):  50.90%
─────────────────────────
Custom 1.5B:       49-51%  ← 最佳權衡
Custom 1.3B:       48-50%
Custom 0.9B:       46-48%  ← 建議用於 4-6GB
Custom 0.7B:       44-46%
Custom 0.5B:       40-42%  ← 適合 web-only
```

### Inference Speed（Tokens/sec，單張 GPU）

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

### 記憶體使用量

```
FP32 (full precision):
  0.9B: ~3.6 GB

FP16 / BF16:
  0.9B: ~1.8 GB

INT8:
  0.9B: ~0.9 GB

INT4 / NF4:
  0.9B: ~0.5-0.7 GB (params) → ~1.5 GB (total)  ← 建議用於 mobile
```

---

## 疑難排解

### 問題："Layers X and Y are reserved" error

**解法**：不要 skip 最後 2 個 layers（KV shared layers）
```python
# ✓ 正確
layers_to_skip = [19, 20, 21, 22, 23, 24, 25, 26, 27]  # 保留 0-18 + 28-34

# ✗ 錯誤
layers_to_skip = [19, 20, 21, 22, 23, 24, 33, 34]  # Skip 到 global layers 了
```

### 問題：FFN dimensions 長度不符

**解法**：確保長度與最終 layer 數一致
```python
final_layers = 35 - len(layers_to_skip)  # 應為 26
ffn_dims = [2048*3]*10 + [int(2048*3.5)]*9 + [2048*4]*7  # 長度必須是 26

assert len(ffn_dims) == final_layers  # 驗證
```

### 問題：Slicing 過程中 out of memory

**解法**：
- 在 Google Colab 上執行（免費 GPU）
- 或改用具足夠 RAM（16GB+）的 CPU
- 模型不會整個載入記憶體，而是逐步處理 checkpoints

### 問題：Sliced model 可以載入，但品質很差

**解法**：檢查 FFN dimension 的分布
```python
# Better: 後段 layers 保留完整容量
ffn = [int(2048*2.5)]*10 + [int(2048*3.5)]*8 + [2048*4]*8  # ✓

# Worse: 全部使用均一低容量
ffn = [int(2048*2.5)]*26  # ✗（品質差）
```

---

## 下一步

1. 使用上述 0.9B configuration 在 MatFormer Lab 中測試
2. 在目標裝置上評估（量測 inference speed、memory）
3. 視需要使用 LoRA 在你的 domain data 上微調
4. 以 4-bit quantization 部署到 mobile
5. 持續監控效能並迭代

---

## 其他資源

- **MatFormer Paper**: https://arxiv.org/abs/2310.07707
- **Gemma 3n Blog**: https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide
- **Slicing Configs Dataset**: https://huggingface.co/datasets/google/gemma3n-slicing-configs
- **Quantization Guide**: https://huggingface.co/docs/transformers/quantization
- **Mobile Deployment**: https://huggingface.co/docs/transformers/onnx

---

## 問題或需求？

如果這些 configurations 不符合你的使用情境：
1. 先查看 [custom_slicing_configs.py](./custom_slicing_configs.py) 做程式化驗證
2. 參考[詳細分析文件](./RESPONSE_SUB_BILLION_AND_AUDIO_SLICING.md)
3. 連同裝置規格與限制提交 issue
