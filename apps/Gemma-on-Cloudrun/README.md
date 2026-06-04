# 將 Gemma Models 部署到 Google Cloud Run

本指南說明如何將 Google Gemma LLM 部署到 Google Cloud Run。這些預先建好的 containers 使用 Ollama 來提供 serving，並額外加入對 Google GenAI SDK 的支援。你可以直接使用現成映像，也可以針對自己的 use cases 進行微調。這些 containers 同時相容於 Google GenAI SDK 與 OpenAI SDK。

## 支援的模型與預建 Docker Images
本服務支援以下 Gemma 模型：
* gemma-3-1b-it
* gemma-3-4b-it
* gemma-3-12b-it
* gemma-3-27b-it
* gemma-3n-e2b-it
* gemma-3n-e4b-it

你也可以依照[下方章節](#部署並使用微調後的-gemma3-模型)提供自己的微調模型。

### 預建 Docker Images
為了方便使用，我們提供預建 Docker images。這些 images 已內含對應的 Gemma 模型：
* `us-docker.pkg.dev/cloudrun/container/gemma/gemma3-1b`
* `us-docker.pkg.dev/cloudrun/container/gemma/gemma3-4b`
* `us-docker.pkg.dev/cloudrun/container/gemma/gemma3-12b`
* `us-docker.pkg.dev/cloudrun/container/gemma/gemma3-27b`
* `us-docker.pkg.dev/cloudrun/container/gemma/gemma3n-e2b`
* `us-docker.pkg.dev/cloudrun/container/gemma/gemma3n-e4b`

當此目錄中的程式碼有變更時，這些 images 會透過 [Cloud Build](./cloudbuild.yaml) 自動建置並發佈。

## Quickstart - 部署到 Cloud Run
本節會帶你使用我們提供的 Docker images 部署 Cloud Run service。如果你曾從 AI Studio 將 Gemma 部署到 Cloud Run，流程會與此相同。

使用以下 `gcloud run deploy` 命令部署 Cloud Run service：
```bash
gcloud run deploy {SERVICE_NAME} \
 --image {IMAGE} \
 --concurrency 4 \
 --cpu 8 \
 --set-env-vars OLLAMA_NUM_PARALLEL=4 \
 --set-env-vars=API_KEY={YOUR_API_KEY} \
 --gpu 1 \
 --gpu-type nvidia-l4 \
 --max-instances 1 \
 --memory 32Gi \
 --allow-unauthenticated \
 --no-cpu-throttling \
 --timeout=600 \
 --region {REGION}
```

變數說明：
* `SERVICE_NAME`：你的 Cloud Run service 唯一名稱。
* `IMAGE`：要部署的 Docker image。可以是我們提供的[預建 image](#預建-docker-images)，也可以是你從本 repository 自行建置的 image。
* `YOUR_API_KEY`：**驗證用關鍵設定**。請設為你自選的一組強且唯一的 API key 字串。之後存取服務時會需要這個 key。更多細節請見下方[驗證](#驗證)章節。如果你是從 AI Studio 部署，這個值會代你產生。請注意，不應重複使用其他服務的 API key。
* `REGION`：部署 Cloud Run service 的 Google Cloud region（例如 `us-central1`）。請確認該 region 支援指定的 GPU 類型。更多資訊請見 [GPU support for Cloud Run services](https://cloud.google.com/run/docs/configuring/services/gpu)。如果你是從 AI Studio 部署，預設為 `europe-west1`。
* 其他 flag 與最佳化設定，請參考 [Run LLM inference on Cloud Run GPUs with Gemma 3 and Ollama](https://cloud.google.com/run/docs/tutorials/gpu-gemma-with-ollama#build-and-deploy)。

部署成功後，gcloud 命令會輸出 Cloud Run service URL。請將這個 URL 記下為 `<cloud_run_url>`，後續與服務互動時會用到。

## 驗證
若要快速開始，你可以使用 `--allow-unauthenticated`，讓 Cloud Run service 以公開（未驗證）方式存取。服務仍會驗證你在部署時設定的 `API_KEY` 環境變數與傳入請求是否相符。長期而言，我們建議在 Cloud Run 啟用 IAM authentication，並在 app 中使用 google-auth SDK。

### 使用 API Key
#### 設定 API Key
* Environment Variable：如部署命令所示：`--set-env-vars=API_KEY={YOUR_API_KEY}`。
* **Secret Manager（建議用於正式環境）**：
為了提升安全性，請將 API key 存放在 Google Cloud Secret Manager，並以環境變數方式暴露，例如 `--update-secrets=API_KEY={yourSecrete}:latest`。更多細節請參考 [Cloud Run Secrets documentation](https://cloud.google.com/run/docs/configuring/services/secrets#access-secrets)。

#### 在請求中使用 API Key
你必須在每個送往 Cloud Run service 的請求中帶上這個 `YOUR_API_KEY`，如下方[與服務互動](#與-cloud-run-service-互動)章節所示。

### 使用 IAM Authentication（建議）
正式環境應將 Cloud Run service 設定為使用 IAM Authentication。你可以重新部署 Cloud Run service，加入 `--no-allow-unauthenticated` flag 來啟用。請注意，這會要求你修改應用程式程式碼，確保傳入請求帶有正確的 identity token。
更多 IAM authentication 與 Cloud Run 的資訊，請參考 [Authenticating service-to-service](https://cloud.google.com/run/docs/authenticating/service-to-service#use_the_authentication_libraries)。

## 與 Cloud Run Service 互動
當 Cloud Run service 部署完成後，你可以使用 curl、Google GenAI SDK，或 OpenAI SDK 與其互動。

GenAI API endpoints：
* [`/v1beta/{model=models/*}:generateContent`](https://ai.google.dev/api/generate-content#method:-models.generatecontent) - 在輸入 GenerateContentRequest 後，產生模型回應。
* [`/v1beta/{model=models/*}:streamGenerateContent`](https://ai.google.dev/api/generate-content#method:-models.streamgeneratecontent) - 在輸入 GenerateContentRequest 後，產生串流式模型回應。

OpenAI API endpoint：
* 另外也提供 OpenAI 相容端點 `/v1/chat/completions`。

佔位符說明：
* `<cloud_run_url>`：你部署完成的 Cloud Run service URL。
* `<YOUR_API_KEY>`：你在部署時設定的 API key。
* `<model>`：你部署的模型名稱（例如 `gemma-3-1b-it`、`gemma-3-4b-it`，或你的自訂微調模型名稱）。

### 1. 使用 curl：

Generate Content
```bash
curl "<cloud_run_url>/v1beta/models/<model>:generateContent?key={YOUR_API_KEY}" \
   -H 'Content-Type: application/json' \
   -X POST \
   -d '{
     "contents": [{
       "parts":[{"text": "Write a story about a magic backpack. You are the narrator of an interactive text adventure game."}]
       }]
      }'
```

Stream Generate Content
```bash
curl "<cloud_run_url>/v1beta/models/<model>:streamGenerateContent?key={YOUR_API_KEY}" \
   -H 'Content-Type: application/json' \
   -X POST \
   -d '{
     "contents": [{
       "parts":[{"text": "Write a story about a magic backpack. You are the narrator of an interactive text adventure game."}]
       }]
      }'
```

### 2. 使用 Google GenAI SDK（Python）

更多細節請參考[官方 GenAI SDK 文件](https://ai.google.dev/gemini-api/docs/libraries)。

#### 2.1 安裝 GenAI SDK
```
pip install --upgrade google-genai
```

#### 2.2 Python 範例：
```python
from google import genai
from google.genai.types import HttpOptions

# Configure the client to use your Cloud Run endpoint and API key
client = genai.Client(api_key="<YOUR_API_KEY>", http_options=HttpOptions(base_url="<cloud_run_url>"))


# Example: Generate content (non-streaming)
response = client.models.generate_content(
   model="<model>", # Example: "gemma-3-4b-it" or your custom model name
   contents=["How does AI work?"]
)
print(response.text)


# Example: Stream generate content
response = client.models.generate_content_stream(
   model="<model>", # Example: "gemma-3-4b-it" or your custom model name
   contents=["Write a story about a magic backpack. You are the narrator of an interactive text adventure game."]
)
for chunk in response:
   print(chunk.text, end="")
```

### 3. 使用 OpenAI API 與 SDK

#### 3.1 Python 程式範例

更多細節請參考[官方 OpenAI SDK 文件](https://platform.openai.com/docs/libraries#install-an-official-sdk)。

```bash
pip install openai
```

```python
from openai import OpenAI

# Configure the OpenAI client to point to your Cloud Run endpoint
openAIclient = OpenAI(
   api_key="<YOUR_API_KEY>",
   base_url="<cloud_run_url>/v1" # Note: Add /v1 to the base_url
)

completion = openAIclient.chat.completions.create(
   model="<model>", # Example: "gemma3:4b" or your custom model name
   messages=[
     {
       "role": "developer",
       "content": "You are a helpful assistant."
     },
     {
       "role": "user",
       "content": "Hello!"
     }
   ]
)

print(completion.choices[0].message.content)
```

#### 3.2 `curl` 範例（OpenAI 相容）
```bash
curl <cloud_run_url>/v1/chat/completions \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer <YOUR_API_KEY>" \
 -d '{
   "model": "<model>",
   "messages": [
     {
       "role": "developer",
       "content": "You are a helpful assistant."
     },
     {
       "role": "user",
       "content": "Hello!"
     }
   ]
 }'
```

### 4. 使用 Ollama SDK

#### 4.1 Python 程式範例

更多細節請參考 [Ollama libraries documentation](https://github.com/ollama/ollama?tab=readme-ov-file#libraries)。

```bash
pip install ollama
```

```python
from ollama import Client
from ollama import chat

client = Client(
  host='<cloud_run_url>',
  headers={'Authorization': 'Bearer <YOUR_API_KEY>'}
)

# Example: non-streaming
response = client.chat(
    model='<model>', # Example: "gemma3:4b" or your custom model name
    messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
])

print(response['message']['content'])

# Example: streaming
stream = client.chat(
    model='<model>', # Example: "gemma3:4b" or your custom model name
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
```

## 部署並使用微調後的 Gemma3 模型

本節說明如何使用 Cloud Run service 部署並使用你自己的自訂微調 Gemma 模型。這個流程包括建立自訂 Ollama 模型、將其組件上傳到 GCS，以及把該 GCS bucket 掛載到你的 Cloud Run service。

步驟如下：

#### 1. 在本機使用 Ollama 自訂模型：

依照 https://github.com/ollama/ollama?tab=readme-ov-file#customize-a-model 的說明，在 Modelfile 中匯入 GGUF model，並於 Ollama 中建立模型
```bash
ollama create <your-custom-model-name> -f Modelfile
```
這個命令會處理你的 GGUF 檔案，並在你的[本機 Ollama models directory](https://github.com/ollama/ollama/blob/main/docs/faq.md#where-are-models-stored) 中建立 Ollama 所需的 blobs 與 manifests。

#### 2. 找出並上傳 Ollama 模型檔到 GCS：

切換到你的[本機 Ollama models directory](https://github.com/ollama/ollama/blob/main/docs/faq.md#where-are-models-stored)。你會看到 `blobs/` 與 `manifests/` 子目錄，裡面就是新建立自訂模型的組件。

請將自訂模型產生的內容，上傳到 GCS bucket 中對應的 `blobs/` 與 `manifests/` 子目錄。這樣才能保持 Ollama 可辨識的正確結構。

例如：
```bash
cd <your-local-ollama-model-dir>
gcloud storage cp --recursive . gs://YOUR_MODEL_BUCKET_NAME
```

#### 3. 以 GCS Volume Mount 部署 Cloud Run Service

```bash
gcloud run deploy {SERVICE_NAME} \
 --image {IMAGE} \
 --concurrency 4 \
 --cpu 8 \
 --set-env-vars OLLAMA_NUM_PARALLEL=4 \
 --set-env-vars=API_KEY={YOUR_API_KEY} \
 --gpu 1 \
 --gpu-type nvidia-l4 \
 --max-instances 1 \
 --memory 32Gi \
 --allow-unauthenticated \
 --no-cpu-throttling \
 --timeout=600 \
 --region {REGION} \
 --add-volume name={VOLUME_NAME},type=cloud-storage,bucket={YOUR_MODEL_BUCKET_NAME} \
 --add-volume-mount volume={VOLUME_NAME},mount-path=/models
```

變數說明：
* `VOLUME_NAME`：你的 volume 名稱（例如 `my-gemma-volume`）。
* `YOUR_MODEL_BUCKET_NAME`：你的 GCS bucket 名稱。

其中 `{IMAGE}` 有兩種選擇：

Option A：使用預建 image 並掛載 GCS（建議，最省事）：

你可以直接使用我們的[預建 image](#預建-docker-images)（內含 baked-in models）。當你將 GCS bucket 掛載到 `/models` 時，GCS bucket 的內容會覆蓋並取代原本 image 在該路徑內建的模型。因此服務會改以 GCS 中的自訂模型為主。

Option B：自行建置 image（不內建模型）並掛載 GCS：

如果你想要更小的 Docker image，或希望完全掌控 image 內容，可以依照我們的 [Dockerfile](./Dockerfile) 自行建置。這種情況下，你會移除 Dockerfile 中的 `ollama pull` 命令，確保 image 不內建任何模型，接著再搭配 GCS volume mount 部署這個自訂 image。

```
# Example Dockerfile snippet (within your build stage)
# ... (other instructions) ...
# Store model weight files in /models (this is where the GCS volume will be mounted)
ENV OLLAMA_MODELS /models
# REMOVE THIS LINE:
# RUN /bin/ollama serve & sleep 5 && ollama pull $MODEL
# ... (rest of your Dockerfile) ...
```
之後再[建置你的自訂 image](https://cloud.google.com/run/docs/building/containers#use-dockerfile)。

#### 4. 與你的自訂模型互動：
現在，你可以像使用預建模型一樣，在 API 請求中指定 `<your-custom-model-name>`（也就是你在 `ollama create` 時使用的名稱）來使用自訂微調模型。

```python
from google import genai
from google.genai.types import HttpOptions

client = genai.Client(api_key="<YOUR_API_KEY>", http_options=HttpOptions(base_url="<cloud_run_url>"))

response = client.models.generate_content_stream(
   model="<your-custom-model-name>", # Use the name you defined in ollama create
   contents=["Write a story about a magic backpack. You are the narrator of an interactive text adventure game."]
)
for chunk in response:
   print(chunk.text, end="")
```
對於 OpenAI SDK 與 curl 範例，也只要把 `<model>` 替換成 `<your-custom-model-name>` 即可。
