# 在 NVIDIA Jetson Orin Nano 上執行Gemma

NVIDIA Jetson Orin Nano 開發套件是一款小巧但功能強大的計算機
能夠執行開放模型，使其成為一種很好的實驗方式
設備上inference。
但是，為了獲得最佳性能，應將其更新為
最新版本的 NVIDIA JetPack 堆疊。
## 為什麼要更新？

tl,dr：以獲得更高的效能。
Jetson Orin Nano 套件通常在工廠預先安裝較舊的套件
NVIDIA JetPack 版本。
2024年12月，NVIDIA 發表 JetPack 6.2更新，增添新動力
Jetson Orin Nano 的模式可以解鎖更高等級的效能，
如下表所示。

Jetson Orin Nano 8GB 上tokens/秒的基準：| 模型 | 奧林 Nano 8GB（原廠） | Orin Nano 8GB（超級模式） | 性能增益 (x) ||:------|:-------------------------|:---------------------------|:-------------|
| Gemma 2 2B | 21.5 | 35.0 | 1.63 || Gemma 2 9B | 7.20 | 9.20 | 1.28 || PaliGemma2 3B | 13.7 | 21.6 | 1.58 |
有關更多信息，請參閱
https://developer.nvidia.com/blog/nvidia-jetpack-6-2-brings-super-mode-to-nvidia-jetson-orin-nano-and-jetson-orin-nx-modules/
## 更新您的開發套件

NVIDIA 已為此過程準備了完整指南，您可以在此處找到。
https://www.jetson-ai-lab.com/initial_setup_jon.html
請注意，您需要一張至少 64GB 容量的 microSD 卡和一台計算機
with a microSD reader.

## 在您的開發套件上執行 Gemma

### 入門
您與開發套件上的 Gemma 的大部分互動都將使用
終端，使用 cURL 和 wget 等工具。
在執行其他操作之前，請先在開發套件上安裝 cURL。
注意：Jetson Orin Nano 的預設使用者名稱和密碼是
`nvidia` / `nvidia`
1. 開啟終端應用程式

    Shortcut : Ctrl + Alt + T

2. 安裝捲曲

    $ sudo apt install curl

### Ollama

Ollama 提供了一種簡化且用戶友好的方式來執行和管理大型
本地語言模式。
它簡化了設定、模型管理和交互，重點是
易用性和可擴展性，使法學碩士可供更廣泛的使用者使用。
以下是在 Jetson Orin 上執行 Ollama 和 Gemma 3 的快速指南
奈米。
首先，安裝Ollama：
    $ curl -fsSL https://ollama.com/install.sh | sh


這將安裝 Ollama 並使其在您的系統路徑中以 `ollama` 的形式存取。
接下來，使用 Gemma 3 嘗試 Ollama 和一些文本 inference（Ollama 將獲取
並在第一次使用時緩存模型）。
    $ ollama run gemma3:1b “Write me a poem about the Kraken.”

# 更多資訊

有關可能性的視訊演示，請參閱 [演示：Gemma 2 2B 在 Jetson Orin Nano 上
](https://www.youtube.com/watch?v=Kd7VJ-TKb8I&list=PLOU2XLYxmsIKOyXflnuPK-qe32hZLc2HB&index=12)。
有關使用 Ollama 的更多信息，請參閱 [Ollama 文件](https://ai.google.dev/gemma/docs/integrations/ollama)
在 ai.google.dev 上。
