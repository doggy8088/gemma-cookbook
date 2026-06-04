# 將Gemma模型部署至Google Cloud執行

本指南向您展示如何將 Google Gemma LLM 部署到 Google Cloud Run。這些預先建置的容器利用 Ollama 進行服務，並額外支援 Google GenAI SDK 。使用現成的，或根據您自己的用例進行微調。 這些容器相容於Google GenAI SDK 和OpenAI SDK。
## 支援的模型和預先建置的 Docker 映像
我們的服務支援以下Gemma型號：* 傑瑪-3-1b-it
* 傑瑪-3-4b-it
* 傑瑪-3-12b-it
* 傑瑪-3-27b-it
* 傑瑪-3n-e2b-it
* 寶石-3n-e4b-it

您可以按照[下面的部分]提供您自己的微調模型(#deploying-and-using-fine-tuned-gemma3-models)
### 預先建置的 Docker 映像
為了方便起見，我們提供預先建造的 Docker images。這些圖像捆綁了各自的 Gemma 型號：* `us-docker.pkg.dev/cloudrun/container/gemma/gemma3-1b`
* `us-docker.pkg.dev/cloudrun/container/gemma/gemma3-4b`
* `us-docker.pkg.dev/cloudrun/container/gemma/gemma3-12b`
* `us-docker.pkg.dev/cloudrun/container/gemma/gemma3-27b`
* `us-docker.pkg.dev/cloudrun/container/gemma/gemma3n-e2b`
* `us-docker.pkg.dev/cloudrun/container/gemma/gemma3n-e4b`

當此目錄中的程式碼發生變更時，這些映像會使用 [Cloud Build](./cloudbuild.yaml) 自動建置和發布。
## 快速入門 - 部署至Cloud Run
本部分將引導您使用我們提供的Docker images 部署Cloud Run 服務。 如果您已從 AI Studio 將 Gemma 部署到 Cloud Run，它會反映此過程。
使用以下 `gcloud run deploy` 指令部署 Cloud Run 服務：```bash
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

變數解釋：* `SERVICE_NAME`：Cloud Run 服務的唯一名稱。
* `IMAGE`：要部署的Docker image。這可以是我們的[預先建置映像](#pre-built-docker-images) 之一，也可以是您從該儲存庫自行建立的映像
* `YOUR_API_KEY`：**對於身份驗證至關重要**。將其設定為您選擇的強大且唯一的 API 金鑰字串。需要此密鑰才能存取您的服務。有關更多詳細信息，請參閱下面的[身份驗證](#authentication) 部分。如果您從 AI Studio 進行部署，則會代表您產生。請注意，這不應該是從其他服務重複使用的 API 金鑰。
* `REGION`：將部署 Cloud Run 服務的 Google Cloud 區域（例如 us-central1）。確保該區域支援指定的 GPU 類型。有關更多詳細信息，請參閱[Cloud Run 服務的 GPU 支援](https://cloud.google.com/run/docs/configuring/services/gpu)。 如果您從 AI Studio 進行部署，則預設為 europe-west1。
* 有關其他標誌和最佳化設置，請參閱[使用 Gemma 3 和 Ollama 在 Cloud Run GPU 上執行 LLM inference](https://cloud.google.com/run/docs/tutorials/gpu-gemma-with-ollama#build-and-deploy) 以了解更多詳細資訊。

部署成功後，gcloud 指令將輸出 Cloud Run 服務 URL。將此 URL 儲存為 `<cloud_run_url>` 與您的服務互動。
## 驗證
要快速開始，您可以使用 `--allow-unauthenticated` 部署具有公共（未經身份驗證）存取的 Cloud Run 服務。 本服務將根據傳入請求驗證您在部署期間設定的 `API_KEY` 環境變數。從長遠來看，我們建議在 Cloud Run 中啟用 IAM 身份驗證並使用 google-auth SDK 更新您的應用程式。
### 使用 API 鍵
#### 設定API鍵
* 環境變數：如部署指令所示：`--set-env-vars=API_KEY={YOUR_API_KEY}`。
* **Secret Manager（建議用於生產）**：
為了增強安全性，請將 API 金鑰儲存在 Google Cloud Secret Manager 中，並將其公開為環境變數 `--update-secrets=API_KEY={yourSecrete}:latest`。有關更多詳細信息，請參閱 [Cloud Run Secrets 文件](https://cloud.google.com/run/docs/configuring/services/secrets#access-secrets)。
#### 在請求中使用 API 鍵
您需要在對Cloud Run 服務的每個請求中包含此`YOUR_API_KEY`，如[與服務互動](#interacting-with-the-cloud-run-service) 部分所示。
### 使用 IAM 身份驗證（建議）
對於生產，您應該設定 Cloud Run 服務以使用 IAM 驗證。 您可以通过使用 `--no-allow-unauthenticated` 标志重新部署 Cloud Run 服务来启用此功能。 請注意，這將需要更改您的應用程式程式碼，以確保傳入請求傳遞適當的身份token。
要了解有關 IAM 身份驗證和 Cloud Run 的更多信息，請參閱[對服務進行身份驗證](https://cloud.google.com/run/docs/authenticating/service-to-service#use_the_authentication_libraries)。
## 與 Cloud Run 服務交互
一旦部署了Cloud Run 服務，您就可以使用 curl、Google 的 GenAI SDK 或 OpenAI 的 SDK 與其進行互動。
GenAI API 端點：* [`/v1beta/{model=models/*}:generateContent`](https://ai.google.dev/api/generate-content#method:-models.generatecontent) - 給定輸入 GenerateContentRequest 產生模型回應。
* [`/v1beta/{model=models/*}:streamGenerateContent`](https://ai.google.dev/api/generate-content#method:-models.streamgeneratecontent) - 在給定輸入 GenerateContentRequest 的情況下從模型產生串流回應。

OpenAI API 端點：* 此外，`/v1/chat/completions` 也提供 OpenAI 相容端點。

佔位符：* `<cloud_run_url>`：您部署的Cloud Run 服務的 URL。
* `<YOUR_API_KEY>`：您在部署期間設定的API 金鑰。
* `<model>`：您部署的模型名稱（例如 gemma-3-1b-it、gemma-3-4b-it 或您微調的模型名稱）。

### 1.使用捲曲：

產生內容```bash
curl "<cloud_run_url>/v1beta/models/<model>:generateContent?key={YOUR_API_KEY}" \
   -H 'Content-Type: application/json' \
   -X POST \
   -d '{
     "contents": [{
       "parts":[{"text": "Write a story about a magic backpack. You are the narrator of an interactive text adventure game."}]
       }]
      }'
```

串流生成內容```bash
curl "<cloud_run_url>/v1beta/models/<model>:streamGenerateContent?key={YOUR_API_KEY}" \
   -H 'Content-Type: application/json' \
   -X POST \
   -d '{
     "contents": [{
       "parts":[{"text": "Write a story about a magic backpack. You are the narrator of an interactive text adventure game."}]
       }]
      }'
```

### 2. 使用Google GenAI SDK (Python)

更多詳情請參考【GenAI SDK 官方文件】(https://ai.google.dev/gemini-api/docs/libraries)。
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

### 3. 使用 OpenAIAPI和 SDK

#### 3.1 Python 程式碼範例

有關更多詳細信息，請參閱[官方 OpenAI SDK 文件](https://platform.openai.com/docs/libraries#install-an-official-sdk)。
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

#### 3.2 `curl`範例（相容 OpenAI）
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

### 4.使用Ollama SDK

#### 4.1 Python 程式碼範例

有關更多詳細信息，請參閱 [Ollama 庫文檔](https://github.com/ollama/ollama?tab=readme-ov-file#libraries)。
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

## 部署與使用微調Gemma3模型

本節詳細介紹如何透過Cloud Run 服務部署和使用您自己的自訂微調Gemma 模型。這涉及建立自訂 Ollama 模型、將其元件上傳到 GCS，以及將該 GCS bucket 安裝到您的 Cloud Run 服務。
步驟：
#### 1. 在本地使用 Ollama 自訂模型：

依照https://github.com/ollama/ollama?tab=readme-ov-file#customize-a-model在 Modelfile 中導入 GGUF 模型，並在Ollama中建立模型```bash
ollama create <your-custom-model-name> -f Modelfile
```
此命令將處理您的 GGUF 文件，並在您的[本地 Ollama 模型目錄](https://github.com/ollama/ollama/blob/main/docs/faq.md#where-are-models-stored) 中為Ollama 建立必要的 blob 和清單。
#### 2. 找到 Ollama 模型檔案並上傳到 GCS：

导航到您的[本地 Ollama 模型目录](https://github.com/ollama/ollama/blob/main/docs/faq.md#where-are-models-stored)。您將找到`blobs/` 和`manifests/` 子目錄。它们包含新创建的自定义模型的组件。
將為自訂模型產生的內容上傳至 GCS bucket 對應的 `blobs/` 和 `manifests/` 子目錄。這將確保 Ollama 的結構正確以找到您的型號。
例如，```bash
cd <your-local-ollama-model-dir>
gcloud storage cp --recursive . gs://YOUR_MODEL_BUCKET_NAME
```

#### 3. 使用 GCS 卷掛載部署Cloud Run服務

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

變數解釋：* `VOLUME_NAME`：磁碟區的名稱（例如 my-gemma-volume）。
* `YOUR_MODEL_BUCKET_NAME`：您的 GCS bucket 的名稱。

請注意，`{IMAGE}` 有兩個選項：
選項 A：使用 GCS 安裝的預先建置映像（為方便起見，建議）：
您可以使用我們的[預先建構影像](#pre-built-docker-images) 之一（其中包含烘焙模型）。當您將 GCS bucket 安裝到 `/models` 時，GCS bucket 的內容將覆蓋並替換最初烘焙到該路徑的 Docker image 中的任何模型。這意味著 GCS 將為您提供客製化模型。
選項 B：使用 GCS 安裝建立您自己的映像（無內建模型）：
如果您喜歡較小的Docker image或想要完全控制鏡像內容，您可以基於我們的[Dockerfile](./Dockerfile)來建立自己的映像。在這種情況下，您將從 Dockerfile 中刪除 `ollama pull` 命令，確保沒有模型被烘焙到映像中。然後，您可以使用 GCS 磁碟區掛載來部署此客製化映像。
```
# Example Dockerfile snippet (within your build stage)
# ... (other instructions) ...
# Store model weight files in /models (this is where the GCS volume will be mounted)
ENV OLLAMA_MODELS /models
# REMOVE THIS LINE:
# RUN /bin/ollama serve & sleep 5 && ollama pull $MODEL
# ... (rest of your Dockerfile) ...
```
然後[建立您的自訂映像](https://cloud.google.com/run/docs/building/containers#use-dockerfile)。
#### 4. 與您的自訂模型互動：
現在，您可以透過在 API 請求中指定 `<your-custom-model-name>`（`ollama create` 中使用的名稱）來使用自訂微調模型，就像使用預先建置模型一樣。
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
同樣，對於OpenAI SDK 和 curl 範例，將`<model>` 替換為`<your-custom-model-name>`。