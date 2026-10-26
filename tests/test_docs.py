from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import check_links  # noqa: E402
import validate_skill  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
PRODUCT_PATHS = (
    SKILL,
    ROOT / "references" / "ariyasacca-debug.md",
    ROOT / "references" / "extended-principles.md",
    ROOT / "README.th.md",
    ROOT / "LICENSE",
)


def test_skill_frontmatter_is_installable() -> None:
    errors, _warns = validate_skill.audit(str(SKILL), lens="claude")
    assert errors == []


def test_skill_name_is_stable() -> None:
    text = SKILL.read_text(encoding="utf-8")
    assert "name: buddhist-method" in text
    assert "Kalāma" in text
    assert "Yoniso Manasikāra" in text
    assert "Sati-Sampajañña" in text
    assert "Anatta" in text
    assert "Pahāna" in text
    assert "Upekkhā" in text


def test_product_pack_files_exist() -> None:
    missing = [str(path.relative_to(ROOT)) for path in PRODUCT_PATHS if not path.is_file()]
    assert missing == []


def test_maintainer_markdown_links_resolve() -> None:
    failures = 0
    for path in check_links.iter_documents():
        problems = check_links.check_document(path)
        failures += len(problems)
        for problem in problems:
            print(f"{path}: {problem}")
    assert failures == 0


def test_skill_referenced_pack_paths_exist() -> None:
    problems = check_links.check_skill_paths()
    assert problems == []
    text = SKILL.read_text(encoding="utf-8")
    assert "references/ariyasacca-debug.md" in text
    assert "references/extended-principles.md" in text


def test_skill_path_checker_flags_missing_reference(tmp_path: Path) -> None:
    skill = tmp_path / "SKILL.md"
    skill.write_text("讀取 `references/missing-file.md`。\n", encoding="utf-8")
    problems = check_links.check_skill_paths(skill)
    assert problems
    assert "references/missing-file.md" in problems[0]


def test_ci_covers_python_314() -> None:
    workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert '"3.14"' in workflow
    assert "windows / py3.14" in workflow
    assert "scripts" not in workflow


def test_public_docs_are_traditional_chinese_and_english_only() -> None:
    """Fork 公開入口只留繁中與英文；上游泰文 README 當產品檔保留，不當第三入口。"""
    assert (ROOT / "README.th.md").is_file()
    for name in ("README.md", "README.en.md"):
        text = (ROOT / name).read_text(encoding="utf-8")
        assert "README.ja.md" not in text
        assert "日本語" not in text
    zh = (ROOT / "README.md").read_text(encoding="utf-8")
    en = (ROOT / "README.en.md").read_text(encoding="utf-8")
    assert "README.en.md" in zh
    assert "README.md" in en
    # 泰文原檔可被點名為產品檔，但不得成為 fork 公開入口的第三語系切換列。
    assert "README.th.md" in zh
    assert "> 🇹🇭" not in zh
    assert "> 🇹🇭" not in en
    thai = (ROOT / "README.th.md").read_text(encoding="utf-8")
    assert "README.en.md" in thai
    assert "Read [README.md](README.md) for the English version" not in thai


def test_readme_keeps_credit_without_author_promotion() -> None:
    zh = (ROOT / "README.md").read_text(encoding="utf-8")
    en = (ROOT / "README.en.md").read_text(encoding="utf-8")
    for name, text in (("README.md", zh), ("README.en.md", en)):
        assert "nai0om/buddhist-method" in text, name
        assert "NOTICE.md" in text, name
        assert "MIT" in text, name
        assert "Udomsak" in text, name
    assert "SanHsien/buddhist-method" in zh
    assert r"~\.cursor\skills\buddhist-method" in zh
    assert "~/.cursor/skills/buddhist-method/" in en
    assert "License: MIT" in zh


def test_bilingual_pairs_cross_link_each_other() -> None:
    for zh_name, en_name in (("README.md", "README.en.md"), ("CHANGELOG.md", "CHANGELOG.en.md")):
        zh = ROOT / zh_name
        en = ROOT / en_name
        assert zh.is_file(), f"missing {zh_name}"
        assert en.is_file(), f"missing {en_name}"
        assert en_name in zh.read_text(encoding="utf-8"), f"{zh_name} does not link {en_name}"
        assert zh_name in en.read_text(encoding="utf-8"), f"{en_name} does not link {zh_name}"


def test_changelog_records_fork_history_not_upstream_product_history() -> None:
    text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "docs/UPSTREAM.md" in text
    assert "docs/DECISIONS.md" in text
    assert "nai0om/buddhist-method" in text


def test_tool_config_matches_ci_flags() -> None:
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    ci = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert 'target-version = "py39"' in pyproject
    assert "--target-version py39" in ci
    assert 'select = ["E9", "F"]' in pyproject
    assert "--select E9,F" in ci
    assert not re.search(r"^\[project\]", pyproject, re.M)
    assert not re.search(r"^\[build-system\]", pyproject, re.M)


def test_review_snapshot_has_required_sections() -> None:
    text = (ROOT / "REVIEW.md").read_text(encoding="utf-8")
    assert "## 結論" in text
    assert "## 已修 findings" in text
    assert "## 接受、不改契約" in text
    assert "## 尚未宣稱範圍" in text
    assert "不回貢" in text
    assert "MIT" in text


def test_fork_license_is_mit() -> None:
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    notice = (ROOT / "NOTICE.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert license_text.startswith("MIT License")
    assert "Copyright (c) 2026 Udomsak" in license_text
    assert "Copyright (c) 2026 SanHsien" in license_text
    assert "MIT" in notice
    assert "MIT" in readme
    assert "License: MIT" in readme


def test_line_endings_are_pinned_to_lf() -> None:
    attrs = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    assert "* text=auto eol=lf" in attrs
    for suffix in ("*.md", "*.py", "*.ps1"):
        assert suffix in attrs


def test_gitignore_covers_secrets_and_reports() -> None:
    text = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert ".env" in text
    assert ".venv/" in text
    assert "upstream-review-report.md" in text
    assert "cookies.txt" in text
    assert "credentials.json" in text


def test_tracked_files_are_not_git_symlinks() -> None:
    result = subprocess.run(
        ["git", "ls-files", "-s"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    symlinks = [
        line.split("\t", 1)[-1]
        for line in result.stdout.splitlines()
        if line.startswith("120000 ")
    ]
    assert symlinks == [], f"git symlink 會讓 Windows checkout 失敗: {symlinks}"


def test_check_links_rejects_path_outside_repo(tmp_path: Path) -> None:
    doc = tmp_path / "note.md"
    doc.write_text("[here](.)\n", encoding="utf-8")
    problems = check_links.check_document(doc)
    assert any("逃出" in item for item in problems)


def test_issue_contact_links_point_at_this_fork() -> None:
    text = (ROOT / ".github" / "ISSUE_TEMPLATE" / "config.yml").read_text(
        encoding="utf-8"
    )
    assert "SanHsien/buddhist-method" in text
    assert "nai0om/buddhist-method" in text
    assert "不要開到這個 fork" in text


def test_contribution_guides_reject_product_prs_on_this_fork() -> None:
    contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    assert "不收產品原則 PR" in contributing
    pr_template = (ROOT / ".github" / "pull_request_template.md").read_text(
        encoding="utf-8"
    )
    assert "不收產品原則 PR" in pr_template
    thai = (ROOT / "README.th.md").read_text(encoding="utf-8")
    assert "does not take product-principle PRs" in thai
    assert "SanHsien/buddhist-method" in thai
    zh = (ROOT / "README.md").read_text(encoding="utf-8")
    en = (ROOT / "README.en.md").read_text(encoding="utf-8")
    assert "不要" in zh and "產品 PR" in zh
    assert "does not take those PRs" in en


def _audit_frontmatter(tmp_path: Path, frontmatter: str, body: str = "body\n"):
    skill = tmp_path / "SKILL.md"
    skill.write_text(f"---\n{frontmatter}\n---\n{body}", encoding="utf-8")
    return validate_skill.audit(str(skill), lens="claude")


def test_inline_allowed_tools_accept_comma_and_flow_lists(tmp_path: Path) -> None:
    for value in ("Read, Grep", "[Read, Grep]", "Read Grep"):
        errors, warns = _audit_frontmatter(
            tmp_path, f"name: a\ndescription: x\nallowed-tools: {value}"
        )
        assert errors == [], value
        assert warns == [], value


def test_inline_allowed_tools_keep_scoped_bash_grant_whole(tmp_path: Path) -> None:
    errors, warns = _audit_frontmatter(
        tmp_path,
        "name: a\ndescription: x\nallowed-tools: Bash(python3 *), Read",
        body="```bash\npython3 run.py\n```\n",
    )
    assert errors == []
    assert warns == []


def test_block_scalar_description_is_measured_not_read_as_indicator(tmp_path: Path) -> None:
    long_text = "word " * 250
    errors, _warns = _audit_frontmatter(
        tmp_path, f"name: a\ndescription: >\n  {long_text}\n"
    )
    assert any("description" in item and "1024" in item for item in errors)


def test_block_scalar_description_that_fits_passes(tmp_path: Path) -> None:
    errors, _warns = _audit_frontmatter(
        tmp_path, "name: a\ndescription: |-\n  first line\n  second line"
    )
    assert errors == []
    assert validate_skill.get_scalar(
        "description: >-\n  first\n  second\nname: a", "description"
    ) == "first second"


def test_check_links_accepts_link_title(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(check_links, "ROOT", tmp_path)
    (tmp_path / "a.md").write_text("x", encoding="utf-8")
    doc = tmp_path / "note.md"
    doc.write_text('[t](a.md "Title") and [u](a.md#top \'T2\')\n', encoding="utf-8")
    assert check_links.check_document(doc) == []


def test_check_links_ignores_examples_in_code(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(check_links, "ROOT", tmp_path)
    doc = tmp_path / "note.md"
    doc.write_text(
        "```\n[x](nope.md)\n```\n\n`[y](nope2.md)`\n\n[real](missing.md)\n",
        encoding="utf-8",
    )
    problems = check_links.check_document(doc)
    assert len(problems) == 1
    assert "missing.md" in problems[0]
