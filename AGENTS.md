# AGENTS.md

給 Codex、Claude Code、Cursor 與其他自動化代理在本專案工作時的指引。產品與使用方式先讀 [`README.md`](README.md)；開發與驗收細節見 [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md)。

## 專案定位

這是 [`nai0om/buddhist-method`](https://github.com/nai0om/buddhist-method) 的 MIT fork。
核心價值是把六條佛教認識論原則編成 Agent 的工作紀律：講事實前先核對、除錯先找根因、長任務重新確認現況、草稿可整份丟掉、捷徑先問是不是藏問題、壓力變大時不要輕易改立場。它不是宗教教材。

`origin` 是 `SanHsien/buddhist-method`，`upstream` 是原作者 repo，預設分支皆為 `main`。
保留上游作者、MIT 授權與產品 `SKILL.md`、`references/`。本 fork 的維護差異記在 [`FORK.md`](FORK.md) 與 [`docs/DECISIONS.md`](docs/DECISIONS.md)。

主要開發與完整驗收環境是 **Windows 11 + PowerShell**；Ubuntu CI 補跨平台相容性。

## 硬性邊界

- **不要覆寫產品 `SKILL.md`。** 根目錄 `SKILL.md` 與 `references/` 是給 Claude Code / Cursor / Codex 安裝的產品規格，不是本 fork 的維護索引。除非有已記錄的 fork 修正（見 `FORK.md` 與 `docs/DECISIONS.md`），否則以上游為準。維護規則以本檔為準。
- 不要把產品 Skill 或 `references/` 翻譯成繁體來「統一文件語言」。上游產品語言是英文（另有泰文 `README.th.md`）；本 fork 的公開入口與維護文件只使用繁體中文與英文。`README.th.md` 當上游產品檔保留，不當第三語系入口。
- 不提交 `.env`、API key、cookie、帳號資料。
- 不推送到 `upstream`。上游同步先跑 `python tools/check_upstream_updates.py`，逐筆審查後再 merge / cherry-pick；不盲目覆蓋 fork 文件與 Windows gate。
- 不把本 fork 包裝成原創專案，不移除原作者與 MIT 標示。
- 不把 Palī／泰文原則名稱改成純英文標籤。名稱是助記鍵，剝掉等於把 sigmoid 改名叫「彎彎的函數」。

## 技術與資料流

- 產品本體是 Markdown skill：`SKILL.md` + `references/`。執行時由宿主 Agent 讀檔，沒有獨立 CLI 或後端。
- `tools/`：fork 維護工具（上游檢查、Skill 規格驗證、相對連結檢查、Windows gate）。
- `tests/`：pytest。CI 另跑 ruff（E9+F）與 `validate_skill.py`。
- `pyproject.toml`：**只放工具設定**，沒有 `[project]` 與 `[build-system]`——本 repo 交付的是
  Markdown Agent Skill，不是 Python 套件。它存在是為了讓本機裸跑 `ruff check`／`pytest` 等同 CI；
  改 `ci.yml` 的 ruff 旗標時要同步改這裡，`tests/test_docs.py` 會擋住漂移。
- `.gitattributes`：index 全 LF。沒有它，全域 `core.autocrlf=true` 會讓檔案假性顯示為 modified
  （`git status` 有、`git diff` 空）。

## 開發原則

- 一般變更直接推 `origin/main`，不開功能分支、不開維護 PR（2026-08-22 起）。只有在需要他人審查、或改動風險高到值得先讓 CI 在 PR 上跑一輪時，才退回 **branch → PR → CI → merge**。與 `CONTRIBUTING.md` 一致。
- 修 bug 先補可重現失敗測試，再做最小修正。
- 上游公開安裝方式、`SKILL.md` 六原則與 `references/` 路徑視為相容性契約。
- 不為了套格式而大改上游檔案；Ruff 只閘 E9（語法）與 F（pyflakes）。
- 使用繁體中文回覆；使用者文件以繁中為主，公開入口同步維護 `README.en.md`。回覆直接交付可驗證結果，避免冗長背景鋪陳。
- 上游更新英文 `README.md` 時：把產品說明翻進本 fork 的繁中 `README.md`，並同步 `README.en.md`。不要帶回作者宣傳。泰文 `README.th.md` 跟隨上游產品檔即可，不要把它升成 fork 公開入口。
- 提交訊息用 Conventional Commit。Dependabot 或外部 fork 的變更也走 PR，讀 diff 並通過 CI 後再合併。
- `REVIEW.md` 是風險快照，不是每個一般 bug 的流水帳。
- 不 force-push `main`，不刪 `upstream` remote。

## 上游處理

1. `git fetch upstream main`
2. `python tools/check_upstream_updates.py --strict`
3. 逐筆判斷是否與繁中 README、Windows gate 或測試衝突。
4. 可同步的提交用 merge；只需要部分修正時 cherry-pick 或最小重做。
5. 跑 `pwsh -NoProfile -File tools\dev_check.ps1`
6. 採用／略過寫進 `docs/DECISIONS.md`，驗證後才推進 `tools/upstream_baseline.json`

Baseline 代表「已審查」，不代表「全部已合併」。

**四個面向都要看，不是只看 commit**：commit、open PR、open issue、上游分支。每個面向各記一個
水位（`reviewed_through`／`reviewed_pr_through`／`reviewed_issue_through`，分支記 head SHA），
下次只看更大的編號或變動過的 head。

**判準是證據，不是分類。** 結論要寫得可查證：diff 動了哪些檔案、本 fork 對應的檔案實際長什麼樣，以及**觸發條件**。

## 驗證

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements-dev.txt
pwsh -NoProfile -File tools\dev_check.ps1
```

沒有實際跑過 Windows gate，不要宣稱本機開發環境已可用。

## 文件責任

- `README.md` / `README.en.md`：公開產品與 fork 入口。只留繁中與英文；來源與授權 credit 必留，作者宣傳不轉載。
- `FORK.md`：與上游的關係、差異、同步方式。
- `NOTICE.md`：授權與 attribution。
- `docs/UPSTREAM.md`：upstream remote 與審查清冊。
- `docs/DEVELOPMENT.md`：本機開發與驗收指令。
- `docs/DECISIONS.md`：長期取捨。
- `REVIEW.md`：最新專案覆核狀態，不是 bug log。
- `CONTRIBUTING.md` / `SECURITY.md` / `CODE_OF_CONDUCT.md`：本 fork 的貢獻、安全回報與行為準則。
- `CHANGELOG.md` / `CHANGELOG.en.md`：**只記本 fork 的維護歷史**，不複製上游產品演進。上游逐筆採用／略過的理由仍寫在 `docs/DECISIONS.md`。

## 對外邊界：PR 只打本 fork

- **PR、push、release 一律指向 `SanHsien/buddhist-method`。** 對上游 `nai0om/buddhist-method` 開 PR、push 或發 release
  需要維護者在當次對話明確同意回貢；「fork 一份」「建開發環境」「比照其他 repo」都不是同意。
- 根因是機制不是粗心：`gh` 在 fork clone 的**預設 repo 就是上游**（`gh repo set-default --view` 會回
  `nai0om/buddhist-method`），裸跑 `gh pr create` 必然打上去。每個 clone 先跑一次
  `gh repo set-default SanHsien/buddhist-method`。
- 開 PR 仍明寫 `gh pr create --repo SanHsien/buddhist-method --base <分支> --head <分支>`，並**讀輸出的 URL**，
  owner 必須是 `SanHsien`。不是就立刻 `gh pr close` 留言道歉說明，再對 origin 重開。
- 2026-08-22 一天內兩個工作階段各誤開一個上游 PR（`lidge-jun/opencodex#2373`、
  `hamanpaul/paulsha-cortex#787`）。批次跑多個 repo 時最容易略過確認，而那正是兩次出事的場合。
