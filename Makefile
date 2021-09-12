test:
	PYTHONPATH=. pytest --exitfirst --hypothesis-show-statistics src/ tests/ -vv

format:
	autoflake --remove-all-unused-imports -i **/*.py
	isort **/*.py
	black **/*.py

typecheck:
	mypy src/
