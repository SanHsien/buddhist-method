<div align="center">

# Buddhist Method

### 把佛法編成 Agent 的工作紀律：講事實前先核對，除錯先找根因，壓力變大時不要輕易改立場

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Platform: Claude Code](https://img.shields.io/badge/Platform-Claude%20Code-f97316.svg)](https://code.claude.com/)
[![Platform: Codex](https://img.shields.io/badge/Platform-Codex-10a37f.svg)](https://developers.openai.com/codex/skills)
[![Platform: Cursor](https://img.shields.io/badge/Platform-Cursor-000000.svg)](https://cursor.com/)
[![CI](https://github.com/SanHsien/buddhist-method/actions/workflows/ci.yml/badge.svg)](https://github.com/SanHsien/buddhist-method/actions/workflows/ci.yml)

<p>
  <a href="README.md"><strong>繁體中文</strong></a> ·
  <a href="README.en.md">English</a>
</p>

</div>

> **這是 [`nai0om/buddhist-method`](https://github.com/nai0om/buddhist-method) 的 Windows-first 維護型 fork**，沿用 MIT 授權與完整 Git 歷史。產品 Skill 與 `references/` 跟隨上游；本維護線補上繁中入口、Windows 開發／驗收 gate，以及逐筆審查的上游追蹤。差異見 [`FORK.md`](FORK.md)，同步策略見 [`docs/UPSTREAM.md`](docs/UPSTREAM.md)，風險快照見 [`REVIEW.md`](REVIEW.md)。

這不是宗教框架。它不要求信仰、儀式或歸屬任何傳統。它是一份有文化根源的檢查清單：針對 LLM 常見的失敗模式——憑訓練記憶講事實、修症狀不修成因、在社交壓力下放棄證據。

上游作者是泰國開發者 Udomsak（[`nai0om`](https://github.com/nai0om)）。原則名稱保留巴利文／泰文，因為那是助記鍵：一個名字能喚回整套模式，一段英文翻譯喚不回來。

## 六條原則

| 原則 | 抓住什麼 |
|---|---|
| **Kalāma**（迦羅摩經／กาลามสูตร） | 憑模式記憶講事實，沒有剛查過 |
| **Yoniso Manasikāra**（如理作意／โยนิโสมนสิการ） | 看到錯誤就先找「讓訊息消失」的補丁 |
| **Sati-Sampajañña**（正念正知／สติ-สัมปชัญญะ） | 憑記得剛才檔案長怎樣去動作 |
| **Anatta**（無我／อนัตตา） | 方向錯了還捨不得整份丟掉，只敢小修 |
| **Pahāna**（斷／ปหานะ） | 捷徑只是把問題藏起來，沒有移除成因 |
| **Upekkhā**（捨／อุเบกขา） | 使用者強力反駁或工具連失敗三次，就因壓力改立場 |

更難的情況看 `references/`：

- 難纏或說不清的 bug → [`references/ariyasacca-debug.md`](references/ariyasacca-debug.md)（四聖諦當除錯框架）
- 重試迴圈、範圍不對、短長期取捨、聽眾不清、長任務後半失守 → [`references/extended-principles.md`](references/extended-principles.md)

## 安裝 Skill（本機呼叫）

把這些**產品檔**一起放到 Agent Skills 目錄。根目錄其餘檔案是本 fork 的開發與治理骨架，不要一起複製進去。

| 宿主 | 建議路徑 |
| --- | --- |
| Cursor | `~\.cursor\skills\buddhist-method\` |
| Claude Code | `~\.claude\skills\buddhist-method\` |
| Codex | `~\.agents\skills\buddhist-method\` |

需要複製的檔案：

- `SKILL.md`
- `references/`

安裝後可直接說：「用 buddhist-method 先核對這件事再動手」，或讓宿主依 description 自行觸發。觸發不需要使用者喊出巴利文名稱——驗證、找根因、壓力下不退讓，都是一般工作紀律。

上游另提供貼進 Claude Code 的一鍵安裝提示（clone 到 `~/.claude/skills/buddhist-method` 並在 `CLAUDE.md` 加指標）。本 fork 的 Windows 開發環境見下方。

開發與驗收指令見 [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md)。維護者 clone：

```powershell
git clone https://github.com/SanHsien/buddhist-method.git
cd buddhist-method
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements-dev.txt
pwsh -NoProfile -File tools\dev_check.ps1
```

## 為什麼保留巴利文／泰文名稱

巴利文名稱是故意留的。它們是助記鍵——學會之後，一個名字能喚回完整、發展成熟的模式，一段普通英文做不到。《Yoniso manasikāra》帶進來的是「把注意力對準成因」整套紀律；翻成「root cause analysis」會丟掉「注意力本身」這個框架。

這跟工程師學 sigmoid 而不是「那個彎彎的函數」是同一件事：名字是基礎設施。

若要讀原則在傳統裡的完整深度，去讀經。這個 skill 不宣稱在教那些。

## 來源與授權

原作：[nai0om/buddhist-method](https://github.com/nai0om/buddhist-method)（MIT，Copyright Udomsak）。
本 fork 的 overlay 同樣以 MIT 發佈，見 [`LICENSE`](LICENSE) 與 [`NOTICE.md`](NOTICE.md)。
上游泰文說明見產品檔 [`README.th.md`](README.th.md)；本 fork 的公開入口只維護繁中與英文。

貢獻本 fork 的維護骨架見 [`CONTRIBUTING.md`](CONTRIBUTING.md)。產品原則的實質改動請開到上游，**不要**把產品 PR 開到這個 fork。
