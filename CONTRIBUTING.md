# 貢獻指南

## 開始前

1. 先讀 [`AGENTS.md`](AGENTS.md)、[`FORK.md`](FORK.md)、[`README.md`](README.md) 與 [`REVIEW.md`](REVIEW.md)。
2. 確認問題在最新 `main` 仍可重現，並查過既有 Issues。
3. **這個 fork 不收產品原則 PR。** `SKILL.md` 或 `references/` 的實質變更請開到 [`nai0om/buddhist-method`](https://github.com/nai0om/buddhist-method)。本線只收 Windows gate、繁中／英文入口與維護骨架。
4. 不要附上 API key、cookie 或任何憑證。
5. 對上游開 PR 需要維護者在當次對話明確同意回貢。

## 本機開發

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements-dev.txt
pwsh -NoProfile -File tools\dev_check.ps1
```

## 提交方式

本 fork 由維護者直接推 `main`，不開短期分支。改完先跑上面的 Windows gate。

- 一次提交聚焦一個問題。
- Bug 修正先附失敗測試；新行為需涵蓋成功、邊界與錯誤路徑。
- 修改使用方式時同步更新 `README.md` 與 `README.en.md`。本 fork 的公開入口不收第三語系 README，也不把作者宣傳寫進公開入口。上游泰文 `README.th.md` 跟隨產品檔即可。
- 說明是否來自 upstream、是否改動產品 `SKILL.md`／`references/`，以及實際跑過哪些指令。
- 提交訊息建議使用 `fix:`、`feat:`、`docs:`、`test:`、`chore:`。
- Dependabot 與外部 fork 仍可能開 Pull Request；合併前讀 diff，不要自動合併。
- 對上游開 PR 需要維護者在當次對話明確同意回貢。
