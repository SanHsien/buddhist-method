English | [中文版](CHANGELOG.md)

# Changelog

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); newest first.
This file records **this fork's maintenance history** only (from 2026-08-28). The product
history of upstream
[`nai0om/buddhist-method`](https://github.com/nai0om/buddhist-method) lives in its
own history and in the review ledger at [`docs/UPSTREAM.md`](docs/UPSTREAM.md). Per-commit
adopt/skip reasoning is recorded in [`docs/DECISIONS.md`](docs/DECISIONS.md).

---

## 2026-08-28 (fix review findings)

### Fixed

- **Visitor routing.** `README.th.md` contributing now states this is the SanHsien
  maintenance fork and product PRs belong upstream. `CONTRIBUTING.md` plus issue / PR
  templates say this line does not take product-principle PRs. No upstream PR.

## 2026-08-28 (full-repo review)

### Added

- **`REVIEW.md` risk snapshot.** Conclusion, evidence (local gate + GitHub Actions URLs), closed findings, accepted contract, checked-but-not-findings, and what this review does not claim. It is not a log of every ordinary bug.

### Changed

- This review found **no new P1/P2 to fix.** Overlay commit `83a577f` is green on CI, CodeQL, upstream check, and dependency freshness. Product `SKILL.md` / `references/` match upstream HEAD. No upstream PR.

## 2026-08-28

### Added

- **Windows-first maintenance overlay.** Full `.github/` set (issue / PR templates,
  Dependabot, CI, CodeQL, dependency freshness, upstream check), `.gitignore`,
  `AGENTS.md`, `CLAUDE.md`, `FORK.md`, `NOTICE.md`, `CONTRIBUTING.md`, `SECURITY.md`,
  `CODE_OF_CONDUCT.md`, `docs/`, `tools/`, and `tests/`. CI runs Ubuntu 3.9–3.14 and
  Windows 3.14: pytest, ruff (E9+F), `validate_skill.py`, link check.
- **Public entrance is Traditional Chinese plus English only.** `README.md` is the
  Chinese primary file; `README.en.md` is the English mirror. Source and license
  credit stay. Upstream `README.th.md` remains a product file, not a third public
  language; its English pointer now targets `README.en.md`.
- **`LICENSE` adds this fork's overlay copyright line.** The original Udomsak MIT
  notice is kept.
