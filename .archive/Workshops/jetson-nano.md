# 在 NVIDIA Jetson Orin Nano 上執行 Gemma

NVIDIA Jetson Orin Nano developer kit 是一台小巧但性能強大的電腦，
能夠執行開放模型，因此非常適合用來體驗 on-device inference。

不過，若要取得最佳效能，建議先將它更新到
最新版的 NVIDIA JetPack stack。

## 為什麼要更新？

tl;dr：效能會高很多。

Jetson Orin Nano kit 出廠時通常已預先燒錄較舊版本的
NVIDIA JetPack。

在 2024 年 12 月，NVIDIA 發布了 JetPack 6.2 更新，
為 Jetson Orin Nano 新增了新的電源模式，可解鎖顯著更高的效能，
如下表所示。


Jetson Orin Nano 8GB 的 benchmark 效能（tokens/sec）：
| Model | Orin Nano 8GB（原始） | Orin Nano 8GB（Super Mode） | Perf Gain (x)|
|:------|:-------------------------|:---------------------------|:-------------|
|Gemma 2 2B|21.5|35.0|1.63|
|Gemma 2 9B|7.20|9.20|1.28|
|PaliGemma2 3B|13.7|21.6|1.58|

更多資訊請參考：
https://developer.nvidia.com/blog/nvidia-jetpack-6-2-brings-super-mode-to-nvidia-jetson-orin-nano-and-jetson-orin-nx-modules/

## 更新你的 dev kit

NVIDIA 已為這個流程準備了完整指南，可在這裡找到：

https://www.jetson-ai-lab.com/initial_setup_jon.html

請注意，你需要至少 64GB 容量的 microSD 卡，以及一台具備 microSD reader 的電腦。

## 在你的 dev kit 上執行 Gemma

### 快速開始
你在 dev kit 上與 Gemma 的大部分互動，都會透過 terminal 與 cURL、wget 等工具進行。

建議在開始之前，先在 dev kit 上安裝 cURL。

注意：Jetson Orin Nano 預設的 username 與 password 是
`nvidia` / `nvidia`

1. 開啟 Terminal app

    快捷鍵：Ctrl + Alt + T

2. 安裝 curl

    $ sudo apt install curl

### Ollama

Ollama 提供一種簡化、友善的方式，可在本機執行與管理大型語言模型。

它簡化了 setup、model management 與互動流程，重點在於易用性與可擴充性，讓更多人都能使用 LLM。

以下是使用 Ollama 與 Gemma 3 在 Jetson Orin Nano 上執行的快速指南。

先安裝 Ollama：

    $ curl -fsSL https://ollama.com/install.sh | sh


這會安裝 Ollama，並將其加入 system path，命令名稱為 `ollama`。

接著，試著用 Gemma 3 執行一段文字推論（Ollama 第一次使用時會抓取並快取模型）。

    $ ollama run gemma3:1b “Write me a poem about the Kraken.”

# 更多資訊

若想看示範影片，請參考 [Demo: Gemma 2 2B on a Jetson Orin Nano
](https://www.youtube.com/watch?v=Kd7VJ-TKb8I&list=PLOU2XLYxmsIKOyXflnuPK-qe32hZLc2HB&index=12)。

更多關於使用 Ollama 的資訊，請參考 ai.google.dev 上的 [Ollama documentation](https://ai.google.dev/gemma/docs/integrations/ollama)。
