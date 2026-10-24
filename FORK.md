# Fork 維護說明

本 repo fork 自 [`nai0om/buddhist-method`](https://github.com/nai0om/buddhist-method)，
沿用 MIT License 與完整 Git 歷史。

## 為什麼維護 fork

- 保留原作者把佛教認識論編成 Agent 工作紀律的產品 Skill。
- 採 Windows-first 維護：Windows 11 + PowerShell 是主要開發、除錯與完整驗收環境。
- 公開入口改以繁體中文為主，英文鏡像放 `README.en.md`。
- 建立可重現的 Windows 開發 gate、Windows CI job，以及逐筆審查的上游追蹤。
- 產品 Skill 仍可直接安裝到 `.agents/skills/`、`~/.claude/skills/` 或 `~/.cursor/skills/`。

**回貢判準：修的是上游的 bug 就送回去；這裡獨創的文件／Windows 維護骨架留在這裡。**
回貢前必須在當次對話取得維護者明確同意；「fork」「建開發環境」「開 PR」都不是同意。

## 與上游的差異

| 項目 | 說明 |
|---|---|
| `README.md` | 繁中主檔；英文鏡像在 `README.en.md`。上游泰文 `README.th.md` 當產品檔保留；語言指標改指 `README.en.md`；共同開發段加上「產品 PR 去上游」 |
| `CONTRIBUTING.md` / Issue／PR 模板 | 明寫本 fork 不收產品原則 PR |
| `AGENTS.md` | 本 fork 的 AI 維護單一真相源 |
| `NOTICE.md` / `FORK.md` | 來源、授權與同步說明 |
| `tools/dev_check.ps1` | Windows 本機一鍵 gate |
| `.github/workflows/ci.yml` | Ubuntu 3.9–3.14 + Windows Python 3.14：pytest / ruff / Skill 驗證 / 連結檢查 |
| `.github/workflows/upstream-check.yml` | 每週對 `upstream/main` 做未審查 commit 檢查 |
| `docs/DECISIONS.md`、`docs/UPSTREAM.md`、`docs/DEVELOPMENT.md` | fork 維護文件 |
| `REVIEW.md` | 風險快照，不是每個一般 bug 的流水帳 |

產品 `SKILL.md`、`references/` 以上游為準，除非有已記錄的 fork 修正。

## 分支與 remote

- `origin/main`：SanHsien 維護線，也是唯一長期分支。
- 日常修改直接推 `origin/main`。只有需要他人審查或高風險改動時才開 branch → PR。
- `upstream/main`：nai0om 原始專案，只追蹤、不推送。
- Dependabot 或外部 fork 的變更同樣走 PR，讀 diff 並通過 CI 後再合併。

不要 `git push upstream`。同步方式見 [`docs/UPSTREAM.md`](docs/UPSTREAM.md)。

上游更新英文 `README.md` 時，把新產品說明翻進本 fork 的繁中 `README.md`，並同步 `README.en.md`。作者宣傳不要帶進來。

## 換一台電腦怎麼開發

```powershell
git clone https://github.com/SanHsien/buddhist-method.git
cd buddhist-method
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements-dev.txt
pwsh -NoProfile -File tools\dev_check.ps1
```

只想安裝 Skill、不開發時，把這些產品檔一起放到 Agent Skills 目錄（例如 `~\.cursor\skills\buddhist-method\`、`~\.claude\skills\buddhist-method\` 或 `~\.agents\skills\buddhist-method\`）：

- `SKILL.md`
- `references/`

不要把 `tools/`、`docs/`、`tests/`、`.github/` 一併複製進去。
