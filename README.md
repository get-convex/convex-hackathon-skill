# Convex hackathon skill

Keep a public `hackathon.md` build log current from the work already in your
Convex project.

The skill reads local repository evidence, writes the first log, backfills Git
history when it can, and adds later progress without asking you to remember what
changed. It does not commit, deploy, submit, score, or read your application
database.

## What it does

Run one skill while you build. It maintains one file at the root of your app:

```text
your-app/
└── hackathon.md
```

That file records:

- what the project does and where it runs
- the repository, frontend host, Convex deployment, auth, and AI models
- registered Convex components and features that appear in the code
- a dated build log backed by commits or local file evidence

The first run creates the file. A late first run can backfill earlier commits.
Later runs add only new evidence. A run with no changes leaves the file alone.

## Who this is for

**New to coding:** You get a readable project diary without learning Git history
commands first.

**Vibe coding:** Call the skill after a building session. It turns the changes
your agent made into a short, public record.

**Experienced developer:** Use the log as a low-maintenance submission artifact.
Entries keep commit boundaries, file evidence, and Convex feature names visible
without adding a release-notes system to the app.

## Install

The package follows the open Agent Skills format. The shared `.agents/skills`
location works with Codex, Cursor, and Factory Droid. Claude Code reads
`.claude/skills` in a project and `~/.claude/skills` for your account, so use
that path there instead.

### Install for one project

The skill needs two files: `SKILL.md` and `references/log-format.md`. Download
them straight from this repository into your app.

Codex, Cursor, Factory Droid, and other `.agents/skills` agents:

```bash
mkdir -p .agents/skills/convex-hackathon-skill/references
curl -fsSL https://raw.githubusercontent.com/get-convex/convex-hackathon-skill/main/SKILL.md \
  -o .agents/skills/convex-hackathon-skill/SKILL.md
curl -fsSL https://raw.githubusercontent.com/get-convex/convex-hackathon-skill/main/references/log-format.md \
  -o .agents/skills/convex-hackathon-skill/references/log-format.md
```

Claude Code:

```bash
mkdir -p .claude/skills/convex-hackathon-skill/references
curl -fsSL https://raw.githubusercontent.com/get-convex/convex-hackathon-skill/main/SKILL.md \
  -o .claude/skills/convex-hackathon-skill/SKILL.md
curl -fsSL https://raw.githubusercontent.com/get-convex/convex-hackathon-skill/main/references/log-format.md \
  -o .claude/skills/convex-hackathon-skill/references/log-format.md
```

Cloning the repository into the same folder works too. Keep `SKILL.md` and the
`references/` subfolder together. `SKILL.md` loads `references/log-format.md`
while it works.

### Install for your user account

Install once for all projects with a clone.

macOS or Linux:

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/get-convex/convex-hackathon-skill.git \
  "$HOME/.agents/skills/convex-hackathon-skill"
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills"
git clone https://github.com/get-convex/convex-hackathon-skill.git `
  "$HOME\.agents\skills\convex-hackathon-skill"
```

For Claude Code, clone into `$HOME/.claude/skills/convex-hackathon-skill`
instead.

Restart the IDE or CLI if it was open during installation.

### Use another IDE or CLI

Any tool that supports the [Agent Skills specification](https://agentskills.io/specification)
can load this package from its documented skills directory. If an agent does not
support skills yet, attach or open the full folder and prompt it with:

```text
Read SKILL.md in convex-hackathon-skill and follow it to update this project's
hackathon.md from local repository evidence.
```

Native discovery and invocation depend on the host. The workflow itself uses
plain Markdown, local files, and optional Git commands. It has no MCP server,
package-manager, runtime, API key, or Convex account dependency.

## Use

Open your Convex app in the IDE or start the CLI from the app folder. Then use
the syntax your agent supports.

| Tool | First or normal update | Explicit backfill |
|---|---|---|
| Codex app, IDE, or CLI | `$convex-hackathon-skill` | `$convex-hackathon-skill start` |
| Cursor IDE or CLI | `/convex-hackathon-skill` | `/convex-hackathon-skill start` |
| Claude Code | `/convex-hackathon-skill` | `/convex-hackathon-skill start` |
| Factory Droid | `/convex-hackathon-skill` | `/convex-hackathon-skill start` |
| Other compatible agent | `Update my Convex hackathon log` | `Start and backfill my Convex hackathon log` |

You can also keep using `/hackathon`. The skill treats it as the short update
request when the host passes that text to the skill.

Typical flow:

1. Build part of your app.
2. Invoke the skill.
3. Review the entry it shows you.
4. Correct any product wording that does not sound like you.
5. Repeat after the next building session.

You do not need to run `start` first. A normal update creates the file when it is
missing.

## What the log looks like

```markdown
# Hackathon log

- **Project:** StandupSync
- **What it does:** Realtime async standups with AI summaries of team blockers.
- **Live app:** https://standupsync.convex.site
- **Repo:** https://github.com/team/standupsync
- **Frontend:** Convex static hosting
- **Convex deployment:** https://standupsync-prod.convex.cloud
- **Components:** @convex-dev/agent
- **Convex features:** queries, mutations, actions, crons
- **Auth:** Convex Auth
- **AI models:** gpt-5.6
- **Started:** 2026-08-18T14:02:11Z
- **Last updated:** 2026-08-21T09:41:55Z

## Log

### 2026-08-21 - 8bc0d44
Wired the Agent component to summarize each day's thread. Added a cron that
posts the summary at 5pm team time (`convex/convex.config.ts`,
`convex/crons.ts`, `convex/summarize.ts`).
```

The example shows the shape, not required services. Your project can use no
auth, no AI model, another frontend, a private repo, or no deployment yet.

## How evidence works

With Git, the skill reads commit history, the current diff, staged changes, and
changed-file summaries. Each committed entry keeps a short SHA so the next run
has a clear starting point.

Without Git, it uses source files, checked-in configuration, and file times. It
marks weaker timestamp-based conclusions instead of pretending they came from
commit history.

Convex features are tied to code. For example, `defineTable` supports a table
claim, `.vectorIndex` supports a vector-search claim, and `app.use` in
`convex/convex.config.ts` supports a component claim. Installing a package does
not prove the app uses it.

## Privacy and safety

Assume `hackathon.md` will be public.

The skill does not open real env files to fill the log. It also excludes API
keys, tokens, passwords, cookies, private keys, personal contact details,
private host names, precise locations, and database records. Public app and
`*.convex.cloud` URLs are allowed when they appear in checked-in evidence or the
user supplies them.

The skill edits only `hackathon.md`. It does not create a commit, push, deploy,
publish, or submit. Those stay separate user decisions.

## Troubleshooting

### The skill does not appear

- Confirm the folder is named `convex-hackathon-skill`.
- Confirm it contains `SKILL.md` directly inside it.
- Confirm the package is under `.agents/skills` in the project or
  `~/.agents/skills` for your user account. In Claude Code, use
  `.claude/skills` or `~/.claude/skills`.
- Restart the IDE or CLI, then inspect its skill list.

### The agent runs the wrong action

Use the full skill name and action:

```text
$convex-hackathon-skill start
```

In Cursor, Claude Code, or Droid, use `/convex-hackathon-skill start`.

### The log repeats an entry

Ask the agent to compare the latest logged SHA and any existing `working tree`
entry against the current repository before saving. A no-change run should not
edit the file.

### A field is unknown

The skill uses `none`, `not deployed`, or omits the optional event field. Give
it the missing fact in your next prompt if you want the header filled sooner.

### The project is private

Use `private` for the Repo field. The log does not need a public GitHub URL.
Follow the event's own rules for submitting private work.

## Package files

- `SKILL.md`: the workflow agents load
- `references/log-format.md`: output format and Convex evidence map
- `agents/openai.yaml`: optional Codex and ChatGPT display metadata
- `tests/validate_skill.py`: local package checks for maintainers
- `LICENSE`: MIT terms for reuse and redistribution

## References

- [Agent Skills specification](https://agentskills.io/specification)
- [OpenAI: build skills for Codex](https://developers.openai.com/codex/skills)
- [Cursor Agent Skills](https://cursor.com/docs/skills)
- [Factory Droid skills](https://docs.factory.ai/harness/skills)
- [Convex TypeScript best practices](https://docs.convex.dev/understanding/best-practices/typescript)
- [Convex development workflow](https://docs.convex.dev/understanding/workflow)
- [Convex query functions](https://docs.convex.dev/functions/query-functions)
- [Convex mutation functions](https://docs.convex.dev/functions/mutation-functions)
- [Convex actions](https://docs.convex.dev/functions/actions)
- [Convex scheduled functions](https://docs.convex.dev/scheduling/scheduled-functions)
- [Convex file storage](https://docs.convex.dev/file-storage)
- [Convex vector search](https://docs.convex.dev/search/vector-search)
- [Convex components](https://docs.convex.dev/components)

## One next step

Install it locally, open a Convex project, and run your first update.
