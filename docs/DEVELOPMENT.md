# 開發環境

維護者與 AI 接手用的開發文件。產品使用方式在 [`README.md`](../README.md)；上游同步在 [`UPSTREAM.md`](UPSTREAM.md)；決策在 [`DECISIONS.md`](DECISIONS.md)；風險快照在 [`../REVIEW.md`](../REVIEW.md)。

## 架構

```text
SKILL.md                 產品 skill：六原則、觸發條件、反模式
        │
        └── references/  四聖諦除錯框架、延伸原則
        │
        ▼
 安裝到 ~/.agents/skills、~/.claude/skills 或 ~/.cursor/skills 後才真正可被呼叫
```

根目錄 `SKILL.md`、`references/` 是要安裝到 Agent Skills 目錄的產品。其餘檔案是本 fork 的開發與治理骨架，不要一起複製進 skills 目錄。

## 本機開發（Windows）

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements-dev.txt
$env:PYTHONUTF8 = "1"
pwsh -NoProfile -File tools\dev_check.ps1
```

先決條件：Python 3.14（CI 另測 3.9–3.14）、PowerShell 7。

只驗證產品入口是否齊全時，確認：

- `SKILL.md`
- `references/ariyasacca-debug.md`
- `references/extended-principles.md`

不要拿一次真實對話當 CI。產品是給宿主讀的檢查清單，gate 驗的是規格、連結與維護腳本。

## Canonical gate

`tools\dev_check.ps1` 會依序：

1. `python -m compileall`（`tests` 與 `tools` 底下的 `.py`）
2. `ruff check`（E9 + F）
3. `pytest tests/ -q`
4. `python tools/validate_skill.py SKILL.md`
5. `python tools/check_links.py`

CI 在 Ubuntu 跑 3.9–3.14，並加一個 Windows Python 3.14 job 跑同一套 gate。推 `main` 前先跑本機 gate。

## 工具設定

`pyproject.toml` **只放工具設定**，沒有 `[project]` 與 `[build-system]`：本 repo 交付的是 Markdown Agent Skill，不是 Python 套件。改 `ci.yml` 的 ruff 旗標時要同步改 `pyproject.toml`，`tests/test_docs.py::test_tool_config_matches_ci_flags` 會擋住漂移。`.python-version` 釘 3.14。

`.gitattributes` 把行尾釘成 LF。沒有它，全域 `core.autocrlf=true` 會讓工作區變 CRLF，於是 `git status` 顯示檔案 modified 但 `git diff` 是空的。

## 依賴新鮮度

`tools/check_dependency_freshness.py` 把 `requirements-dev.txt` 宣告的每一筆直接依賴拿去對 PyPI 現行版本，`.github/workflows/dependency-freshness.yml` 每月跑一次。紅燈只有兩條誠實出口：`# freshness-hold:`（常態政策）或 `.github/dependency-deferrals.json` 的 `deferredLatest`（會過期）。調高宣告下限來讓報告變綠不是出口。

## 不要做的事

- 不要把產品 `SKILL.md` 改寫成維護索引。
- 不要翻譯 `SKILL.md` 或 `references/`。
- 不要把 `README.th.md` 升成 fork 公開入口的第三語系。
- 不要提交 `.env`、API key 或 cookie。
- 測試必須是靜態規格檢查，不能拿一次真實對話當 fixture。
