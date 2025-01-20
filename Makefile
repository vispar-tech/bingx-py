# Makefile

# Formatting and linting
format:
	ruff check . --fix
	@echo "✅ Formatting and linting complete!"

# Type checking
typecheck:
	pyright . --warnings
	@echo "✅ Type checking complete!"

# Running tests
test:
	python -m unittest tests/*.py -v
	@echo "✅ Tests complete!"

# Building documentation
documentation:
	cd docs && make html
	cd ..
	@echo "✅ Documentation built! Open docs/build/html/index.html"

# Installing pre-commit hooks
install-hooks:
	pre-commit install
	@echo "✅ Pre-commit hooks installed!"

# Running all checks (formatting, linting, type checking)
check-all: format typecheck
	@echo "✅ All checks complete!"
