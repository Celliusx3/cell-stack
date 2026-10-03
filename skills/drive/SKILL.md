---
name: drive
description: Write a repo-local skill that starts the app, drives it the way a person does, and captures proof. Use for /drive, "make a drive skill for this repo", "how do I verify the UI", or when a Verify step has no scripted way to prove a screen or a command. Ported from pstack's create-verification-skill.
disable-model-invocation: true
---

# Drive

A skill under the project's own `.claude/skills/drive-<app>/` that a later agent, one that has never seen the app, can follow cold: launch, check, drive one feature, capture, clean up. Written for that agent, not for a person.

## Steps

1. Read the repo, not the user. Answer from the code and ask only what you cannot see. Evidence: one line per answer, with the file it came from.
   - Surface: what a person touches. A web page, a CLI, a desktop app, an API, a library. Pick the main one and note the rest.
   - Run: how it starts locally. The repo's own command first (a package script, a Makefile target, the README). Ports, env vars, seed data, a login.
   - Drive: how an agent can work it. What is already there first (Playwright specs, curl-able routes, a debug port, a PTY helper), then the generic recipe: a browser tool for web, a PTY or tmux for a CLI, plain HTTP for a service.
   - Observe: what proof can be captured. Screenshots, terminal output, response bodies, logs, exit codes, rows in a store.
   - Isolate: can two copies run side by side (ports, data dirs, profiles)? If not, the skill must say so; refusing to drive a shared copy beats corrupting the person's session. A copy started for proof runs from a scratch config that keeps only what the run needs: a live credential carried along (a chat bot's token, a webhook secret) makes your copy answer the person's real users. A production build never writes into the folder a running dev server serves from, or the dev server breaks mid-drive.
   If the checkout does not build or start as is, fix that or report it exactly before writing anything; a skill written against a broken base teaches wrong steps.
2. Write `.claude/skills/drive-<app>/SKILL.md`. Frontmatter is `name: drive-<app>` and a `description` naming the app, the surface, and when to reach for it. Then these sections, each filled from step 1, no placeholder left:
   - Launch: the exact start command, how to tell it is ready (a log line, a port answering), and how to stop it. For a short-lived CLI, launch means build once, then each drive gets its own fresh session.
   - Doctor: one read-only check that says "this copy is worth driving": process up, right build, port owned by us, login valid. An agent runs it first whenever anything looks off.
   - Drive: the recipe with this repo's real handles (ARIA labels, data attributes, prompt strings, route paths), never coordinates or tab order.
   - Evidence: what to capture and where it goes. Drive the real user path, not a test-only route; capture the action and the state after it, not only the final screen; check side effects (a file written, a row inserted, a message sent) beside what is visible; mock only where a production boundary already isolates the outside system. A dry-run mode is checked by watching what it touches, not by trusting its name.
   - Cleanup: how to stop what this run started. Never kill by process name; kill what you started. Cleanup removes copies and scratch state, never the evidence; the skill names where the evidence lives.
   - Helpers: any script the skill ships is executable and its call is shown in the body.
   Evidence: the file, and `wc -l` under 150.
3. Seed the feature map at `.claude/skills/drive-<app>/features/`: a `README.md` index and one file per user-facing feature, the top three to five from routes, commands, menus or docs. Copy the shape in `references/feature-map/`: each file has an H1, one paragraph on what a person sees, then exactly four H2s, `Sub-features`, `How to get to it (user POV)`, `Driving it with <harness>`, `Gotchas`. The map is the repo's maintained list; a proof that drives one convenient entry point is incomplete when the map lists others. Evidence: the file list.
4. Run the skill once, end to end: launch, doctor, drive one mapped feature (one is enough; the map exists so later runs cover the rest), capture, clean up. After cleanup, confirm the evidence is still at the named place; a cleanup that eats the proof fails this step. Fix what fails and run the cleanup after every failed try too, so nothing is left running. A skill never run is a draft, not a deliverable. Evidence: the commands, their output, the evidence path.
5. Reply.

## Subagents

None. The whole procedure runs in the main conversation, since step 4 must be driven and watched by the agent that wrote step 2.

## Reply

Under twenty lines. The surface and the run command, one line each. The path of the skill and the features mapped, one line each. What step 4 drove and where its evidence is. What could not be answered from the repo and was assumed. One line pointing at the map as the place to add a feature.
