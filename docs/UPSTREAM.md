# 上游維護

## Remote

- Fork：`origin` → `https://github.com/SanHsien/buddhist-method.git`
- 原作者：`upstream` → `https://github.com/nai0om/buddhist-method.git`
- 追蹤分支：`main`

## 檢查新提交

```powershell
git fetch upstream main
python tools\check_upstream_updates.py --strict
```

工具以 `tools/upstream_baseline.json` 的 `reviewed_through` 為起點，列出所有未審查提交。
有新提交或檢查失敗時，`--strict` 回傳非零；排程 workflow 也會因此明確失敗。

## 審查清冊

每次只做一次批次審查：

1. 讀 commit 主旨與變更檔案（open PR 必須讀 diff，禁止只憑標題結案）。
2. 判斷是否與繁中 README、Windows gate 或測試衝突。
3. 可直接同步的提交用 merge；只需要部分修正時 cherry-pick 或最小重做。
4. 跑 `pwsh -NoProfile -File tools\dev_check.ps1`。
5. 在 `docs/DECISIONS.md` 記錄採用／略過理由（須引用具體檔案與衝突點）。
6. 驗證完成後才把 baseline 推進到已審查的完整 40 字元 SHA。

Baseline 代表「已審查」，不代表「全部已合併」。

README 衝突的解法：上游新英文產品說明翻進 `README.md`，並同步 `README.en.md`。作者宣傳略過。`README.th.md` 跟隨上游產品檔。來源與授權 credit 留在 README 與 `NOTICE.md`。

## 2026-08-28：fork 起點

本 fork 自上游 `main` `745caa74ef27fce7c57cbdbf27af5add3de884d7`
（`Replace git clone snippet with one-shot Claude Code install prompt`）建立。此 SHA 設為第一個 `reviewed_through`。
之後的上游 commit 才需要進入審查清冊。

水位：

- PR：上游無 open PR；`reviewed_pr_through` = **0**
- issue：上游無 open issue；`reviewed_issue_through` = **0**
- commit baseline：`745caa7`（完整 SHA 見 `tools/upstream_baseline.json`）
- 下次只看編號更大的，或已評估項目是否出現新 commit／新 head

上游目前只有兩筆 commit（初始導入與上述 README 一鍵安裝提示）。產品 `SKILL.md`、`references/`、`README.th.md`、MIT `LICENSE` 原樣保留。
