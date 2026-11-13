# Skill review checklist

What a good skill does, from Anthropic's "Skill authoring best practices" page and the skill-creator skill. Last checked against that page on 2026-11-13.

## Contents

1. How the skill loads
2. Context cost
3. Instructions
4. Files and links
5. Workflows and scripts
6. Tests
7. Claude Code

## 1. How the skill loads

Claude sees only the `name` and `description` of each installed skill, and picks from them. A skill with a weak description never runs.

- `name` has at most 64 characters: lowercase letters, digits and hyphens. It has no XML tags and no "anthropic" or "claude".
- `name` matches the folder name.
- `name` says the activity, such as `processing-pdfs`. A vague noun such as `helper` or `utils` is a finding.
- `description` has 1 to 1024 characters and no XML tags.
- `description` says what the skill does and when to use it. A "When to use" section in the body is not seen when Claude picks a skill.
- `description` is in the third person or the imperative. "I can help you" is a finding.
- `description` names real triggers: the words people type, file types, tool names and folder names.
- Claude tends to load skills too rarely. "Use this whenever X, even if the user does not say Y" helps.
- `description` says what the skill is not for when a nearby skill does similar work.
- `description` is not so broad that it takes unrelated tasks.

## 2. Context cost

Once loaded, the whole body sits in context next to the conversation.

- Claude is already capable. Each paragraph must give Claude something it would not do anyway. An explanation of what a PDF is costs tokens and changes nothing.
- The body has fewer than about 500 lines. Longer material moves to reference files.
- Nothing is said twice in the body and the reference files.
- There is no history, changelog or "why we built this". That belongs in docs.
- There are no dated rules such as "until August 2025, use the old API". Put old ways in a section named "Old patterns" if they are needed at all.

## 3. Instructions

- A rule comes with its reason. A model that knows the reason handles cases the rule did not list.
- Heavy `ALWAYS`, `NEVER` or `CRITICAL` text is a warning sign. Current models follow instructions closely, and capitals make them apply the rule too widely. Keep strong words for one or two hard limits.
- A rule says what to do, not only what not to do.
- The freedom matches how fragile the task is.
  - Judgement work, such as a review or writing, gets prose guidance.
  - Work with a preferred pattern gets a template with parameters.
  - Work that breaks with a small change, such as a migration or a deploy, gets the exact command or script.
  - A mismatch in either direction is a finding.
- A skill gives a default, not a menu. "Use pypdf, pdfplumber or PyMuPDF" makes runs differ. "Use pdfplumber, and use OCR for scanned pages" does not.
- One word means one thing in the whole skill.
- The output format is given when it matters, with a template or an example.
- Examples of output are concrete pairs of input and output. Tool calls get no examples, per **rule-name-tools-exactly**. They differ enough that Claude does not copy the surface of one.
- No two instructions conflict, and none conflicts with the frontmatter.
- Nothing would surprise the user if said plainly, such as a hidden network call.

## 4. Files and links

- `SKILL.md` is the overview and the router. Detail goes in `references/`, code in `scripts/`, templates in `assets/`.
- `SKILL.md` links each reference file directly, with a sentence on when to read it. A reference that links to another reference often gets only part read.
- A reference file over about 100 lines starts with a table of contents.
- A skill for several domains splits by domain, so only the relevant file loads.
- File names say what is inside, such as `form-rules.md`, not `doc2.md`.
- Paths use forward slashes.
- Every linked file exists, and every file in the folder is used.

## 5. Workflows and scripts

- A task with many steps has numbered steps. A long or risky task gives a checklist that Claude can copy.
- A step that must be right has a loop: run the check, fix, run it again, then go on.
- Destructive or batch work plans first, checks the plan, then runs it.
- For each script, the skill says whether Claude runs it or reads it.
- A script handles its own errors with a useful message.
- A constant in a script says why it has its value. An unexplained `47` is a finding.
- The skill lists the packages a script needs.
- When every run would write the same helper, the skill ships that helper.
- An MCP tool is named with its server prefix, such as `mcp__server__tool`. Without it, Claude may not find the tool.

## 6. Tests

- There is a way to tell that the skill works: an `evals/` folder, example prompts with expected results, or a stated goal.
- There are at least three realistic test prompts. One is a near-miss that should not load the skill.
- A skill for several models was tried on the weakest one. Instructions that work for Opus can be too thin for Haiku.

## 7. Claude Code

Check these only for a skill that runs in Claude Code.

- Optional frontmatter is used correctly when present. Examples are `allowed-tools`, `disable-model-invocation`, `argument-hint` and `model`.
- A skill that the person must start by name sets `disable-model-invocation: true` and says so.
- Personal skills live in `~/.claude/skills/`. Project skills live in `.claude/skills/` and are committed.
- A project skill does not depend on files that exist only on one person's machine.
