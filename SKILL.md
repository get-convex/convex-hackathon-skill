---
name: convex-hackathon-skill
description: Create and update an evidence-based hackathon.md build log for a Convex project. Use when a user invokes $convex-hackathon-skill, /convex-hackathon-skill, or /hackathon; mentions a Convex hackathon; asks to start, backfill, refresh, or correct a hackathon build log; or wants submission-ready project history. Work from local repository evidence, keep claims honest, exclude secrets and personal data, and never submit, deploy, or commit.
---

# Convex hackathon skill

Keep one `hackathon.md` file at the project root current while the user builds.
Treat the file as a public, evidence-based build log.

## Interpret the request

Support two actions:

- **Update:** Run for `$convex-hackathon-skill`, `/convex-hackathon-skill`,
  `/hackathon`, or a natural-language request to update the hackathon log.
- **Start:** Run for the same invocation followed by `start`, or an explicit
  request to create the log from existing project history.

If the user requests an update and `hackathon.md` does not exist, start it
automatically. Do not require the user to know the start action.

## Run the workflow

1. Locate the project root.
   - Prefer the result of `git rev-parse --show-toplevel` when Git is available.
   - Otherwise, use the current workspace root.
2. Read `references/log-format.md` before creating or editing `hackathon.md`.
3. Inspect `hackathon.md` if it exists. Preserve factual user corrections and
   the exact header field names.
4. Collect local evidence without changing the project.
   - With Git, inspect commit history, the working tree, staged changes, and
     changed-file summaries. Do not count generated or dependency files as
     product progress.
   - Without Git, inspect source files, configuration, and modification times.
     Treat timestamps as weaker evidence and say so in the entry when needed.
   - Inspect project manifests, Convex configuration, registered components,
     frontend deployment configuration, and relevant source files.
5. Create or update the log.
   - On start, backfill meaningful Git history in chronological order. Group
     tightly related commits from the same work session when that reads better.
   - On update, append one UTC-dated entry for new evidence since the latest
     logged commit or update time.
   - Refresh header facts that changed.
   - Keep entries in plain language and connect detected Convex features to the
     files that show them.
6. Check idempotency before saving.
   - If no commits, staged changes, working-tree changes, or newer source
     evidence exist, leave the file unchanged.
   - Do not add a duplicate entry just to refresh the timestamp.
7. Report the result in a few lines. Show the new entry or say that the log was
   already current.

## Use evidence carefully

- Derive the project name from a manifest, existing product copy, or the folder
  name.
- Derive the repository URL from the configured Git remote when available.
- List a Convex component only when `convex/convex.config.ts` or an equivalent
  config registers it. A dependency alone does not prove use.
- List a Convex feature only when source code or config shows it.
- Record AI model names only when code, config, project docs, or the user's own
  statement identifies them. Do not guess the model that built the app.
- Use `not deployed` for an unknown live app or Convex deployment. Do not stop a
  normal update to ask for a URL. Ask once only when the user requests final
  submission cleanup and the missing fact cannot be detected.
- Omit an unknown event name. Never ask for an event name, date, or access code.
- Prefer `none` over an invented value for components, auth, or AI models.

## Protect public data

Treat `hackathon.md` as public.

- Never open or dump `.env`, `.env.local`, secret stores, deployment keys, or
  credential files to fill the log.
- Read public deployment URLs from checked-in config, source, existing docs, or
  user-provided values. Reading variable names from an example env file is fine;
  do not copy real environment values.
- Never include API keys, tokens, passwords, cookies, private keys, email
  addresses, phone numbers, street addresses, precise coordinates, private host
  names, or application database records.
- Remove secret or personal data from a requested entry and tell the user in one
  line what was omitted.
- Do not call production APIs or query application data to make the log richer.

## Stay inside the boundary

- Edit only `hackathon.md` unless the user asks for another change.
- Never create a Git commit, push, deploy, publish, or submit.
- Do not score the project or promise how judges will evaluate it.
- Do not rewrite older factual entries for tone alone.
- If local evidence conflicts with an existing claim, keep the evidence-based
  value and briefly flag the correction.

## Keep the tone useful

Write as the builder: direct, factual, and brief. Use two to six lines per log
entry when possible. Name shipped behavior before implementation detail. Show
the entry, accept corrections, and return to the build.
