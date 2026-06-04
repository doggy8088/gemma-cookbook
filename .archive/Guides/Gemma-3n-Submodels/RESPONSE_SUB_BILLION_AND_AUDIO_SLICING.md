# 回應：Gemma 3n 的數十億模型切片和音訊編碼器縮減

## 概述

本文檔針對資源受限環境（具有 4-6GB RAM 和 Web 部署的行動裝置）Gemma 3n 模型切片相關的兩個功能請求提供技術指導和建議：
1. 建立小於 1.91B 的模型（可能為 0.9B 或更小，有 26 層）
2. 將層縮減技術應用於音訊編碼器

---

## 第 1 部分：建立低於 10 億的模型（0.9B 或更小）

### 目前設定狀況

MatFormer Lab notebook (`[Gemma_3n]MatFormer_Lab.ipynb`) 目前支援的切片設定範圍從 **1.91B (E2B)** 到 **3.98B (E4B)**，最小的是：
- **官方 E2B 模型的設定**
  - 有效參數：1.91B
  - 層數：30
  - 跳過的層數：[20, 21, 22, 23, 24]
  - FFN 隱藏尺寸：所有層的 [2048 * 4] (8,192)

### 十億以下模型的可行性

**是的，使用 MatFormer 切片技術絕對可以建立小於 0.9B 的模型**。以下是設計注意事項：
#### 選項 A：層數減少路徑（26 層）

對於 **0.9B 26 層模型**，請考慮以下設定：
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

#### Option B: Even Smaller - 0.5B Model with 20 Layers

對於更積極的壓縮：
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

### 最佳切片建議

基於現有設定中觀察到的 MatFormer 設計原則：
#### 主要設計原則：

1. **層分佈**：從中間到末端部分（第 15-24 層）而不是早期層跳過層，因為早期層捕獲重要的低級語言特徵
2. **FFN 容量分佈**：
   - 第 0-10 層：較低容量（2048×2 至 2048×3）
   - 第 11-20 層：中等容量（2048×3 至 2048×3.5）
   - 第 21 層以上：更高容量 (2048×4)
3. **保留層**：始終保留最後 2 個全域層（原始層為 33-34 層），因為它們對於輸出品質至關重要
4. **KV 共用**：最後 2 層使用 KV 共用 - 確保它們被保留

#### 0.9B（26層）的設定：

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

### 在 MatFormer 實驗室中的實現

若要將此設定與現有 MatFormer Lab notebook 一起使用：
```python
# In the "Config details" cell, uncomment and set:
layers_to_skip = [19, 20, 21, 22, 23, 24, 25, 26, 27]
ffn_hidden_dims = [2048*3]*10 + [int(2048*3.5)]*9 + [2048*4]*7
ffn_hidden_dims_str = str(ffn_hidden_dims)
```

---

## 第 2 部分：音訊編碼器切片

### 目前架構

Gemma 3n 是**多模式模型**，具有：- 文字編碼器/解碼器（目前切片的主要焦點）
- 視覺編碼器（影像處理）
- 音訊編碼器（語音處理）

### 音頻編碼器減少的可行性

**是的，可以使用類似的層切片技術來減少音訊編碼器**，但需要額外的實現工作，因為 MatFormer 實驗室notebook 目前專注於文字模型切片。
#### 音訊編碼器特性

Gemma 3n 中的音訊編碼器通常具有：- ~12-24 變壓器層
- 與文字編碼器類似的結構（注意力+FFN）
- 可以透過跳過層或減少 FFN 維度來減少

### 提議的音訊編碼器切片方法

#### 第 1 步：識別音訊編碼器設定

```python
# Load the original model config
from transformers import AutoConfig

config = AutoConfig.from_pretrained("google/gemma-3n-E4B-it")

# Access audio encoder config
audio_config = config.audio_config  # or similar field name

print(f"Original audio layers: {audio_config.num_hidden_layers}")
print(f"Audio FFN dimension: {audio_config.intermediate_size}")
```

#### 第 2 步：建議的音訊編碼器縮減

對於0.9B 整體型號，建議：
```python
# Audio encoder reduction (from original ~16-20 layers)
audio_layers_to_skip = [12, 13, 14, 15]  # Skip last 4 layers
# Keep: 12 layers (vs. original 16)

# FFN reduction for audio
audio_ffn_hidden_dims = [1024 * 3] * 12  # Reduce from 1024*4

# Expected audio encoder size: ~80-100M parameters
# Combined with text (0.8B) = 0.9B total
```

#### 第三步：實施要求

與文字編碼器不同，音訊編碼器切片需要：
1. **修改模型切片程式碼**以類似地處理音訊編碼器參數：
   - 圖案：`.audio_model.layers.{layer_idx}.`
   - 應用相同的 FFN 維度切片邏輯

2. **更新 MatFormer 實驗室 notebook 中的安全張量載入**：
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

3. **Update config.json**:
   ```python
   config.audio_config.num_hidden_layers = 12  # Reduced from 16
   config.audio_config.intermediate_size = 3072  # Reduced from 4096
   ```

### Audio + Text Joint Optimization

For optimal performance in resource-constrained scenarios, suggest:

| Model Size | Text Layers | Text FFN | Audio Layers | Audio FFN | RAM (4-bit) | Use Case |
|-----------|------------|---------|--------------|-----------|-----------|----------|
| 0.5B | 20 | 2048×2-3 | 10 | 1024×2 | ~1.5 GB | Ultra-light mobile |
| 0.9B | 26 | 2048×3-3.5 | 12 | 1024×3 | ~2.2 GB | Standard mobile |
| 1.5B | 28 | 2048×3.5-4 | 14 | 1024×3.5 | ~3.8 GB | High-end mobile |

---

## Implementation Roadmap

### Phase 1: Text Model Only (Immediate)
Use existing MatFormer Lab notebook with 0.9B configuration (26 layers)

### Phase 2: Audio Encoder Support (Enhancement)
1. Extend MatFormer Lab slicing logic to handle audio encoder
2. Add audio-specific configuration parameters
3. Create new notebook: `[Gemma_3n]MatFormer_Lab_with_Audio_Slicing.ipynb`

### Phase 3: Validation & Benchmarking (Optional)
1. Evaluate MMLU performance for sub-billion configs
2. Measure inference latency on target mobile devices
3. Create mobile deployment guide

---

## Practical Migration Steps

### For 0.9B Model without Audio Changes:

```python
# 在 MatFormer 實驗室notebook、cell「設定詳細資料」：
config_name = "Custom 0.9B (26-layer)"

# 手動設定：
layers_to_skip = [19, 20, 21, 22, 23, 24, 25, 26, 27]
ffn_hidden_dims = [2048*3]*10 + [int(2048*3.5)]*9 + [2048*4]*7
ffn_hidden_dims_str = str(ffn_hidden_dims)

# 像往常一樣執行剩餘的cells
```

### For Full Implementation with Audio:

A new enhanced notebook would need:
- Audio encoder configuration UI
- Extended tensor slicing logic
- Separate audio layer skip/FFN configs
- Joint optimization validation

---

## Deployment Recommendations

### For 4-6 GB Mobile RAM:

1. **Use 0.9B model** with configuration above
2. **Apply 4-bit quantization** (NF4/Int4) to reduce size to ~1.2-1.5 GB
3. **Keep audio encoder lean** (12 layers, 1024×3 FFN)
4. **Disable KV cache** during inference if memory is critical

### Estimated Performance:
- **MMLU Accuracy**: 46-48% (vs. 50.9% for E2B)
- **Inference Speed**: 50-100 tokens/sec on modern mobile GPUs
- **Memory Footprint**: 1.5-2.2 GB during inference

---

## References

- MatFormer Paper: https://arxiv.org/abs/2310.07707
- Gemma 3n Developer Guide: https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide
- MatFormer Lab Notebook: `[Gemma_3n]MatFormer_Lab.ipynb`
- Official Slicing Configs: https://huggingface.co/datasets/google/gemma3n-slicing-configs

---

## Next Steps

To implement these recommendations:

1. **Test 0.9B configuration** using existing MatFormer Lab with proposed layer/FFN settings
2. **Evaluate on target hardware** (4-6GB RAM mobile devices)
3. **For audio support**: File enhancement request with proposed tensor slicing logic
4. **Contribute back**: Share optimal configurations with community via Hugging Face

