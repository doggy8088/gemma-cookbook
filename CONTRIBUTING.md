# 為 Gemma Cookbook 做出貢獻

我們很樂意接受你對 Gemma Cookbook 的修補與貢獻。很高興你願意投入時間，而這份指南會幫助我們尊重你的時間並讓協作更順利。

# 提交前須知

## 簽署 contributor agreement

對本專案的所有貢獻，都必須附上 [Contributor License Agreement](https://cla.developers.google.com/about)（CLA）。你（或你的雇主）仍保有你所提交內容的著作權；CLA 只是授權我們可將你的貢獻作為本專案的一部分使用與再散布。

如果你或你目前的雇主之前已簽署過 Google CLA（即使是其他專案），通常不需要再次簽署。

請前往 [https://cla.developers.google.com/](https://cla.developers.google.com/) 查詢你目前的協議狀態，或簽署新的協議。

## Style guides

開始撰寫前，請先閱讀 [technical writing style guide](https://developers.google.com/style)。你不必一次消化完整文件，但至少請先看過 [highlights](https://developers.google.com/style/highlights)，以便預期最常見的回饋方向。

也請查看你所使用語言對應的 [style guide](https://google.github.io/styleguide/)。這些規範會嚴格套用於原始程式碼檔（例如 `*.py`、`*.js`），至於文件中的程式片段（例如 markdown 或 notebook），通常會以可讀性優先，而不是絕對嚴格遵守風格規範。

# PR 檢查清單

1. 完成下列事項後，提交含註解且輸出乾淨的 notebook：
   * 請確認 notebook 最上方包含 setup 步驟（可參考任何既有 notebook），其中應包括：
        * 指向你 notebook 的 Colab 自連結
        * 如何選擇 GPU
        * 如何設定 Kaggle/HF tokens
   * 在 notebook 開頭加入署名，包含你的姓名、社群帳號與/或 GitHub username
   * 執行 `nbfmt` 與 `nblint` 進行格式化與 lint（[參考](.github/workflows/notebooks.yaml)）
   * notebook 檔名請使用底線分隔單字，例如 `Integrate_with_Mesop.ipynb`
2. 在 `README.md` 的目錄中加入 notebook 名稱與簡短說明
3. （如適用）刪除你已實作項目在 `WISHLIST.md` 中的條目
4. 提交 review
5. 在 PR 留言中告訴我們，你是否希望你的貢獻出現在 Google 的官方社群帳號中（例如 [Google for Developers](https://x.com/googledevs?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor) 的 Twitter）

# 變更方式

## 小型修正

像是 typo 或 bug fix 這類小型修正，可以直接透過 pull request 提交。

## 大型變更或新 notebook

在你送出 PR 之前，甚至在你開始寫第一行內容之前，請先提出一個 [issue](https://github.com/google-gemini/gemma-cookbook/issues)。我們會在那裡討論你的需求，並提供如何組織內容的建議。

新增一份新指南通常需要大量細部 review，我們希望在你開始撰寫前，就先確認你的構想已經成形並獲得充分支持。也請先查看目錄，以避免與既有內容重複。如果你是想移植現有指南（例如你自己 GitHub 上已經有 Gemma 指南），也歡迎在 issue 中附上連結。

## 我們重視的面向

在接受新指南時，我們會平衡以下幾個面向：
* 原創性 - 例如：是否已有其他指南在做同樣的事情？
* 教學性 - 例如：這份指南是否真的教會使用者有用的內容？是否確實對應某個 Gemma 功能？
* 品質 - 例如：是否有清楚、具描述性的文字？程式碼是否容易理解？內容是否有錯誤？
* 實用性 - 例如：指南中使用的技術是否真的適用於真實世界？

不要求每份提交都在所有面向上都非常突出，但越強越好。若有更新、品質更佳的新提交出現，較舊的提交可能會被取代。
