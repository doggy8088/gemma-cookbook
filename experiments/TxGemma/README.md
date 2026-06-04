# TxGemma

該資料夾分為幾個類別，每個類別都專注於使用 TxGemma 模型的特定方面：
* [推論與服務](#inference-and-serving)：如何為inference載入、執行和部署TxGemma模型
* [微調](#fine-tuning)：如何針對特定任務與領域微調TxGemma模型
* [代理](#agentic)：如何將TxGemma模型整合到agentic工作流程中

有關TxGemma的更多信息，請訪問[HAI-DEF 開發者網站](https://developers.devsite.corp.google.com/health-ai-developer-foundations/txgemma)。
**引用**
```bibtex
@article{wang2025txgemma,
    title={TxGemma: Efficient and Agentic LLMs for Therapeutics},
    author={Wang, Eric and Schmidgall, Samuel and Jaeger, Paul F. and Zhang, Fan and Pilgrim, Rory and Matias, Yossi and Barral, Joelle and Fleet, David and Azizi, Shekoofeh},
    year={2025},
}
```

在[此處](https://arxiv.org/abs/2504.06196) 尋找論文。
## 推論和服務

| notebook 名稱 | 描述 || :------------------------------------------------------------------------------------------| --------------------------------------------------------------------------------------------------------------------------------- |
| [[TxGemma]Quickstart_with_Hugging_Face.ipynb]([TxGemma]Quickstart_with_Hugging_Face.ipynb) | 使用 [Hugging Face](https://huggingface.co/) 載入並執行 TxGemma。 || [[TxGemma]Quickstart_with_Model_Garden.ipynb]([TxGemma]Quickstart_with_Model_Garden.ipynb) | 使用 [Model Garden](https://console.cloud.google.com/vertex-ai/model-garden) 部署 TxGemma 並獲得線上或批次預測。 |
## 微調
| notebook 名稱 | 描述 || :--------------------------------------------------------------------------------------| ------------------------------------------------------------------------------------------------------------- |
| [[TxGemma]Finetune_with_Hugging_Face.ipynb]([TxGemma]Finetune_with_Hugging_Face.ipynb) | 使用 Hugging Face 庫在 [TrialBench](https://arxiv.org/abs/2407.00631) dataset 上微調 TxGemma。 |
## 代理商
| notebook 名稱 | 描述 || :--------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| [[TxGemma]Agentic_Demo_with_Hugging_Face.ipynb]([TxGemma]Agentic_Demo_with_Hugging_Face.ipynb) | 使用 Agentic-Tx，一個專注於治療學的法學碩士agent。 |