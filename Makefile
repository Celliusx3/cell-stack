.PHONY: help lint check new eval
help:
	@echo "lint                     the structure rules (scripts/lint.sh)"
	@echo "check                    lint + claude plugin validate"
	@echo "new kind=<k> name=<n>    add a skill: kind is steering|procedure|playbook|rule"
	@echo "eval                     run the blinded cases in evals/ (claude plugin eval)"

lint:
	scripts/lint.sh

check: lint
	bash -n hooks/comment-nag.sh hooks/session-start.sh
	claude plugin validate .

new:
	@test -n "$(kind)" -a -n "$(name)" || { echo "usage: make new kind=<steering|procedure|playbook|rule> name=<kebab-case>"; exit 2; }
	scripts/new-skill.sh $(kind) $(name)

eval:
	claude plugin eval . --scaffold --allow-tools Bash Edit Write
