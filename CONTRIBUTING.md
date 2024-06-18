# 貢獻到 Gemma Cookbook

我們很樂意接受您對 Gemma Cookbook 的修補和貢獻。我們很高興您考慮捐贈一些您的時間，本指南將幫助我們尊重您的時間。

# 在你發送任何東西之前

## 簽署我們的貢獻者協議

所有對此專案的貢獻必須附有[貢獻者授權協議](https://cla.developers.google.com/about) (CLA)。您（或您的雇主）保留對您貢獻的版權；這只是給予我們使用和重新分發您的貢獻作為專案一部分的許可。

如果你或你的現任雇主已經簽署了 Google CLA（即使是針對不同的專案），你可能不需要再次簽署。

請訪問 [https://cla.developers.google.com/](https://cla.developers.google.com/) 查看您當前的協議或簽署新的協議。

## Style guides

在你開始寫作之前，請查看[技術寫作風格指南](https://developers.google.com/style)。你不需要完全消化整個文件，但請閱讀[重點](https://developers.google.com/style/highlights)，這樣你可以預期最常見的反饋。

也請查看您將使用的語言的相關[風格指南](https://google.github.io/styleguide/)。這些嚴格適用於原始程式碼檔案（例如 *.py, *.js），雖然文件中的程式碼片段（例如 markdown 檔案或筆記本）傾向於可讀性而非嚴格遵守。

# PR checklist

1. 提交完成的筆記本，並在完成以下操作後添加評論和清理輸出：
   * 確保在頂部包含設定步驟（可以從任何現有的筆記本中複製），包括：
        * 指向您筆記本的 Colab 自我連結
        * 如何選擇 GPU
        * 如何設定 Kaggle/HF 令牌
   * 在筆記本頂部包含您的姓名、社交帳號和/或 GitHub 用戶名
   * 執行 ‘pyink’ 進行格式化
   * 使用下劃線分隔單詞來命名您的筆記本。例如，‘Integrate_with_Mesop.ipynb’
2. 在 README.md 中的目錄中添加筆記本名稱和簡短描述
3. （如果適用）移除您在 WISHLIST.md 中已實現的條目
4. 提交審查
5. 在您的 PR 評論中，讓我們知道您是否希望您的貢獻在 Google 的社交帳號中被突出顯示（例如，[Google for Developers](https://x.com/googledevs?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor) Twitter）

# 進行變更

## 小修正

小的修正，例如拼寫錯誤或錯誤修正，可以直接通過 pull request 提交。

## 大幅變更或新的筆記本

在您發送 PR 或甚至撰寫一行程式碼之前，請提交一個 [issue](https://github.com/google-gemini/gemma-cookbook/issues)。在那裡我們可以討論請求並提供有關如何構建您撰寫的任何內容的指導。

新增指南通常涉及大量詳細審查，我們希望確保您的想法已經充分形成並且在您開始撰寫任何內容之前獲得充分支持。請先檢查目錄表以避免重複現有工作。如果您想要移植現有的指南（例如，如果您在自己的 GitHub 上有一個 Gemma 的指南），請隨時在問題中鏈接到它。

## 我們考慮的事情

當接受一個新的指南時，我們希望平衡幾個方面：

* 原創性 - 例如，有沒有其他指南做同樣的事情？
* 教學法 - 例如，這個指南是否教了有用的東西？特別是關於 Gemma 功能的？
* 品質 - 例如，這個指南是否包含清晰、描述性的文章？程式碼是否容易理解？有沒有任何錯誤？
* 實用性 - 例如，指南中使用的技術在現實世界中是否實用？

提交不需要在所有這些方面都很強，但越強越好。舊的提交可能會被超過這些屬性的較新提交取代。

