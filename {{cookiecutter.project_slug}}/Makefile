.PHONY: setup dev-setup format lint test clean build docs release

# 检测操作系统
UNAME := $(shell uname)

# 默认 Python 解释器
PYTHON = python3

# 项目名称
PROJECT_NAME = {{ cookiecutter.project_slug }}

# 虚拟环境相关
VENV_NAME = .venv
ifeq ($(UNAME), Darwin)
    VENV_ACTIVATE = . $(VENV_NAME)/bin/activate
else
    VENV_ACTIVATE = source $(VENV_NAME)/bin/activate
endif

# 帮助信息
help:
	@echo "Available commands:"
	@echo "  make setup      - 创建虚拟环境并安装依赖"
	@echo "  make dev-setup  - 安装开发依赖"
	@echo "  make format     - 使用 ruff 格式化代码"
	@echo "  make lint       - 使用 ruff 检查代码"
	@echo "  make test       - 运行测试"
	@echo "  make clean      - 清理临时文件"
	@echo "  make build      - 构建项目包"
	@echo "  make docs       - 生成文档"
	@echo "  make release    - 发布到 PyPI"

# 创建虚拟环境并安装依赖
setup:
	@echo "Creating virtual environment..."
	@uv venv $(VENV_NAME) -p $(PYTHON)
	@echo "Installing dependencies..."
	@uv pip install -e "."
	@echo "Setting up direnv..."
	@echo "source .venv/bin/activate" > .envrc
	@direnv allow .
	@echo "Setup complete. Activate the virtual environment with: $(VENV_ACTIVATE)"

# 安装开发依赖
dev-setup: setup
	@echo "Installing development dependencies..."
	@uv pip install -e ".[dev]"
	@echo "Development setup complete."

# 格式化代码
format:
	@echo "Formatting code with ruff..."
	@ruff format $(PROJECT_NAME) tests

# 代码质量检查
lint:
	@echo "Linting code with ruff..."
	@ruff check $(PROJECT_NAME) tests --fix

# 运行测试
test:
	@echo "Running tests..."
	@pytest -xvs tests/

# 清理临时文件
clean:
	@echo "Cleaning up..."
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info
	@rm -rf .pytest_cache/
	@rm -rf .coverage
	@rm -rf .ruff_cache/
	@find . -type d -name __pycache__ -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@echo "Clean complete."

# 构建项目包
build: clean
	@echo "Building package..."
	@uv pip install build
	@python3 -m build

# 生成文档
docs:
	@echo "Building documentation..."
	@cd docs && make html
	@echo "Documentation built in docs/build/html/"

# 发布到 PyPI
release: build
	@echo "Releasing to PyPI..."
	@uv pip install twine
	@twine upload dist/*

# macOS 特定优化
ifeq ($(UNAME), Darwin)
macos-optimize:
	@echo "Optimizing for macOS..."
	@# macOS 特定的优化命令
else
macos-optimize:
	@echo "Not on macOS, skipping optimization."
endif
