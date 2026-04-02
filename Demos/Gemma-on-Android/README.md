#### 由 [Aashi Dutt](https://linkedin.com/in/aashi-dutt) 與 [Nitin Tiwari](https://linkedin.com/in/tiwari-nitin) 開發。

# Gemma on Android
這個專案示範如何在自訂資料集上微調 Gemma 2b-it 模型，並將微調後的模型部署到 Android。


## Pipeline:

![Logo](assets/SciGemma_Pipeline.gif)


## Demo Output:

![Logo](assets/SciGemma.gif)


## 執行步驟：

1. 在本機複製這個 repository。
2. 使用 Android Studio 開啟專案。
3. 編輯 **Line 44** 的 `InferenceModel.kt` 檔案，將 `YOUR_MODE_NAME.bin` 替換為你的實際模型名稱。
4. 建置專案。
5. 將 Android app 安裝到手機上，開始使用 SciGemma。



## 資源：

1. 可搭配閱讀以下三篇 blog series，深入了解程式碼細節：

   Part 1: [Step-by-Step Dataset Creation- Unstructured to Structured](https://aashi-dutt3.medium.com/part-1-step-by-step-dataset-creation-unstructured-to-structured-70abdc98abf0)

   Part 2: [Fine Tune - Gemma 2b-it model](https://aashi-dutt3.medium.com/part-2-fine-tune-gemma-2b-it-model-a26246c530e7)

   Part 3: [Deploying SciGemma on Android](https://tiwarinitin1999.medium.com/part-3-deploy-gemma-on-android-5bac532c54b7)

3. 在 🤗 上的微調模型：https://huggingface.co/NSTiwari/fine_tuned_science_gemma2b-it

4. 在 HFSpaces 試用模型：[https://huggingface.co/spaces/Aashi/NSTiwari-fine_tuned_science_gemma2b-it?logs=container](https://huggingface.co/spaces/Aashi/NSTiwari-fine_tuned_science_gemma2b-it)

5. 在 YouTube 觀看 demo 影片：https://www.youtube.com/watch?v=T_HDsVHTrwg
