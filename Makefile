.PHONY: help lint check new
help:
	@echo "lint                     the structure rules (scripts/lint.sh)"
	@echo "check                    lint + claude plugin validate"
	@echo "new kind=<k> name=<n>    add a skill: kind is steering|procedure|playbook|principle"

lint:
	scripts/lint.sh

check: lint
	claude plugin validate .

new:
	@test -n "$(kind)" -a -n "$(name)" || { echo "usage: make new kind=<steering|procedure|playbook|principle> name=<kebab-case>"; exit 2; }
	scripts/new-skill.sh $(kind) $(name)
