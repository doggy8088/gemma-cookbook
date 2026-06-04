# 為Gemma Cookbook 做出貢獻

我們很樂意接受您對Gemma Cookbook 的補丁和貢獻。我們很高興您考慮捐贈一些時間，本指南將幫助我們尊重這段時間。
# 在您發送任何內容之前

## 簽署我們的貢獻者協議

對該專案的所有貢獻都必須附有[貢獻者許可協議](https://cla.developers.google.com/about) (CLA)。您（或您的雇主）保留您的貢獻的版權；這只是允許我們作為專案的一部分使用和重新分發您的貢獻。
如果您或您目前的雇主已經簽署了 Google CLA（即使是針對不同的項目），您可能不需要再次簽署。

請造訪 [https://cla.developers.google.com/](https://cla.developers.google.com/) 查看您目前的協議或簽署新協議。
## 風格指南

在開始寫作之前，請先查看[技術寫作風格指南](https://developers.google.com/style)。您不需要完全消化整個文檔，但請閱讀[要點](https://developers.google.com/style/highlights)，以便您可以預見最常見的回饋。
另請參閱您將使用的語言的相關[風格指南](https://google.github.io/styleguide/)。這些嚴格適用於原始程式碼檔案（例如 *.py、*.js），儘管文件中的程式碼片段（例如 markdown 檔案或 notebooks）往往更注重可讀性而不是嚴格遵守。
# 公關清單

1. Commit your finished notebook with comments and clean output after finishing the following:
   * 確保在頂部包含設定步驟（您可以從任何現有notebook複製），包括：
*Colab自連結到您的notebook * how to select GPU * 如何設定Kaggle/HF tokens   * 在 notebook 頂部新增署名，其中包含您的姓名、社交帳號和/或 GitHub 用戶名
   * 執行「nbfmt」和「nblint」進行格式化和檢查（[參考](.github/workflows/notebooks.yaml)）
   * 將您的notebook命名為以下劃線分隔的單字。例如，“Integrate_with_Mesop.ipynb”
2. 在 README.md 的目錄中新增 notebook 名稱和簡短描述
3. （如果適用）刪除您在 WISHLIST.md 中實作的項目
4. 提交審核
5. 在您的公關評論中，請告訴我們您是否希望在 Google 的社交帳號中突出顯示您的貢獻（例如，[Google for Developers](https://x.com/googledevs?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor) Twitter）

# 做出改變

## 小修復

小的修復，例如拼寫錯誤或錯誤修復，可以透過拉取請求直接提交。
## 大的變化或新的notebook

在發送 PR 之前，甚至寫一行內容之前，請先提交一個 [問題](https://github.com/google-gemini/gemma-cookbook/issues)。在那裡，我們可以討論該請求並提供有關如何建立您編寫的任何內容的指導。
新增指南通常涉及大量詳細的評論，我們希望在您開始編寫任何內容之前確保您的想法已完全形成並得到充分支持。另請先檢查目錄，以避免重複現有工作。如果您想移植現有的指南（例如，如果您自己的 GitHub 上有 Gemma 的指南），請隨時在問題中連結到它。
## 我們考慮的事情

在接受新指南時，我們希望平衡幾個面向：* 原創性 - 例如還有其他指南可以做同樣的事情嗎？
* 教育學 - 例如本指南是否教授了一些有用的內容？专门针对 Gemma 功能？
* 品質 - 例如本指南是否包含清晰的描述性文字？程式碼容易理解嗎？有沒有錯誤？
* 實用性 - 例如，指南中使用的技術在現實世界中實用嗎？

提交在所有這些方面都強大並不重要，但越強大越好。舊的提交內容可能會被超出這些屬性的新提交內容所取代。