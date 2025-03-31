# Cookiecutter UV Python

一个使用 UV 包管理器的现代化 Python 项目模板。

## 快速开始

### 1. 安装依赖

首先确保你的系统已安装：
- Python 3.13 或更高版本
- UV 包管理器
- Make 工具
- direnv (可选，用于自动激活虚拟环境)

### 2. 创建新项目

```bash
# 安装 cookiecutter
pip install cookiecutter

# 使用模板创建新项目
cookiecutter https://github.com/yourusername/cookiecutter-uv-python.git
```

### 3. 项目初始化

```bash
# 进入项目目录
cd your-project-name

# 初始化开发环境
make setup      # 创建虚拟环境并安装基础依赖
make dev-setup  # 安装开发依赖
```

## Make 命令使用指南

项目使用 Makefile 管理常见的开发任务，以下是主要命令：

### 开发环境管理
```bash
make setup      # 创建虚拟环境并安装基础依赖
make dev-setup  # 安装开发依赖
make clean      # 清理临时文件（构建文件、缓存等）
```

### 代码质量
```bash
make format     # 使用 ruff 格式化代码
make lint       # 使用 ruff 检查代码
```

### 测试
```bash
make test       # 运行测试
```

### 构建与发布
```bash
make build      # 构建项目包
make release    # 发布到 PyPI
```

### 文档
```bash
make docs       # 生成文档
```

### 帮助信息
```bash
make help       # 显示所有可用命令
```

### macOS 特定优化
```bash
make macos-optimize  # 运行 macOS 特定的优化命令
```

## 项目结构

```
{{ cookiecutter.project_slug }}/
├── {{ cookiecutter.project_slug }}/     # 主包目录
├── tests/                              # 测试目录
├── cli.py                             # CLI 入口点
├── pyproject.toml                     # 项目配置
├── Makefile                          # 开发任务管理
├── .gitignore                        # Git 忽略规则
└── README.md                         # 项目文档
```

## 开发工具

- 🚀 UV: 现代化的 Python 包管理器
- 🛠️ Ruff: 代码检查和格式化
- 📊 Pytest: 单元测试框架
- ⌨️ Typer: CLI 应用开发
- 📦 Make: 任务自动化
- 🔄 direnv: 自动激活虚拟环境

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 作者

- Qlong (wql1994513@gmail.com) 