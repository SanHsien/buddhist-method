# 維護決策

## 2026-08-28：建立 Windows-first 維護型 fork

**決定**：fork `nai0om/buddhist-method`，保留 MIT 與完整歷史，預設分支維持 `main` 以降低與上游同步摩擦。本線聚焦繁中公開入口、Windows 開發 gate、Windows CI，以及逐筆審查的上游追蹤。

**理由**：上游已把六條佛教認識論原則編成可安裝的 Agent Skill，符合維護者用工作紀律約束 Agent 的需求。缺的是 Windows 11 上可重現的開發／驗收骨架，以及繁中入口。直接用上游 repo 難以長期記錄 fork 取捨。授權是 MIT，fork 修改同樣走 MIT。

**限制**：

- 不把 fork 包裝成原創專案，不移除原作者與 MIT 標示。
- `SKILL.md` 與 `references/` 保持產品規格，不用維護索引覆寫。
- 不把產品 skill 翻譯成繁體；產品語言跟隨上游英文。
- 上游泰文 `README.th.md` 當產品檔保留，不升成 fork 公開入口。
- 上游更新必須逐筆審查。
- 不回貢，除非維護者在當次對話明確同意。

## 2026-08-28：維護線直接推 main

**決定**：fork 維護不再開功能分支。改完在本機跑 gate，通過後直接推 `origin/main`。遠端只留 `main`；`upstream/main` 只追蹤。

**理由**：這是單人維護 fork，分支與 PR 沒有第二審查者，只增加同步成本。

**限制**：

- Dependabot 與外部 fork 仍可能開 PR，讀 diff 後再合併，不自動合併。
- 不推 `upstream`，不 force-push `main`。
- 不刪 `upstream` remote。

## 2026-08-28：不啟用 Dependabot 自動合併

**決定**：Dependabot 只開 PR；CI 與人工讀 diff 通過後才合併。

**理由**：開發依賴只有 pytest / ruff，體積小，但自動合併仍會跳過「讀 diff」這一步。

## 2026-08-28：公開文件只留繁中與英文；README 只留 credit

**決定**：GitHub About 與公開入口只用繁體中文與英文。README 不轉載作者個人宣傳。來源與授權 credit 留在 README 短段與 `NOTICE.md`。`README.th.md` 跟隨上游，不當第三語系切換列。

**理由**：這是維護型 fork，不是原作者的宣傳頁。相關 credit 放 README 短段與 `NOTICE.md` 即可滿足 MIT 標示。上游泰文 README 是產品檔，刪掉會少一份原作；把它放進語言切換列則違反「公開入口只留繁中與英文」。

**限制**：上游若把宣傳段落一併推進來，merge 後刪掉／不要合進公開入口。原則表與 references 連結可同步。

## 2026-08-28：README.th.md 語言指標改指 README.en.md

**決定**：保留上游泰文 `README.th.md`，但把「英文版在 README.md」改成指向 `README.en.md`，並在目錄樹補上 `README.en.md`。

**理由**：本 fork 的 `README.md` 已是繁中主檔。若泰文檔仍寫「README.md 是英文」，讀者會點進繁中頁卻以為是英文。這是 overlay 造成的事實錯誤，不是翻譯產品 skill。

**限制**：不把 `README.th.md` 翻成繁中，不把它放進公開入口語言切換列。目錄樹不改成完整 overlay 清單。

## 2026-08-28：訪客導流——產品 PR 去上游，本線不收

**決定**：`README.th.md` 共同開發段加上 fork 說明；`CONTRIBUTING.md`、Issue／PR 模板明寫本 fork 不收產品原則 PR。不回貢。

**理由**：覆核 A-04。泰文檔沿用上游「歡迎開 PR」口吻，訪客會把產品原則 PR 開到這個 fork。這是 overlay 造成的導流錯誤，用最短的英文告示修好，不改寫上游對新原則的門檻文字。

**限制**：不翻譯 `SKILL.md`／`references/`。不把 GitHub topic `buddhism` 拿掉。不對上游開 PR。

## 2026-08-28：fork 起點 baseline

**決定**：`tools/upstream_baseline.json` 的 `reviewed_through` 設為上游 `main` head `745caa74ef27fce7c57cbdbf27af5add3de884d7`。PR／issue 水位為 0（上游無 open 項目）。

**理由**：這是 fork 當下已審查的完整歷史。之後的 commit／PR／issue 才需要進清冊。

**限制**：baseline 代表已審查，不代表之後可以盲目 merge。

## 2026-08-29：上游檢查補上 PR 與 issue 兩個面向

**決定**：`check_upstream_updates.py` 補上以 `--state all` 收集上游 PR／issue 的邏輯，
`upstream-check.yml` 補 `GH_TOKEN: ${{ github.token }}`，新增 `tests/test_upstream_updates.py`。
Baseline 既有的水位不動。

**理由**：`docs/UPSTREAM.md` 早就寫著「四個面向都要看」，`upstream_baseline.json` 也記著
`reviewed_pr_through` 與 `reviewed_issue_through`——但**沒有任何程式讀那兩個欄位**，檢查器只比對
commit 水位。那兩個面向不是「查過沒發現」，是根本沒查，而每週的排程報告長得跟查過一樣綠。
這是艦隊層級的問題：24 個 fork 裡 21 個都這樣（`SanHsien/repo-fleet-ops` 的 `docs/INCIDENTS.md`
第十條）。參考實作是 `SanHsien/harness-guard`。

三個性質，缺一不可：

- **`--state all`**：只查 `open` 看不到「開了又關、沒有合併」的 PR，而那正是「上游拒收、但可能對
  本 fork 有價值」的一類——已合併的遲早會經由 commit 抵達，被關掉的永遠不會。
- **`gh` 失敗時回 `None` 不回 `[]`**，報告寫 `Not checked` 並 **fail closed**（exit 2）。
  「沒查到」和「沒有」在綠色報告裡長得一樣，只有一個是真的。
- **`GH_TOKEN`**：`gh` 在 Actions 裡沒有憑證就列舉不到，配上 fail closed 會讓紅燈的意思變成
  「檢查器壞了」而不是「上游有東西」。

**證據**：落地後實跑 `python tools/check_upstream_updates.py`，三個面向都印出水位與待辦數；
本 repo 的 gate 全綠。

**已知代價**：水位以上真的有東西時，每週的 upstream-check 會回 exit 1。那是它該做的事——先前的
綠燈不是「沒有待辦」，是沒有人看。

**觸發條件**：報告列出項目時逐筆讀 diff、把採用／略過理由寫進本檔，然後才推進 baseline 的水位。


## 2026-08-30：上游 issue #1 不引用（上游自己也 NOT_PLANNED）

**決定**：不引用。issue 水位 0 → 1；PR 水位維持 0（實查上游 PR 數為 **0**，是查過為空不是沒查）。

**上游要的是什麼**：`#1` 要一個 `/buddhist` 斜線指令，作為 `/caveman` 的語氣對照——
「calm, contemplative, gently philosophical」「occasional koan or zen-flavored aside」，
明說「只換聲音，技術正確性不變」（tonal / personality command）。

**為什麼不適用**：本 skill 不是語氣模式。`SKILL.md` 的 description 寫的是**工作紀律**，
而且是**由任務情境觸發**、不是由指令觸發：「Use this skill whenever the user asks to *think more
carefully*, verify claims, debug a stubborn problem...」「Trigger this even when the user does not
name Buddhist principles」。把它做成要打指令才生效的語氣皮膚，會把「該驗證時自動生效」這個核心
性質拿掉，換來一個裝飾。

**上游的處置**：2026-05-09 以 `NOT_PLANNED` 關閉——上游自己也沒有要做。

**觸發條件**：本 skill 哪天真的加入語氣／人格模式（現在沒有），或上游重開這個 issue 並實作，
再回來重評。
