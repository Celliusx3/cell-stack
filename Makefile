.PHONY: help lint check rule eval
help:
	@echo "lint                     the structure rules (scripts/lint.sh)"
	@echo "check                    lint + claude plugin validate"
	@echo "rule name=<n>            add a rule: copies templates/rule.md and lists it in cell-mode"
	@echo "eval                     run the blinded cases in evals/ (claude plugin eval)"

lint:
	scripts/lint.sh

check: lint
	bash -n hooks/comment-nag.sh hooks/session-start.sh hooks/sentence-nag.sh
	claude plugin validate .

rule:
	@test -n "$(name)" || { echo "usage: make rule name=<kebab-case>"; exit 2; }
	scripts/new-rule.sh $(name)

eval:
	claude plugin eval . --scaffold --allow-tools Bash Edit Write
