# Write how-to-use

Write a skill under the project's own `.claude/skills/how-to-use-<app>/`. The skill starts the app, uses it the way a person does, and captures proof. It is for a later agent that has never seen the app and follows it cold: launch, check, use one feature, capture, clean up. Ported from pstack's create-verification-skill.

## Steps

1. Read the repo, not the user. Evidence: one line per answer, with the file it came from.
   1. Answer from the code. Ask only what you cannot see.
   2. Answer these five questions:
      - Surface: what a person touches. A web page, a CLI, a desktop app, an API, a library. Pick the main one, and note the rest.
      - Run: how it starts locally. The repo's own command first: a package script, a Makefile target, the README. Ports, env vars, seed data, a login.
      - Use: how an agent can work it. First, what is already there: Playwright specs, curl-able routes, a debug port, a PTY helper. Then the generic recipe: a browser tool for web, a PTY or tmux for a CLI, plain HTTP for a service.
      - Observe: what proof can be captured. Screenshots, terminal output, response bodies, logs, exit codes, rows in a store.
      - Isolate: can two copies run side by side, with their own ports, data dirs and profiles? If not, the skill must say so. Refusing to use a shared copy beats corrupting the person's session.
   3. Start a copy for proof from a scratch config that keeps only what the run needs.
   4. Never carry a live credential along, such as a chat bot's token or a webhook secret. Your copy would then answer the person's real users.
   5. Never let a production build write into the folder a running dev server serves from. The dev server breaks mid-run.
   6. If the checkout does not build or start as is, fix that, or report it exactly, before writing anything. A skill written against a broken base teaches wrong steps.
2. Write `.claude/skills/how-to-use-<app>/SKILL.md`. Evidence: the file, and `wc -l` under 150.
   1. Write the frontmatter: `name: how-to-use-<app>`, and a `description` naming the app, the surface, and when to reach for it.
   2. Then write these sections, each filled from step 1, with no placeholder left:
      - Launch: the exact start command, how to tell it is ready (a log line, a port answering), and how to stop it. For a short-lived CLI, launch means build once. Then each run gets its own fresh session.
      - Doctor: one read-only check that says "this copy is the one to use": process up, right build, port owned by us, login valid. An agent runs it first whenever anything looks off.
      - Use: the recipe with this repo's real handles (ARIA labels, data attributes, prompt strings, route paths), never coordinates or tab order.
      - Evidence: what to capture and where it goes. Use the real user path, not a test-only route. Capture the action and the state after it, not only the final screen. Check side effects beside what is visible: a file written, a row inserted, a message sent. Mock only where a production boundary already isolates the outside system. Check a dry-run mode by watching what it touches, not by trusting its name.
      - Cleanup: how to stop what this run started. Never kill by process name. Kill what you started. Cleanup removes copies and scratch state, never the evidence. The skill names where the evidence lives.
      - Helpers: any script the skill ships is executable, and the body shows its call.
3. Seed the feature map at `.claude/skills/how-to-use-<app>/features/`. Evidence: the file list.
   1. Write a `README.md` index.
   2. Write one file per user-facing feature: the top three to five, from routes, commands, menus or docs.
   3. Copy the shape of the example in `${CLAUDE_PLUGIN_ROOT}/skills/cell-mode/procedures/write-how-to-use/example-feature-map/`. Its index says what each feature file holds.
   4. The map is the repo's maintained list. A proof that uses one convenient entry point is incomplete when the map lists others.
4. Run the skill once yourself, end to end, not through a helper. Evidence: the commands, their output, the evidence path.
   1. Launch.
   2. Run the doctor.
   3. Use one mapped feature. One is enough, because the map exists so later runs cover the rest.
   4. Capture.
   5. Clean up.
   6. After cleanup, confirm the evidence is still at the named place. A cleanup that eats the proof fails this step.
   7. Fix what fails.
   8. Run the cleanup after every failed try too, so nothing is left running.
   9. A skill never run is a draft, not a deliverable.

## Reply

Under twenty lines:

- The surface and the run command, one line each.
- The path of the skill and the features mapped, one line each.
- What step 4 used, and where its evidence is.
- What could not be answered from the repo and was assumed.
- One line pointing at the map as the place to add a feature.
