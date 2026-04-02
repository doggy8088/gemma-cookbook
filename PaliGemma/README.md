# PaliGemma

這個資料夾依照主題分成數個分類，每一類都聚焦於使用 PaliGemma 模型的特定面向：

* [推論](#推論) : 如何載入並執行 PaliGemma 模型以進行推論
* [微調](#微調) : 深入了解如何針對特定任務與領域微調 PaliGemma 模型

## 推論
| Notebook Name | Description |
| :----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[PaliGemma_1]Common_use_cases.ipynb]([PaliGemma_1]Common_use_cases.ipynb)                                                       | 說明 PaliGemma 的一些常見使用案例。 |
| [[PaliGemma_1]Image_captioning.ipynb]([PaliGemma_1]Image_captioning.ipynb)                                                       | 使用 Keras 與 PaliGemma 生成圖片說明。 |
| [[PaliGemma_1]Referring_expression_segmentation_in_images.ipynb]([PaliGemma_1]Referring_expression_segmentation_in_images.ipynb) | 使用 PaliGemma 在圖片中進行 referring expression segmentation。 |
| [[PaliGemma_1]Referring_expression_segmentation_in_videos.ipynb]([PaliGemma_1]Referring_expression_segmentation_in_videos.ipynb) | 使用 PaliGemma 在影片中進行 referring expression segmentation。 |
| [[PaliGemma_1]Using_with_Mesop.ipynb]([PaliGemma_1]Using_with_Mesop.ipynb)                                                           | 將 PaliGemma 與 [Google Mesop](https://google.github.io/mesop/) 整合。 |
| [[PaliGemma_1]Zero_shot_object_detection_in_images.ipynb]([PaliGemma_1]Zero_shot_object_detection_in_images.ipynb)               | 使用 PaliGemma 在圖片中進行 zero-shot object detection。 |
| [[PaliGemma_1]Zero_shot_object_detection_in_videos.ipynb]([PaliGemma_1]Zero_shot_object_detection_in_videos.ipynb)               | 使用 PaliGemma 在影片中進行 zero-shot object detection。 |
| [[PaliGemma_2]Convert_PaliGemma2_to_ONNX.ipynb]([PaliGemma_2]Convert_PaliGemma2_to_ONNX.ipynb)                                                     | 將 PaliGemma 2 轉換並量化為 ONNX 格式，使其可搭配 Transformers.js 進行推論。 |
| [[PaliGemma_2]Inference_PaliGemma2_with_Transformers_js.ipynb]([PaliGemma_2]Inference_PaliGemma2_with_Transformers_js.ipynb)                                                     | 使用 Transformers.js 對 PaliGemma 2 進行推論，用於 image captioning、zero-shot object detection、OCR 與 visual Q&A 等任務。 |
| [[PaliGemma_2]Keras_Quickstart.ipynb]([PaliGemma_2]Keras_Quickstart.ipynb)                                                              | 使用 Keras 的 PaliGemma 2 3B DOCCI 模型快速開始教學 |
| [[PaliGemma_2]Using_with_Transformersjs.ipynb]([PaliGemma_2]Using_with_Transformersjs.ipynb)                                                         | 使用 Transformers.js 執行 PaliGemma 2。 |

## 微調
| Notebook Name | Description |
| :----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[PaliGemma_1]Finetune_with_Keras.ipynb]([PaliGemma_1]Finetune_with_Keras.ipynb)                                                             | 使用 Keras 微調 PaliGemma。 |
| [[PaliGemma_1]Finetune_with_image_captioning.ipynb]([PaliGemma_1]Finetune_with_image_captioning.ipynb)                                   | 使用 [Hugging Face](https://huggingface.co/) 比較不同 PaliGemma 版本的 image captioning 結果。 |
| [[PaliGemma_1]Finetune_with_image_description.ipynb]([PaliGemma_1]Finetune_with_image_description.ipynb)                                       | 使用 [JAX](https://github.com/google/jax) 為圖片描述任務微調 PaliGemma。 |
| [[PaliGemma_1]Finetune_with_object_detection.ipynb]([PaliGemma_1]Finetune_with_object_detection.ipynb)                                       | 使用 [JAX](https://github.com/google/jax) 在 fashion dataset 上為 object detection 任務微調 PaliGemma。 |
| [[PaliGemma_2]Finetune_with_JAX.ipynb]([PaliGemma_2]Finetune_with_JAX.ipynb)                                                         | 使用 JAX 微調 PaliGemma 2。 |
| [[PaliGemma_2]Finetune_with_Keras.ipynb]([PaliGemma_2]Finetune_with_Keras.ipynb)                                                     | 使用 Keras 微調 PaliGemma 2。 |
