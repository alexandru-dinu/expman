SRC := $(shell find {opskrift,tests,references} -name "*.py")

test:
	@poetry run pytest --exitfirst --hypothesis-show-statistics

lint:
	@poetry run ruff check $(SRC)

format:
	@poetry run autoflake --remove-all-unused-imports -i $(SRC)
	@poetry run isort $(SRC)
	@poetry run black --line-length 100 $(SRC)

typecheck:
	@poetry run mypy opskrift/ tests/

build-docs:
	rm -rfv docs/sources/reference
	rm -rfv docs/sources/template
	poetry run python3 docs/gen_references.py
	poetry run mkdocs build --config-file docs/mkdocs.yml
	(cd docs/build && git add ./ && git commit -m "Rebuild site." && git push -u origin site)

clean:
	rm -rf **/__pycache__
	rm -rf **/.ipynb_checkpoints
	rm -rf .mypy_cache
	rm -rf .hypothesis
	rm -rf .pytest_cache
