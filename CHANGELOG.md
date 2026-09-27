[English](CHANGELOG.en.md) | 中文版

# 變更紀錄

格式參考 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.1.0/)，新的在上面。
本檔只記錄**本 fork 的維護歷史**（2026-08-28 起）；上游
[`nai0om/buddhist-method`](https://github.com/nai0om/buddhist-method)
的產品演進見其自身歷史與 [`docs/UPSTREAM.md`](docs/UPSTREAM.md) 的審查清冊。
逐筆採用／略過的理由記在 [`docs/DECISIONS.md`](docs/DECISIONS.md)。

---

## 2026-08-28（覆核可修項）

### 修復

- **訪客導流。** `README.th.md` 共同開發段標明這是 SanHsien 維護 fork，產品 PR 去上游。
  `CONTRIBUTING.md`、Issue／PR 模板改成「本線不收產品原則 PR」。不回貢。

## 2026-08-28（全庫覆核）

### 新增

- **`REVIEW.md` 覆核快照。** 結論、本輪實證（本機 gate + GitHub Actions URL）、已修 findings、接受不改契約、已檢查不列 finding、尚未宣稱範圍。不是每個一般 bug 的流水帳。

### 變更

- 本輪覆核**沒有**新的 P1／P2 要改。overlay 首推 `83a577f` 的 CI／CodeQL／Upstream check／Dependency freshness 全綠。產品 `SKILL.md`／`references/` 與上游 head 相同。本輪不回貢。

## 2026-08-28

### 新增

- **`fork` Windows-first 維護骨架。** `.github/` 全套（issue／PR 模板、dependabot、
  CI、CodeQL、相依新鮮度、上游檢查 workflow）、`.gitignore`、`AGENTS.md`、`CLAUDE.md`、
  `FORK.md`、`NOTICE.md`、`CONTRIBUTING.md`、`SECURITY.md`、`CODE_OF_CONDUCT.md`、`docs/`、
  `tools/`、`tests/`。CI 跑 Ubuntu 3.9–3.14 與 Windows 3.14：pytest、ruff（E9+F）、
  `validate_skill.py`、連結檢查。
- **公開入口只留繁中與英文。** `README.md` 改繁中主檔、`README.en.md` 為英文鏡像。
  來源與授權 credit 保留。上游泰文 `README.th.md` 當產品檔保留，不當第三語系入口；
  語言指標改指 `README.en.md`。
- **`LICENSE` 加本 fork overlay 的 Copyright 行。** 原作 Udomsak 的 MIT 標示保留。
