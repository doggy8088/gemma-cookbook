# 展示複雜端到端使用案例

這個資料夾收錄 "Build with AI" 影片系列的配套 notebooks，以及行動 app demo 的程式碼範例。你可以在這裡找到實用範例與可直接執行的程式碼，幫助你把 AI 驅動功能真正做出來。

## "Build with AI" 影片系列配套 notebooks
| Folder                                                      | Description |
| ----------------------------------------------------------- | ----------- |
| [Business email assistant](business-email-assistant/) | [Business Email AI Assistant with Gemma](https://www.youtube.com/watch?v=YxhzozLH1Dk)<br>這個專案聚焦於從寄給烘焙坊的 email 中擷取訂單資訊，轉成結構化資料，以便快速匯入訂單處理系統。 |
| [Personal code assistant](personal-code-assistant/)   | [Personal AI Code Assistant with Gemma](https://www.youtube.com/watch?v=Zpo7UTvg_9E)<br>這個專案示範如何建立自己的 Gemma web service，並將其連接到 Microsoft Visual Studio Code extension，讓你在撰寫程式時更方便使用模型。 |
| [Spoken language tasks](spoken-language-tasks/)       | [Spoken Language AI Assistant with Gemma](https://www.youtube.com/watch?v=M4HGJehH4r0)<br>了解如何在不需要大量資料或長時間訓練的前提下，將模型調整為能在特定語言中執行特定任務。 |

## 行動 App Demo
| Folder                                                      | Description |
| ----------------------------------------------------------- | ----------- |
| [Gemma on Android](Gemma-on-Android/)         | 使用 MediaPipe LLM Inference API 部署經微調的 Gemma-2B-it 模型的 Android app。 |
| [PaliGemma on Android](PaliGemma-on-Android/) | 透過 Hugging Face 與 Gradio Client API 在 Android 上對 PaliGemma 執行推論，用於 zero-shot object detection、image captioning 與 visual question-answering 等任務。 |

## Web App Demo
| Folder                                                      | Description |
| ----------------------------------------------------------- | ----------- |
| [PaliGemma 2 on Web](PaliGemma2-on-Web/)         | 使用其 ONNX weights 與 Transformers.js 在網頁端對 PaliGemma 2 執行推論，用於 object detection、image captioning、OCR 與 visual Q&A 等任務。 |
| [Gemma 3 on Web](Gemma3-on-Web/)         | 在網頁上以 ONNX weights 與 Transformers.js 執行 Gemma 3 270M 模型，重點涵蓋 chat 能力與 system prompt 自訂。 |
| [Emoji Gemma on Web](Emoji-Gemma-on-Web/)  | 了解如何將 Gemma 3 270M 模型微調為 emoji translation 用途，並使用 MediaPipe LLM Inference API 或 Transformers.js 在瀏覽器端執行。 |

## Cloud Run Demo
| Folder                                                      | Description |
| ----------------------------------------------------------- | ----------- |
| [Gemma on Cloud run](Gemma-on-Cloudrun/)         | 這個資料夾包含用於建置與部署 Gemma 驅動應用到 Cloud Run 的 Dockerfile，並整合 Gemini APIs。 |
