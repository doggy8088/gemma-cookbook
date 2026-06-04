# TxGemma

這個資料夾依照主題分成數個分類，每一類都聚焦於使用 TxGemma 模型的特定面向：

* [推論與服務部署](#推論與服務部署)：如何載入、執行與部署 TxGemma 模型以進行推論
* [微調](#微調)：如何針對特定任務與領域微調 TxGemma 模型
* [Agentic](#agentic)：如何將 TxGemma 模型整合到 agentic 工作流程

更多關於 TxGemma 的資訊，請參考 [HAI-DEF developer site](https://developers.devsite.corp.google.com/health-ai-developer-foundations/txgemma)。

**引用**

```bibtex
@article{wang2025txgemma,
    title={TxGemma: Efficient and Agentic LLMs for Therapeutics},
    author={Wang, Eric and Schmidgall, Samuel and Jaeger, Paul F. and Zhang, Fan and Pilgrim, Rory and Matias, Yossi and Barral, Joelle and Fleet, David and Azizi, Shekoofeh},
    year={2025},
}
```

論文可見 [此處](https://arxiv.org/abs/2504.06196)。

## 推論與服務部署

| Notebook Name | Description |
| :------------------------------------------------------------------------------------------| --------------------------------------------------------------------------------------------------------------------------------- |
| [[TxGemma]Quickstart_with_Hugging_Face.ipynb]([TxGemma]Quickstart_with_Hugging_Face.ipynb) | 使用 [Hugging Face](https://huggingface.co/) 載入並執行 TxGemma。 |
| [[TxGemma]Quickstart_with_Model_Garden.ipynb]([TxGemma]Quickstart_with_Model_Garden.ipynb) | 使用 [Model Garden](https://console.cloud.google.com/vertex-ai/model-garden) 部署 TxGemma，並取得線上或批次預測。 |

## 微調
| Notebook Name | Description |
| :--------------------------------------------------------------------------------------| ------------------------------------------------------------------------------------------------------------- |
| [[TxGemma]Finetune_with_Hugging_Face.ipynb]([TxGemma]Finetune_with_Hugging_Face.ipynb) | 使用 Hugging Face libraries 在 [TrialBench](https://arxiv.org/abs/2407.00631) dataset 上微調 TxGemma。 |

## Agentic
| Notebook Name | Description |
| :--------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| [[TxGemma]Agentic_Demo_with_Hugging_Face.ipynb]([TxGemma]Agentic_Demo_with_Hugging_Face.ipynb) | 使用 Agentic-Tx，這是一個聚焦治療領域的 LLM agent。 |
