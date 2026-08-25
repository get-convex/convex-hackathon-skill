# Hackathon log format

Use this reference whenever creating or updating `hackathon.md`.

## Contents

- Header format
- Field rules
- Entry format
- Convex detection guide
- Backfill and update rules

## Header format

Keep these labels and this order. Omit `Event` when it is unknown. Use `none` or
`not deployed` where the field rules allow it.

```markdown
# Hackathon log

- **Project:** StandupSync
- **Event:** Convex + OpenAI Global Hackathon
- **What it does:** Realtime async standups with AI summaries of team blockers.
- **Live app:** https://standupsync.convex.site
- **Repo:** https://github.com/team/standupsync
- **Frontend:** Convex static hosting
- **Convex deployment:** https://standupsync-prod.convex.cloud
- **Components:** @convex-dev/agent, @convex-dev/rate-limiter
- **Convex features:** queries, mutations, actions, crons, full-text search
- **Auth:** Convex Auth
- **AI models:** gpt-5.6
- **Started:** 2026-08-18T14:02:11Z
- **Last updated:** 2026-08-21T09:41:55Z

## Log
```

## Field rules

- **Project:** Use the product name from a manifest or visible app copy. Fall
  back to the folder name.
- **Event:** Use optional free text already supplied by the user or found in
  checked-in project docs. Omit it when unknown.
- **What it does:** Write one factual sentence grounded in the app or its docs.
  Use `Not documented yet` if the purpose cannot be inferred.
- **Live app:** Use one public app URL. Accept `*.convex.site`, `*.chatgpt.site`,
  custom domains, or another public frontend. Use `not deployed` when absent.
- **Repo:** Use a normalized public remote URL, `private`, or `none`.
- **Frontend:** Use `Codex Sites`, `Convex static hosting`, `Vercel`, `Netlify`,
  `Other`, or `not deployed`. Detect it from checked-in deployment config or the
  live host.
- **Convex deployment:** Use a public `*.convex.cloud` URL or `not deployed`.
- **Components:** List only registered `@convex-dev/*` components, or `none`.
- **Convex features:** Use short feature names backed by code, or `none yet`.
- **Auth:** Use `Convex Auth`, `WorkOS`, `Clerk`, `Other`, or `none`. The
  `@convex-dev/auth` package plus `convex/auth.ts` or `convex/auth.config.ts`
  proves Convex Auth; the beta and v2 alpha both use that package. A
  `convex/auth.config.ts` that points at an external provider domain proves the
  named third party provider.
- **AI models:** Record model identifiers backed by evidence, or `none`. A
  `convexGateway("provider/model")` call names the model directly; log that id
  and note it runs through the Convex AI Gateway.
- **Started:** Use the first meaningful commit time. Without Git, use the
  earliest trustworthy source-file modification time. Write UTC ISO 8601.
- **Last updated:** Use the time of the latest logged evidence. Write UTC ISO
  8601. Do not change it on a no-op run.

## Entry format

Append entries oldest to newest. Use a short commit SHA when Git exists. Use the
date alone without Git.

```markdown
### 2026-08-18 - 3f2a91c
Set up teams, members, and standups with indexes on teamId and postedAt. Added
the first query and mutation for posting a standup. Convex features: schema,
indexes, query, mutation (`convex/schema.ts`, `convex/standups.ts`).
```

For a working tree update without a new commit, label the entry `working tree`:

```markdown
### 2026-08-21 - working tree
Added the submission screen and wired it to the existing create mutation
(`src/components/SubmissionForm.tsx`).
```

Do not add another `working tree` entry for the same unchanged diff. Update the
existing entry only when the uncommitted work itself changed and remains part of
the same work session.

## Convex detection guide

Use code and configuration as proof. Match equivalent imports and names when a
project wraps the Convex APIs.

| Evidence | Log as |
|---|---|
| `defineSchema`, `defineTable` | schema, tables |
| `.index(` | indexes |
| `.searchIndex(` | full-text search |
| `.vectorIndex(` or vector search calls | vector search |
| `query`, `internalQuery` | queries |
| `mutation`, `internalMutation` | mutations |
| `action`, `internalAction` | actions |
| `httpAction`, `httpRouter` | HTTP actions |
| `crons` | crons |
| `ctx.scheduler` | scheduled functions |
| `storage.` | file storage |
| `useQuery` | realtime queries |
| `usePaginatedQuery` | paginated queries |
| `app.use(` in `convex.config.ts` | registered component |
| `@convex-dev/auth` plus `convex/auth.ts` or `auth.config.ts` | Convex Auth |
| `convex/auth.config.ts` naming an external provider domain | that provider in Auth |
| `convexGateway(` in an action | AI Gateway; its argument is the model id |

Check all manifest dependency sections when identifying auth and component
packages. Search nested manifests in monorepos. A package name proves only that
the package is present; require configuration or source use before claiming the
feature is active.

## Backfill and update rules

- Use chronological Git history for a start backfill.
- Skip mechanical commits that only change generated output, lockfiles without
  a dependency change, or formatting without behavior changes.
- Group commits only when they form one clear unit and retain the newest SHA in
  the heading so the next update has a stable boundary.
- Inspect both committed and uncommitted work on an update.
- Summarize behavior first, then name the main files and Convex features.
- Do not claim a deployment, integration, model, component, or feature without
  local evidence or an explicit user statement.
- Preserve user-written corrections unless newer evidence disproves them.
