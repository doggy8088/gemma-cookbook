### 由 [Nitin Tiwari](https://linkedin.com/in/tiwari-nitin) 開發。

# 使用 ONNX & Transformers.js 在瀏覽器上推論PaliGemma 2
此專案是使用轉換後的 ONNX 權重和 Hugging Face Transformers.js 在瀏覽器上推論 paligemma2-3b-mix-224 模型的實作。
## PaliGemma 2 至 ONNX 轉換：
![Logo](assets/paligemma2-onnx-pipeline.png)


## 執行步驟：

1. 將儲存庫克隆到本機上。
2. 導航至`gemma-cookbook/Demos/PaliGemma2-on-Web` 目錄。
3. 執行 `npm install` 安裝 Node.js 套件。
4. 執行`node server.js`來啟動伺服器。
5. 在網頁瀏覽器上開啟`localhost:3000`並使用PaliGemma 2開始推論。

> [！筆記]
> 第一次載入模型權重大約需要 10-15 分鐘。

## 結果：
![Logo](assets/paligemma2-onnx-output.gif)


## 資源和參考資料

1. [Google DeepMind PaliGemma 2](https://developers.googleblog.com/en/introducing-paligemma-2-mix/)
2. Colab notebook：
<table> <tr>    <td><b>Convert and quantize PaliGemma 2 to ONNX</b></td>
    <td><a target="_blank" href="https://colab.research.google.com/github/NSTiwari/PaliGemma2-ONNX-Transformers.js/blob/main/Convert_PaliGemma2_to_ONNX.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
</tr> <tr>    <td><b>Inference PaliGemma 2 with Transformers.js</b></td>
    <td><a target="_blank" href="https://colab.research.google.com/github/NSTiwari/PaliGemma2-ONNX-Transformers.js/blob/main/Inference_PaliGemma2_with_Transformers_js.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></td>
</tr>
</table>
3. [**Medium Blog**](https://medium.com/@tiwarinitin1999/inference-paligemma-2-with-transformers-js-5545986ac14a) 用於逐步實施。
4. [ONNX 社群](https://huggingface.co/onnx-community)
