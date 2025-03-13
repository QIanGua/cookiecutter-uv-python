"""Tests for {{ cookiecutter.project_name }}."""

import pytest  # 导入 pytest
from {{cookiecutter.project_slug}} import __version__


def test_version():
    """Test version is defined."""
    # 使用 pytest 的 assert 语句来验证版本
    with pytest.raises(AssertionError):  # 这里我们使用 raises 来捕获 AssertionError
        assert __version__ != "0.1.0"  # 反向断言, 确保版本是正确的
