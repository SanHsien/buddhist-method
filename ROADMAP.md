# 路線圖

> 本 repo 後續工作的單一真相源。做完一項，就在同一個 commit 刪掉那一列；新工作只加在這裡。
> 現況段的數字是 2026-11-08 依 `main` `6ea02ba` 查的快照，開工前先重查 GitHub。

## 現況

本 repo 用佛教認識論原則約束 Agent 的查證、除錯與抗壓工作紀律，產品為 `SKILL.md` 與 `references/`，沒有獨立 CLI 或後端（`AGENTS.md:7-8,26-30`）。issue 因停用而未查到（2026-10-29 `gh` 查詢）。目前尚未以宿主完整任務證明原則改變行為，裝包與靜態 gate 不能取代該證據（`REVIEW.md`〈尚未宣稱範圍〉）。

2026-11-02 已重審依賴與支援矩陣：保留 Python 3.9–3.14、pytest／ruff 宣告下限；最新相容依賴與 Windows gate 通過，ruff 延後水位更新至 0.17.3（見 `docs/DECISIONS.md` 同日決策）。2026-11-08 重查：open PR 0、Dependabot 與 code scanning open alert 0，`main` 最近的 CI、CodeQL、Dependency freshness 皆 success（`gh pr list`、`gh api .../dependabot/alerts`、`gh run list -b main`）。

## 近期：可以直接動手

| 項目 | 為什麼 | 驗收方式 | 建議執行者 | 證據 |
| --- | --- | --- | --- | --- |
| 在「中途催促」任務上測沒點名時 skill 是否觸發、差異是否來自 skill 內容 | 2026-11-19 第三輪（`docs/SKILL-AB-2026-11-19.md`）找到對照組會走捷徑的任務 C：第二輪催促寫 all passing 時，Haiku 對照組 5/5 照改，明示叫用組 4/5 拒改。但差異只在提示點名 skill 時觀察到，沒有「裝了不點名」與安慰劑組，還不能據此改寫 `description` | 用同一個 fixture 與隔離做法（`docs/SKILL-AB-2026-11-19.md`〈設定〉、〈任務〉），在 Haiku 上加跑兩組各 5 次：裝 skill 但提示不點名；點名一個無關 skill 的安慰劑組。不點名組叫用 skill 少於半數、且行為接近對照組，才改寫 `description`，改寫後在同一任務重測觸發。依原評分表評分，更新 `REVIEW.md` | Claude Opus | `docs/SKILL-AB-2026-11-19.md`；`REVIEW.md`〈尚未宣稱範圍〉 |

## 中期：等條件成立再做

| 項目 | 觸發條件 | 驗收方式 | 建議執行者 | 證據 |
| --- | --- | --- | --- | --- |
| 逐筆審查上游更新 | 上游超出 baseline，或已審項目 head／內容改變 | 跑 `python tools/check_upstream_updates.py --strict`，核對產品原則與 references、記錄取捨；Windows gate 通過後才推進水位 | Codex | `tools/upstream_baseline.json`；`AGENTS.md:47-62`；`docs/UPSTREAM.md`〈審查清冊〉 |
| 補少見 YAML／Markdown 解析案例 | 實際 skill 或維護文件出現 block scalar 指示符、巢狀 scoped grant 或特殊 fence，且產生可重現誤報 | 對實際格式先補回歸案例，維持缺少授權與過長 description 的拒絕行為；Windows gate 通過 | Codex | 深掃報告〈刻意不修〉；`2841b2c`、`4974a01`、`7a429bd` |

## 刻意不做

| 不做什麼 | 理由 | 什麼情況下重新考慮 |
| --- | --- | --- |
| 新增只切換語氣的 `/buddhist` 指令 | 與依任務情境觸發的工作紀律不同；理由見 `docs/DECISIONS.md:98` 起的上游 issue #1 決策 | 產品正式加入語氣模式，或上游重開並實作後再評估 |
| 翻譯產品規格、刪改巴利文／泰文名稱或把泰文檔升為公開入口 | 保留產品與文化助記名稱；公開入口採繁中／英文，見 `AGENTS.md:17-22`、`docs/DECISIONS.md:36-50` | 維護者明確修改產品語言與維護範圍政策 |
| 為維護線另造 CLI、後端或獨立 release 版號 | 現有交付物是宿主讀取的 Markdown skill，沒有此需求證據 | 有可重現的宿主限制或明確分發需求，另訂驗收後 |

## 維護方式

每週依 `docs/UPSTREAM.md` 與 baseline 做增量巡檢；Upstream check 有未審項目時先審查，不盲目推水位，也不為共同祖先問題改寫歷史。
每月查 Dependency freshness、`gh pr list --repo SanHsien/buddhist-method` 與安全告警；工具修改跑 Windows gate，產品改動另驗宿主行為；其他文件只連結本路線圖。
