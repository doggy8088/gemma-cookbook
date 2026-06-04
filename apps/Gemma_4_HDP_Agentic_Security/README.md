# Gemma 4 + HDP：保護代理函數調用

此範例示範如何將 **人工委託來源 (HDP)** 協定與 **Gemma 4 的本機函數呼叫** 集成，以加密方式驗證每個工具呼叫在執行前均經過人工委託人授權。
## 問題

Gemma 4 專為agentic 工作流程而建置。其原生函數呼叫使其能夠跨多步驟規劃自主調用工具和APIs——從雲端工作站到離線執行機器人的 Raspberry Pi。
這就產生了一個差距：當 Gemma 4 生成函數呼叫時，沒有人類主體授權該特定操作的可驗證記錄。注入的prompt、受損的system prompt或來自另一個agent的橫向樞軸可以觸發與工具介面上的合法請求無法區分的函數呼叫。

HDP 縮小了這一差距。
## What HDP does

HDP（IETF 草案：`draft-helixar-hdp-agentic-delegation-00`）提供：
- **Ed25519 簽署的委託代幣 (HDT)** 由人類委託人發行
- **範圍限制** — 允許 agent 呼叫哪些工具
- **Irreversibility classification** (Class 0–3) — from read-only to physical actuation
- **執行前驗證** - 中間件閘門在任何工具執行*之前*執行
- **審核日誌** — 每個授權決策的防篡改記錄

對於指導實體執行器的**邊緣裝置（Jetson Nano、Raspberry Pi + 機器手臂）上的 Gemma 4，HDP-P 配套規範增加了實施例約束、策略證明和佇列委派控制。
## 文件

| 文件 | 描述 ||---|---|
| `Gemma_4_HDP_Agentic_Security.ipynb` | 完整演練notebook — 載入Gemma 4，發出tokens，閘函數調用 || `hdp_middleware.py` | 嵌入式中間件 — `HDPMiddleware.gate()` 包裝任何 Gemma 4 工具執行器 |
## 快速啟動

```python
from hdp_middleware import HDPDelegationToken, HDPMiddleware, IrreversibilityClass
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

# Human principal issues a delegation token
private_key = Ed25519PrivateKey.generate()
token = HDPDelegationToken.issue(
    principal_id="alice@example.com",
    agent_id="gemma4-agent-01",
    scope=["get_weather", "send_email"],
    max_class=IrreversibilityClass.CLASS_2,
    ttl_seconds=3600,
    private_key=private_key,
)

# Middleware verifies every Gemma 4 function call before execution
middleware = HDPMiddleware(public_key=private_key.public_key())

result = middleware.gate(
    function_call={"name": "send_email", "parameters": {"to": "bob@example.com", ...}},
    token=token,
)

if result.allowed:
    execute_tool(function_call)
```

## 不可逆性等級

| 班級 | 定義 | 授權 ||---|---|---|
| 0 | 完全可逆－讀取、查詢 | HDT 足夠 || 1 | 努力可逆－書寫、移動 | HDT 足夠 || 2 | 不可逆——發送、刪除、發布 | HDT+本金確認 || 3 | 不可逆+潛在有害－物理驅動 | 需要雙主體 (HDP-P) |
## 參考

- **IETF 草案：** https://datatracker.ietf.org/doc/draft-helixar-hdp-agentic-delegation/
- **Zenodo DOI:** https://doi.org/10.5281/zenodo.19332023
- **HDP-P（實體人工智慧）：** https://doi.org/10.5281/ZENODO.19332440
- **螺旋：** https://helixar.ai
