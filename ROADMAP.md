# 路線圖

> 本 repo 後續工作的單一真相源。做完一項，就在同一個 commit 刪掉那一列；新工作只加在這裡。
> 現況段的數字是 2026-11-08 依 `main` `6ea02ba` 查的快照，開工前先重查 GitHub。

## 現況

本 repo 用佛教認識論原則約束 Agent 的查證、除錯與抗壓工作紀律，產品為 `SKILL.md` 與 `references/`，沒有獨立 CLI 或後端（`AGENTS.md:7-8,26-30`）。issue 因停用而未查到（2026-10-29 `gh` 查詢）。2026-11-19 的宿主對照實驗只在 Haiku、明示叫用 skill 時觀察到行為改變（被催促時維持證據）；不點名時不會自動觸發，改寫 `description` 也沒改變這點（`docs/SKILL-AB-2026-11-19.md`、`REVIEW.md`〈尚未宣稱範圍〉）。裝包與靜態 gate 不能取代這類證據。

2026-11-02 已重審依賴與支援矩陣：保留 Python 3.9–3.14、pytest／ruff 宣告下限；最新相容依賴與 Windows gate 通過，ruff 延後水位更新至 0.17.3（見 `docs/DECISIONS.md` 同日決策）。2026-11-08 重查：open PR 0、Dependabot 與 code scanning open alert 0，`main` 最近的 CI、CodeQL、Dependency freshness 皆 success（`gh pr list`、`gh api .../dependabot/alerts`、`gh run list -b main`）。

## 近期：可以直接動手

目前沒有。

## 中期：等條件成立再做

| 項目 | 觸發條件 | 驗收方式 | 建議執行者 | 證據 |
| --- | --- | --- | --- | --- |
| 補少見 YAML／Markdown 解析案例 | 實際 skill 或維護文件出現 block scalar 指示符、巢狀 scoped grant 或特殊 fence，且產生可重現誤報 | 對實際格式先補回歸案例，維持缺少授權與過長 description 的拒絕行為；Windows gate 通過 | Codex | 深掃報告〈刻意不修〉；`2841b2c`、`4974a01`、`7a429bd` |
| 逐筆審查上游更新 | 觸發條件已成立（2026-11-21 查：`python tools/check_upstream_updates.py --strict` exit 1：上游新 PR #2、#3 待分流（commit 軸無新 commit）；`Upstream check` 2026-11-20 failure）。原條件：上游超出 baseline，或已審項目 head／內容改變 | 跑 `python tools/check_upstream_updates.py --strict`，核對產品原則與 references、記錄取捨；Windows gate 通過後才推進水位 | Codex | `tools/upstream_baseline.json`；`AGENTS.md:47-62`；`docs/UPSTREAM.md`〈審查清冊〉 |

## 刻意不做

| 不做什麼 | 理由 | 什麼情況下重新考慮 |
| --- | --- | --- |
| 新增只切換語氣的 `/buddhist` 指令 | 與依任務情境觸發的工作紀律不同；理由見 `docs/DECISIONS.md:98` 起的上游 issue #1 決策 | 產品正式加入語氣模式，或上游重開並實作後再評估 |
| 翻譯產品規格、刪改巴利文／泰文名稱或把泰文檔升為公開入口 | 保留產品與文化助記名稱；公開入口採繁中／英文，見 `AGENTS.md:17-22`、`docs/DECISIONS.md:36-50` | 維護者明確修改產品語言與維護範圍政策 |
| 改寫 `SKILL.md` 的 `description` 讓它更容易自動觸發 | 2026-11-19 第四輪（`docs/SKILL-AB-2026-11-19.md`〈第四輪〉）：Haiku 不點名時原 description 0/5 叫用，改寫候選也 0/5，未達事先定的採用條件（叫用 ≥ 3/5 且紅 ≥ 3/5）；差異只在點名時出現，安慰劑點名不會出現。改產品檔會偏離上游，沒有足夠證據當 fork 修正 | 另一個模型或宿主上，有改寫版本在同一隔離做法下把不點名叫用率拉到多數，且行為差異隨之出現；或上游自行改 description |
| 為維護線另造 CLI、後端或獨立 release 版號 | 現有交付物是宿主讀取的 Markdown skill，沒有此需求證據 | 有可重現的宿主限制或明確分發需求，另訂驗收後 |

## 維護方式

每週依 `docs/UPSTREAM.md` 與 baseline 做增量巡檢；Upstream check 有未審項目時先審查，不盲目推水位，也不為共同祖先問題改寫歷史。
每月查 Dependency freshness、`gh pr list --repo SanHsien/buddhist-method` 與安全告警；工具修改跑 Windows gate，產品改動另驗宿主行為；其他文件只連結本路線圖。
