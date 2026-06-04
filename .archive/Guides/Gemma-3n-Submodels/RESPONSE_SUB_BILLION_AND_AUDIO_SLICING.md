# Response: Gemma 3n 的 Sub-Billion Model Slicing 與 Audio Encoder Reduction

## 概覽

本文件針對兩項與 Gemma 3n model slicing 有關的 feature requests，提供技術指引與建議，目標是支援資源受限環境（4-6GB RAM 的 mobile devices 與 web deployment）：

1. 建立小於 1.91B 的模型（可達 0.9B 或更小，26 layers）
2. 將 layer reduction 技術套用到 audio encoder

---

## Part 1: 建立 Sub-Billion Models（0.9B 或更小）

### 目前的 Configuration Landscape

MatFormer Lab notebook（`[Gemma_3n]MatFormer_Lab.ipynb`）目前支援的 slicing configurations 範圍介於 **1.91B（E2B）** 到 **3.98B（E4B）**，其中最小的是：

- **官方 E2B Model 的 config**
  - Effective Parameters：1.91B
  - Number of Layers：30
  - Layers Skipped：`[20, 21, 22, 23, 24]`
  - FFN Hidden Dims：所有 layers 都是 `[2048 * 4]`（8,192）

### Sub-Billion Models 的可行性

**是的，絕對可以透過 MatFormer slicing 技術建立小於 0.9B 的模型**。設計上要考量以下幾點：

#### Option A: 走 Layer Reduction 路線（26 Layers）

對於 **26 layers 的 0.9B 模型**，可考慮以下 configuration：

```python
# Proposed configuration for 0.9B model
layers_to_skip = [17, 18, 19, 20, 21, 22, 23, 24]  # Skip 8 layers (from original 35)
final_num_layers = 35 - 8  # 27

# FFN Hidden Dimensions (suggested)
ffn_hidden_dims = [2048 * 3] * 10 + [int(2048 * 3.5)] * 10 + [2048 * 4] * 7

# Estimated model size:
# - Embedding: ~250M (token embedding, ~256k vocab)
# - 27 layers × (attention + FFN) with varying capacities: ~600M
# - Output projection: ~100M
# **Total: ~950M (0.95B)**
```

#### Option B: 更小的 0.5B 模型（20 Layers）

若要更積極壓縮：

```python
# Proposed configuration for 0.5B model
layers_to_skip = [12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24]  # Skip 12 layers
final_num_layers = 35 - 12  # 23

# FFN Hidden Dimensions (ultra-compact)
ffn_hidden_dims = [
    2048 * 2,    # 4,096 for layers 0-7 (minimal capacity)
    2048 * 2,
    2048 * 2,
    2048 * 2,
    2048 * 2,
    2048 * 2,
    2048 * 2,
    2048 * 2,
    int(2048 * 2.5),  # 5,120 for layers 8-14 (moderate)
    int(2048 * 2.5),
    int(2048 * 2.5),
    int(2048 * 2.5),
    int(2048 * 2.5),
    int(2048 * 2.5),
    int(2048 * 2.5),
    2048 * 3,    # 6,144 for layers 15-22 (higher capacity)
    2048 * 3,
    2048 * 3,
    2048 * 3,
    2048 * 3,
    2048 * 3,
    2048 * 3,
    2048 * 3,
]

# Estimated model size: ~500M (0.5B)
```

### 最佳化 Slicing 建議

依照既有 configs 可觀察到的 MatFormer 設計原則：

#### 關鍵設計原則：

1. **Layer Distribution**：應優先從中後段（layers 15-24）skip，而不是前段 layers，因為前段 layers 會捕捉重要的低階語言特徵
2. **FFN Capacity Distribution**：
   - Layers 0-10：較低容量（2048×2 到 2048×3）
   - Layers 11-20：中等容量（2048×3 到 2048×3.5）
   - Layers 21+：較高容量（2048×4）
3. **Reserved Layers**：務必保留最後 2 個 global layers（原始模型中的 layers 33-34），它們對輸出品質非常關鍵
4. **KV Sharing**：最後 2 層使用 KV sharing，因此必須保留

#### 0.9B（26 layers）建議 Configuration：

```python
# Recommended configuration
config_name = "Custom 0.9B (26-layer)"

# Skip 9 layers (35 - 26 = 9)
layers_to_skip = [19, 20, 21, 22, 23, 24, 25, 26, 27]

# FFN Hidden Dimensions (optimized for Pareto frontier)
ffn_hidden_dims = [2048 * 3] * 10 + [int(2048 * 3.5)] * 9 + [2048 * 4] * 7
# Estimated MMLU Performance: 46-48% (compared to E2B's 50.9%)
# Memory Requirements: ~2.2-2.4 GB for inference (FP32)
# Target Deployment: 4-6 GB RAM mobile devices (with 4-bit quantization)
```

### 在 MatFormer Lab 中實作

若要在現有 MatFormer Lab notebook 中使用此設定：

```python
# In the "Config details" cell, uncomment and set:
layers_to_skip = [19, 20, 21, 22, 23, 24, 25, 26, 27]
ffn_hidden_dims = [2048*3]*10 + [int(2048*3.5)]*9 + [2048*4]*7
ffn_hidden_dims_str = str(ffn_hidden_dims)
```

---

## Part 2: Audio Encoder Slicing

### 現有架構

Gemma 3n 是一個 **multimodal model**，包含：
- Text encoder/decoder（目前 slicing 的主要焦點）
- Vision encoder（圖片處理）
- Audio encoder（語音處理）

### Audio Encoder Reduction 的可行性

**可以，audio encoder 也能使用類似的 layer-slicing 技術縮減**，但因為 MatFormer Lab notebook 目前主要聚焦於 text model slicing，所以仍需要額外實作。

#### Audio Encoder 特性

Gemma 3n 的 audio encoder 通常具備：
- 約 12-24 個 transformer layers
- 與 text encoder 類似的結構（attention + FFN）
- 可透過 skip layers 或縮減 FFN dimensions 來壓縮

### 建議的 Audio Encoder Slicing 方法

#### Step 1: 找出 Audio Encoder Configuration

```python
# Load the original model config
from transformers import AutoConfig

config = AutoConfig.from_pretrained("google/gemma-3n-E4B-it")

# Access audio encoder config
audio_config = config.audio_config  # or similar field name

print(f"Original audio layers: {audio_config.num_hidden_layers}")
print(f"Audio FFN dimension: {audio_config.intermediate_size}")
```

#### Step 2: 建議的 Audio Encoder 縮減方式

若整體目標是 0.9B，建議：

```python
# Audio encoder reduction (from original ~16-20 layers)
audio_layers_to_skip = [12, 13, 14, 15]  # Skip last 4 layers
# Keep: 12 layers (vs. original 16)

# FFN reduction for audio
audio_ffn_hidden_dims = [1024 * 3] * 12  # Reduce from 1024*4

# Expected audio encoder size: ~80-100M parameters
# Combined with text (0.8B) = 0.9B total
```

#### Step 3: 實作需求

與 text encoder 不同，audio encoder slicing 額外需要：

1. **修改 model slicing code**，讓它能以同樣方式處理 audio encoder 參數：
   - Pattern：`.audio_model.layers.{layer_idx}.`
   - 套用相同的 FFN dimension slicing logic

2. **更新 MatFormer Lab notebook 中的 safetensors loading**：
   ```python
   # Add audio processing to the tensor slicing loop
   elif '.audio_model.layers.' in tensor_name:
       match = re.search(r'\.layers\.(\d+)\.', tensor_name)
       if not match:
           continue  # Or handle error appropriately

       # Apply similar slicing logic as text encoder
       old_layer_idx = int(match.group(1))
       if old_layer_idx in audio_layers_to_skip:
           continue
       new_layer_idx = audio_layer_rename_map[old_layer_idx]
       # ... slice audio FFN dimensions ...
   ```

3. **更新 config.json**：
   ```python
   config.audio_config.num_hidden_layers = 12  # Reduced from 16
   config.audio_config.intermediate_size = 3072  # Reduced from 4096
   ```

### Audio + Text Joint Optimization

若要在資源受限情境中取得最佳表現，可考慮：

| Model Size | Text Layers | Text FFN | Audio Layers | Audio FFN | RAM (4-bit) | Use Case |
|-----------|------------|---------|--------------|-----------|-----------|----------|
| 0.5B | 20 | 2048×2-3 | 10 | 1024×2 | ~1.5 GB | Ultra-light mobile |
| 0.9B | 26 | 2048×3-3.5 | 12 | 1024×3 | ~2.2 GB | Standard mobile |
| 1.5B | 28 | 2048×3.5-4 | 14 | 1024×3.5 | ~3.8 GB | High-end mobile |

---

## Implementation Roadmap

### Phase 1: 僅處理 Text Model（可立即進行）
使用現有 MatFormer Lab notebook 搭配 0.9B configuration（26 layers）

### Phase 2: 支援 Audio Encoder（Enhancement）
1. 擴充 MatFormer Lab slicing logic，使其可處理 audio encoder
2. 加入 audio 專用 configuration parameters
3. 建立新 notebook：`[Gemma_3n]MatFormer_Lab_with_Audio_Slicing.ipynb`

### Phase 3: 驗證與 Benchmarking（選用）
1. 評估 sub-billion configs 的 MMLU 表現
2. 在目標 mobile devices 上量測 inference latency
3. 撰寫 mobile deployment guide

---

## Practical Migration Steps

### 針對不含 Audio 變更的 0.9B 模型：

```python
# In MatFormer Lab notebook, cell "Config details":
config_name = "Custom 0.9B (26-layer)"

# Manually set:
layers_to_skip = [19, 20, 21, 22, 23, 24, 25, 26, 27]
ffn_hidden_dims = [2048*3]*10 + [int(2048*3.5)]*9 + [2048*4]*7
ffn_hidden_dims_str = str(ffn_hidden_dims)

# Run remaining cells as usual
```

### 若要完整支援 Audio：

需要建立新的增強版 notebook，其中包含：
- Audio encoder configuration UI
- 擴充過的 tensor slicing logic
- 個別的 audio layer skip / FFN configs
- Joint optimization validation

---

## Deployment Recommendations

### 針對 4-6 GB Mobile RAM：

1. **使用 0.9B 模型**，採用上述 configuration
2. **套用 4-bit quantization**（NF4/Int4），將大小降至約 1.2-1.5 GB
3. **保持 audio encoder 精簡**（12 layers、1024×3 FFN）
4. 若記憶體極度吃緊，inference 時可**停用 KV cache**

### 預估表現：
- **MMLU Accuracy**：46-48%（E2B 為 50.9%）
- **Inference Speed**：現代 mobile GPUs 上約 50-100 tokens/sec
- **Memory Footprint**：inference 過程約 1.5-2.2 GB

---

## References

- MatFormer Paper：https://arxiv.org/abs/2310.07707
- Gemma 3n Developer Guide：https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide
- MatFormer Lab Notebook：`[Gemma_3n]MatFormer_Lab.ipynb`
- Official Slicing Configs：https://huggingface.co/datasets/google/gemma3n-slicing-configs

---

## Next Steps

若要落實這些建議：

1. 使用提議的 layer / FFN 設定，透過現有 MatFormer Lab **測試 0.9B configuration**
2. 在目標硬體（4-6GB RAM mobile devices）上**實際評估**
3. 若要支援 audio：可先提出 enhancement request，並附上建議的 tensor slicing logic
4. **回饋社群**：將最佳化 configurations 分享到 Hugging Face
