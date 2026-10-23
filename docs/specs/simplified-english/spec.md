# Every text for a person, in the spirit of ASD-STE100

## Problem

Cell mode asks for short sentences, but it gives no word limit and nothing counts the words. A plan can put five actions in one step, use three words for one thing, and hold a 70-word sentence. The spec, the tickets, the grill questions, the replies, and the commit and PR text have the same gaps. The cellstack pages use the same long style, and the model copies the style it reads.

## What changes for you

1. You ask Claude, in plan mode, to fix small photos that the vision model reads badly.
2. Claude reads the plan page. The plan page points at the Writing section of the mode.
3. Claude writes each step of the plan with one action. A step can add one sentence for its result.
4. Claude picks one word for each thing, for example "photo", and uses only that word.
5. Claude saves the plan. A hook counts the words in each sentence.
6. If a sentence is too long, the hook tells Claude to split it before you see the plan.
7. You read each line one time and say yes or no.

The spec, the tickets, the grill questions, the replies, and the commit and PR text follow the same Writing section. Every cellstack page is rewritten in the same style, with the same meaning.

## Decisions

- An instruction or a numbered step has 20 words at most. Any other sentence has 25 words at most. A paragraph has six sentences at most. ASD-STE100 Issue 9 (rules 5.1, 6.3 and 6.6), PostHog, AminBlg/SimpleEnglish, danyuchn/asd-ste100-skill and AsherHou/asd-ste100-for-coding use the same numbers.
- Each numbered step has one action. Two actions share a step only when they happen at the same time. A step can add one sentence for its result. ASD-STE100 rule 5.2 and AminBlg/SimpleEnglish say the same.
- A condition comes before its instruction. The ASD-STE100 FAQ and AminBlg/SimpleEnglish say the same.
- Each text uses one word for one thing. The ASD-STE100 FAQ, AsherHou/asd-ste100-for-coding and danyuchn/asd-ste100-skill say the same.
- The rules are in the spirit of ASD-STE100 only. There is no STE word list. The ASD-STE100 FAQ and AsherHou/asd-ste100-for-coding say the same.
- The rules are one short section of the mode, which is always in context. AminBlg/SimpleEnglish found that an 8-line prompt was better than its full skill for a reader.
- The rules are not a rule page. Three evals pass when Claude reads any rule page, and each reply would read this page.
- The word count includes list items. AminBlg/SimpleEnglish found that the model puts all text in bullets when list items do not count. Syntaf/vale-llm-slop also counts list items.
- The hook only gives a message. It never stops a write. The hook of AminBlg/SimpleEnglish does the same.
- A playbook keeps its numbered steps and their numbers. The one-action sub-steps go under each step. ASD-STE100 rule 5.2 numbers and letters the work steps.
- Word limits replace line limits for pages: 950 words for a playbook, 2,700 for the mode, and 1,100 for each other page. Words are what goes into context.
- Cellstack writes its own rules and does not adopt danyuchn/asd-ste100-skill or AminBlg/SimpleEnglish. Lint allows only one skill, and the AminBlg/SimpleEnglish reply rules ban numbered lists.

## Out of scope

- The STE word list.
- The wording of the eval graders, because only the judge model reads them.
- The specs that are already in this folder, because they are a record of past work.
- A release, and the update of the installed copy of cellstack.

## How we will know it works

- You run make check after each ticket. It passes.
- You run the long-sentences script on each page that a ticket rewrites. It finds no long sentence.
- You run the meaning script on each rewritten page against the commit before this work. It finds no lost path, rule name, number, quoted phrase or heading.
- You add a 30-word sentence to the plan page. Lint fails and names the file and the line.
- You write a plan with a 30-word sentence. The hook gives a message about it.
- You run the Explain eval. Its reply has no sentence longer than the limits.
- You run the full eval suite at the end. It passes at the same rate as the baseline or better.
