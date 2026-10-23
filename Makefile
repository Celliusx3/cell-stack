.PHONY: help lint check rule eval
help:
	@echo "lint                     the structure rules (scripts/lint.sh)"
	@echo "check                    lint + claude plugin validate"
	@echo "rule name=<n>            add a rule: copies templates/rule.md and lists it in cell-mode"
	@echo "eval                     run the blinded cases in evals/ (claude plugin eval)"

lint:
	scripts/lint.sh

check: lint
	for f in hooks/*.sh; do bash -n "$$f" || exit 1; done
	claude plugin validate .

rule:
	@test -n "$(name)" || { echo "usage: make rule name=<kebab-case>"; exit 2; }
	scripts/new-rule.sh $(name)

eval:
	claude plugin eval . --scaffold --allow-tools Bash Edit Write
