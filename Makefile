SRC := $(shell find {ml-recipes,tests,references} -name "*.py")

test:
	@poetry run pytest --exitfirst --hypothesis-show-statistics

lint:
	@poetry run ruff check $(SRC)

format:
	@poetry run autoflake --remove-all-unused-imports -i $(SRC)
	@poetry run isort $(SRC)
	@poetry run black --line-length 100 $(SRC)

typecheck:
	@poetry run mypy src/ tests/

clean:
	rm -rf **/__pycache__
	rm -rf **/.ipynb_checkpoints
	rm -rf .mypy_cache
	rm -rf .hypothesis
	rm -rf .pytest_cache
