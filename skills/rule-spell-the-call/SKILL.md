---
name: rule-spell-the-call
description: Text a model follows (a skill, a tool description, a system prompt) spells each call exactly, with its name and arguments, and carries one worked example that a test runs. From a failed skill reuse on 2026-09-24, and a project's prompt ledger that recorded the same fix earlier.
disable-model-invocation: true
---

# Spell the call

## When

Writing or editing anything a model reads and then acts on: a skill's body, a tool's description, a system prompt, a template the model copies into files of its own. Not a doc written for people.

## Rule

Write every call the model must make exactly as it must type it, with the tool's real name and its arguments: `skill({ name: "notes", path: "references/style.md" })`, not "read it with the skill tool". Keep one worked example of the whole task, and run that example in a test, so what the model copies is known to work. A step that names no call leaves the model guessing a tool name, and the name is exactly what it invents.

Instead of the tempting thing: do not describe a call in prose because its name feels obvious.

## The test

Read each step as the model will. Could it act without guessing a name, an argument or a shape? Does a test fail when the example stops working?

## Example

A saved skill said "Read `scripts/convert.ts` with the skill tool". In a new conversation the model called `unit_convert__read_file` six times, a name no tool has, then guessed the answer. The skill that teaches skill-writing was changed to show `skill({ name: "unit-convert", path: "scripts/convert.ts" })`; the skills it writes now carry that line, and the next two conversations ran the script first time (22.0462 pounds for 10 kg). Its example script is run by a test, so changing one factor in it fails the suite. A project's prompt ledger records the same repair for a memory skill five days earlier: told only to read the functions first, the model skipped the read until the step gave the exact call.
