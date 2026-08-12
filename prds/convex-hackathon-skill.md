# Convex hackathon skill package

- **Created:** 2026-08-12T22:22:03Z
- **Status:** Complete

## Goal

Turn `hackathon-skill.md` into an installable Agent Skill named
`convex-hackathon-skill`. The skill keeps one evidence-based `hackathon.md`
file current while a team builds a Convex hackathon project.

## People

The package must work for a first-time builder, a vibe coder, or an experienced
developer using an Agent Skills-compatible IDE or CLI. Codex, Cursor, and
Factory Droid are named targets.

## Required behavior

- Create `hackathon.md` on first use and update it on later uses.
- Backfill useful history when Git is available.
- Fall back to repository evidence when Git is unavailable.
- Detect Convex features from code and configuration without inflating claims.
- Never copy secrets, personal data, or database records into the public log.
- Make repeated no-change calls idempotent.
- Never commit, push, deploy, or submit on the user's behalf.
- Support natural-language invocation plus each host's native skill syntax.

## Package

- `SKILL.md` with portable `name` and `description` frontmatter only.
- `agents/openai.yaml` for optional Codex and ChatGPT UI metadata.
- One reference file for the exact output format and detection rules.
- A detailed `README.md` with install, use, troubleshooting, and source links.
- Local project records in `files.md`, `changelog.md`, and `task.md`.

## Non-goals

- Submit to a hackathon.
- Judge or score a project.
- Require Convex, Git, GitHub, an MCP server, or a specific shell.
- Publish the package or create Git history in this folder.

## Acceptance checks

- Pass the Codex skill validator.
- Pass a local package test that checks the portable frontmatter and key safety
  instructions.
- Keep `SKILL.md` under 500 lines.
- Verify that every relative file link resolves.
- Verify that no secret-shaped value is stored in the package.
- Delete the original `hackathon-skill.md` only after the user approves it.
