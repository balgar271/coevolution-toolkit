# Contributing to CoEvolution Toolkit

Thank you for your interest in contributing to the CoEvolution Toolkit! This document provides guidelines for contributing to the project.

## 🌟 Ways to Contribute

1. **Report Bugs**: Open an issue describing the bug
2. **Suggest Features**: Propose new features via issues
3. **Fix Issues**: Pick an issue and submit a PR
4. **Improve Documentation**: Enhance README, docstrings, examples
5. **Add Examples**: Create new tutorial notebooks
6. **Optimize Code**: Improve performance, readability

## 🚀 Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/coevolution-toolkit.git
cd coevolution-toolkit
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

## 📝 Development Guidelines

### Code Style

We follow [PEP 8](https://pep8.org/) with some modifications:

- **Line length**: 100 characters (not 79)
- **Indentation**: 4 spaces
- **Docstrings**: NumPy style

```python
def example_function(param1: float, param2: np.ndarray) -> float:
    """
    Brief description of function.
    
    Parameters
    ----------
    param1 : float
        Description of param1
    param2 : ndarray
        Description of param2
        
    Returns
    -------
    float
        Description of return value
        
    Examples
    --------
    >>> result = example_function(1.0, np.array([1, 2, 3]))
    >>> print(result)
    6.0
    """
    return param1 * np.sum(param2)
```

### Code Formatting

Use `black` for automatic formatting:

```bash
black coevolution_toolkit/
```

### Linting

Check code quality with `flake8`:

```bash
flake8 coevolution_toolkit/ --max-line-length=100
```

### Type Hints

Add type hints where appropriate:

```python
from typing import Optional, Tuple, List

def process_data(data: np.ndarray, 
                 threshold: float = 0.5) -> Tuple[np.ndarray, int]:
    """Process data with optional threshold."""
    ...
```

## 🧪 Testing

### Writing Tests

Tests go in `tests/` directory:

```python
# tests/test_core.py
import pytest
import numpy as np
from coevolution_toolkit import CosmologicalBackground

def test_cosmology_initialization():
    """Test cosmological background initialization."""
    cosmo = CosmologicalBackground()
    assert cosmo.Omega_m0 > 0
    assert cosmo.H0 > 0

def test_hubble_parameter():
    """Test Hubble parameter calculation."""
    cosmo = CosmologicalBackground()
    H_0 = cosmo.H(0)
    H_1 = cosmo.H(1)
    assert H_1 > H_0  # Universe was denser in past
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=coevolution_toolkit --cov-report=html

# Run specific test file
pytest tests/test_core.py

# Run specific test
pytest tests/test_core.py::test_cosmology_initialization
```

## 📚 Documentation

### Docstrings

All public functions/classes must have docstrings in NumPy style:

```python
class NewProfile(DensityProfile):
    """
    New density profile model.
    
    This profile implements the XYZ model from Smith et al. (2024).
    
    Parameters
    ----------
    r_array : ndarray
        Radial coordinates [kpc]
    param1 : float
        First parameter [units]
    param2 : float, optional
        Second parameter [units], default: 1.0
        
    Attributes
    ----------
    r : ndarray
        Radial array
    param1 : float
        Stored parameter
        
    Examples
    --------
    >>> r = np.linspace(0.1, 10, 100)
    >>> profile = NewProfile(r, param1=5.0)
    >>> rho = profile.rho()
    
    References
    ----------
    .. [1] Smith et al. (2024), ApJ, 900, 123
    """
    ...
```

### Updating README

If you add a new feature, update `README.md`:
- Add to feature list
- Add usage example
- Update API documentation section

## 🔄 Pull Request Process

### 1. Before Submitting

- [ ] Code passes all tests (`pytest`)
- [ ] Code is formatted (`black`)
- [ ] Code passes linting (`flake8`)
- [ ] New features have tests
- [ ] Documentation is updated
- [ ] Commit messages are clear

### 2. Commit Messages

Use clear, descriptive commit messages:

```
[TYPE] Brief description

Detailed explanation if necessary.

Fixes #123
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding/updating tests
- `chore`: Maintenance tasks

**Examples**:
```
feat: Add Einasto profile implementation

Implements Einasto density profile following Einasto (1965).
Includes tests and example usage in tutorial.

Closes #45
```

```
fix: Correct adiabatic contraction convergence

Fixes numerical instability in AC solver for extreme mass ratios.
Added checks for r_final > 0 and improved initial guess.

Fixes #67
```

### 3. Submit Pull Request

1. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. Go to GitHub and create a Pull Request

3. Fill out the PR template:
   - **Description**: What does this PR do?
   - **Motivation**: Why is this change needed?
   - **Testing**: How was it tested?
   - **Related Issues**: Fixes #XXX

4. Wait for review and address comments

### 4. Review Process

- Maintainers will review within 1-2 weeks
- You may be asked to make changes
- Once approved, PR will be merged

## 🐛 Reporting Bugs

Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md).

**Include**:
- Python version
- Operating system
- Toolkit version
- Minimal reproducible example
- Expected vs. actual behavior
- Error messages/tracebacks

## 💡 Suggesting Features

Use the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md).

**Include**:
- Clear description of feature
- Use case / motivation
- Possible implementation approach
- Examples of similar features elsewhere

## 📖 Examples and Tutorials

### Adding Examples

Create new `.py` files in `examples/`:

```python
"""
Example: Custom Galaxy Evolution
=================================

This example shows how to model a custom galaxy scenario.
"""

import numpy as np
from coevolution_toolkit import ...

# Your example code here
```

### Adding Tutorials

Create new Jupyter notebooks in `tutorials/`:

```jupyter
# Tutorial: Advanced Feedback Mechanisms

This tutorial covers...

## 1. Introduction
...

## 2. Setup
...
```

## 🏷️ Issue Labels

- `bug`: Something isn't working
- `enhancement`: New feature request
- `documentation`: Documentation improvements
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention needed
- `question`: Further information requested
- `wontfix`: This will not be worked on

## 💬 Communication

- **Issues**: For bugs, features, questions
- **Pull Requests**: For code contributions
- **Discussions**: For general questions (coming soon)

## 📜 Code of Conduct

Be respectful, inclusive, and professional. We follow the [Contributor Covenant](https://www.contributor-covenant.org/).

## 🙏 Acknowledgments

Contributors will be acknowledged in:
- `README.md` Contributors section
- Release notes
- Academic citations (for significant contributions)

## ❓ Questions?

If you're unsure about anything:
1. Check existing issues and documentation
2. Open an issue with the `question` label
3. Reach out to maintainers

---

**Thank you for contributing to CoEvolution Toolkit!** 🌌

Your contributions help advance our understanding of cosmic structure formation and the interplay between visible and dark matter.
