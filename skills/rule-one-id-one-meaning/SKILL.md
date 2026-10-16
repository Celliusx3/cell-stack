---
name: rule-one-id-one-meaning
description: Two ids that hold the same value today stay two names, and one function maps between them. From a correction on 2026-10-11, when a chat's id was passed wherever a bot's id was meant, and the person asked to keep the two independent although they are equal.
disable-model-invocation: true
user-invocable: false
---

# One id, one meaning

## When

A value means one thing to one part of the code and another thing elsewhere (a chat and the bot that answers in it, an order and its invoice, a user and an account), and the two happen to be equal today. Also a parameter or field named for one while it carries the other.

## Rule

Name each id for what it means where it is used, and never pass one where the other is meant. Exactly one function, in the code that owns the relation, maps one to the other, in each direction it is needed; everything else asks it. When the relation changes, that function is the only line that does.

Instead of the tempting thing: do not pass the one you have because it is the other "anyway". The day they differ, every such line is a bug, and none of them says so.

## The test

Search for each place one id is used as the other. Every hit outside the mapping function is a finding.
