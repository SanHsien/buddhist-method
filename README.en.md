# Buddhist Method

<p>
  <a href="README.md">繁體中文</a> ·
  <a href="README.en.md"><strong>English</strong></a>
</p>

[![CI](https://github.com/SanHsien/buddhist-method/actions/workflows/ci.yml/badge.svg)](https://github.com/SanHsien/buddhist-method/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

A skill that encodes six Buddhist epistemic and decision-making principles as practical work disciplines for any LLM-driven workflow. Each principle targets a failure mode models routinely exhibit: stating facts from pattern memory, patching symptoms, acting on stale state, defending a wrong draft, hiding bugs, or capitulating under pressure.

> **This is a Windows-first maintenance fork of [`nai0om/buddhist-method`](https://github.com/nai0om/buddhist-method).** It keeps the MIT license and full git history. Product behaviour follows upstream; this line adds Traditional Chinese docs, a Windows development gate, and commit-by-commit upstream review. See [`FORK.md`](FORK.md), [`docs/UPSTREAM.md`](docs/UPSTREAM.md), and [`REVIEW.md`](REVIEW.md).

This is not a religious framework. It does not require belief, ritual, or commitment to any tradition. The Pali / Thai names stay because they are mnemonic keys — each name retrieves a complete pattern that a paragraph of plain English does not retrieve as cleanly.

The upstream author is Udomsak ([`nai0om`](https://github.com/nai0om)).

## The six principles

| Principle | What it catches |
|-----------|-----------------|
| **Kalāma** (กาลามสูตร) | Stating facts from pattern memory without verifying |
| **Yoniso Manasikāra** (โยนิโสมนสิการ) | Treating symptoms instead of finding root causes |
| **Sati-Sampajañña** (สติ-สัมปชัญญะ) | Acting on stale or remembered state |
| **Anatta** (อนัตตา) | Patching a fundamentally wrong draft instead of rewriting |
| **Pahāna** (ปหานะ) | Workarounds that hide bugs instead of removing them |
| **Upekkhā** (อุเบกขา) | Capitulating under user pressure or thrashing under tool failures |

Deeper references:

- Hard or fuzzy bugs → [`references/ariyasacca-debug.md`](references/ariyasacca-debug.md)
- Retry loops, scope, short vs long term, audience, late-task discipline → [`references/extended-principles.md`](references/extended-principles.md)

## Install the skill

Copy these **product files** into the host skills directory. Everything else in this repo is fork maintenance scaffolding — do not copy it into the skills folder.

| Host | Suggested path |
| --- | --- |
| Cursor | `~/.cursor/skills/buddhist-method/` |
| Claude Code | `~/.claude/skills/buddhist-method/` |
| Codex | `~/.agents/skills/buddhist-method/` |

Files to copy:

- `SKILL.md`
- `references/`

Then say “use buddhist-method before you claim this” or let the host trigger on the skill description. The user does not need to name the Pali terms.

Upstream also ships a one-shot Claude Code install prompt that clones into `~/.claude/skills/buddhist-method` and appends a `CLAUDE.md` pointer. Windows development setup for this fork is below.

```powershell
git clone https://github.com/SanHsien/buddhist-method.git
cd buddhist-method
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements-dev.txt
pwsh -NoProfile -File tools\dev_check.ps1
```

See [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md).

## Source and license

Original work: [nai0om/buddhist-method](https://github.com/nai0om/buddhist-method) (MIT, Copyright Udomsak).
This fork's overlay is also MIT. See [`LICENSE`](LICENSE) and [`NOTICE.md`](NOTICE.md).
The upstream Thai README remains as a product file at [`README.th.md`](README.th.md); this fork's public entrance is Traditional Chinese plus English only.

Maintenance contributions belong in [`CONTRIBUTING.md`](CONTRIBUTING.md). Product-principle changes go to upstream; this fork does not take those PRs.
