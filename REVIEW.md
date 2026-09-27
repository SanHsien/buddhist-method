# Repository review（Windows-first）

- Review date: 2026-08-28
- Review baseline: `414fefa` 覆核快照；本輪再修 A-04 導流
- Remediation: overlay 初建 R-01～R-03 已在 tree；本輪把覆核 A-04 修掉（訪客導流）。A-01／A-02／A-03／A-05 維持不改。**不回貢**。
- Upstream reviewed through: `745caa74ef27fce7c57cbdbf27af5add3de884d7`
- Upstream watermarks: PR / issue `reviewed_pr_through` / `reviewed_issue_through` = **0**
- Primary environment: Windows 11、PowerShell、Python 3.14（本機 gate 與 CI Windows job）；Ubuntu CI 補 3.9–3.14
- Status: 維護骨架可用。產品 `SKILL.md`、`references/` 未改寫。訪客導流已修。本輪 **不回貢**。本次僅自審（未跑跨模型二審）。

## 結論

這個 fork 適合作為 Windows 本機安裝、並追蹤上游佛教工作紀律 Skill 的維護線。產品是一份英文 `SKILL.md`（137 行，`description` 956 字元）加兩份 `references/`，沒有 CLI 或後端。授權是 MIT（原作 Copyright Udomsak；overlay 另加 SanHsien）。

overlay 首推 `83a577f` 的 GitHub Actions **一次全綠**。本輪把覆核留下的可修項 A-04 修掉：產品原則 PR 導向上游，本 fork 不收。

**沒有**改寫產品 skill、**沒有**翻譯 `references/`、**沒有**對上游開 PR。

## 已修 findings

這些是 overlay 初建關掉的缺口（R-01～R-03），加上本輪修掉的訪客導流（R-04）。

| ID | 嚴重度 | Finding | 修復 |
|---|---|---|---|
| R-01 | P1 | 上游 repo 沒有 Windows 可重現的開發／驗收骨架，也沒有繁中維護入口。 | overlay：`AGENTS.md`、`FORK.md`、`docs/`、`tools/dev_check.ps1`、pytest／ruff CI、上游 baseline。本輪本機 gate 與 GitHub CI 都綠。 |
| R-02 | P2 | 公開入口若沿用上游英文 README 當唯一主檔，與其他 SanHsien fork 的繁中＋英文契約不一致。 | `README.md` 繁中主檔，`README.en.md` 英文鏡像。`README.th.md` 當產品檔保留；語言指標改指 `README.en.md`（`tests/test_docs.py` 擋住再寫回「README.md 是英文」）。 |
| R-03 | P3 | overlay 的 `LICENSE` 若只留原作 Copyright，fork 修改的歸屬不清楚。 | 加 `Copyright (c) 2026 SanHsien`，原作 Udomsak 行保留。`git diff 745caa7 HEAD -- LICENSE` 只多這一行。 |
| R-04 | P3 | `README.th.md` 的「ร่วมพัฒนา」仍是上游口吻，訪客會把產品原則 PR 開到這個 fork。Issue／PR 模板也只軟性問「是否回報上游」。 | 泰文檔加上 SanHsien fork 告示；`CONTRIBUTING.md`、Issue／PR 模板改成「本線不收產品原則 PR」。`test_contribution_guides_reject_product_prs_on_this_fork` 鎖行為。不回貢。 |

## 接受、不改契約

| ID | 嚴重度 | 處理 |
|---|---|---|
| A-01 | P1 | **不**翻譯 `SKILL.md`／`references/`。`git diff 745caa7 HEAD -- SKILL.md references/` 為空。 |
| A-02 | P2 | **不**刪 `README.th.md`，也**不**把它放進公開入口語言切換列。 |
| A-03 | P1 | **不回貢。** 本次對話明確先不考慮回貢。 |
| A-05 | P3 | GitHub topic 含 `buddhism`。Skill 本文寫明這不是宗教框架；topic 只是發現用，不改 README 的「不是宗教教材」陳述。 |

## 本輪實證

### 審查當下

```text
git rev-parse HEAD
→ 83a577f1d28b3e829bbbeec49924ca4e3963731d

gh repo set-default --view
→ SanHsien/buddhist-method

git ls-files -s CLAUDE.md
→ 100644（不是 120000 symlink）

git ls-files | 含 .env / credentials / cookies
→ 無

python tools/check_upstream_updates.py --strict
→ No new upstream commits. Nothing to review.
  reviewed_through = 745caa74ef27fce7c57cbdbf27af5add3de884d7
```

實查（不是只讀 README）：

- `git diff 745caa7 HEAD -- SKILL.md references/` 為空；產品本體與上游 head 相同。
- `SKILL.md` frontmatter：`name: buddhist-method`，`description` 956 字元（上限 1024），`license: MIT`。`validate_skill.py --lens claude` 0 error 0 warning。
- overlay Python（`tools/check_*.py`、`tools/validate_skill.py`）無 `os.system`、`shell=True`、`eval(`、`exec(`、`pickle`。`check_upstream_updates.py` 以 argv 列表呼叫 `git`。
- `tools/check_links.py` 拒絕逃出 repo 根目錄的相對路徑（`test_check_links_rejects_path_outside_repo`）。
- `.github/ISSUE_TEMPLATE/config.yml` 同時連本 fork `CONTRIBUTING.md` 與上游 `nai0om/buddhist-method`。
- CI／CodeQL／upstream-check／dependency-freshness 的 checkout 皆 pin `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1`（v7.0.1），且 `persist-credentials: false`。

**沒有**用真實開發任務跑一輪「原則是否真的改變 Agent 行為」。**沒有**對上游開 PR。

### 本機 gate

```text
pwsh -NoProfile -File tools\dev_check.ps1
→ compileall / ruff E9+F / pytest / validate_skill / check_links 全綠
→ 35 passed
→ 21 份維護文件 + SKILL 裝包路徑，0 斷連結
→ WINDOWS DEV CHECK GREEN
```

### GitHub Actions（overlay 首推 `83a577f`）

| Workflow | 結果 | 說明 |
|---|---|---|
| [CI](https://github.com/SanHsien/buddhist-method/actions/runs/33142788260) | success | Ubuntu `test (py3.9)`–`test (py3.14)` 與 `test (windows / py3.14)` 全綠 |
| [CodeQL](https://github.com/SanHsien/buddhist-method/actions/runs/33142788225) | success | Python `security-extended` |
| [Upstream check](https://github.com/SanHsien/buddhist-method/actions/runs/33142788408) | success | 無未審 upstream commit |
| [Dependency freshness](https://github.com/SanHsien/buddhist-method/actions/runs/33142788226) | success | |

## 已檢查、不列為 finding

- 產品現況：`SKILL.md` + `references/ariyasacca-debug.md` + `references/extended-principles.md`；frontmatter 可安裝。
- 倉庫沒有提交 `.env`（`git ls-files` 為 0）。
- 公開入口只留繁中／英文互指；README 保留 `nai0om/buddhist-method`、Udomsak、MIT、`NOTICE.md`。
- `pyproject.toml` 沒有 `[project]`／`[build-system]`；ruff 旗標與 `ci.yml` 一致（E9+F、py39）。
- `.gitattributes` 釘 `eol=lf`。
- Dependabot 只開 PR（pip + github-actions），不自動合併。
- `gh repo set-default --view` 為 `SanHsien/buddhist-method`。不對上游開 PR、不 push `upstream`。
- overlay 初建時 `git add --renormalize .` 只處理已追蹤檔；untracked overlay 是另一次 `git add` 進去的。目前 tree 完整，不是 ignore 規則把 `docs/`／`tools/` 吃掉。

## 尚未宣稱範圍

- **沒有**在 Cursor／Claude Code／Codex 實際跑一輪完整任務來證明六原則會改變行為。本機雖把產品檔複製到 `~\.cursor\skills\buddhist-method\`，那只是裝包，不是觸發證據。
- **沒有**把 overlay 送回上游。
- **不宣稱**本 fork 有自己的 GitHub Release 或獨立產品版號。
- `dev_check.ps1` **不含** Bandit；CodeQL 是獨立 workflow。
- **不宣稱** `SKILL.md` 的 `description`（956／1024）永遠夠用；上游若加長會先被 `validate_skill.py` 擋住。

## 建議下一步

1. 之後維護直接推 `origin/main`。回貢需當次對話明確同意。
2. 週排程 Upstream check 應維持綠；若再紅，先看是不是上游有新 commit，不要把 watermark 往回退。
3. 產品原則的實質改動開到 [`nai0om/buddhist-method`](https://github.com/nai0om/buddhist-method)。這個 fork 的 Issue／PR 模板已寫明不收。回貢需當次對話明確同意。
