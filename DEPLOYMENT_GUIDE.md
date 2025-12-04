# 🚀 DEPLOYMENT GUIDE
## Wie Sie das Repository auf GitHub veröffentlichen

**Datum**: 4. Dezember 2025  
**Status**: ✅ Repository vollständig bereit für Deployment

---

## 📦 KOMPLETTE STRUKTUR

```
github_repo/
├── .github/
│   ├── workflows/
│   │   └── ci.yml                    # GitHub Actions CI/CD
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md            # Bug Report Template
│   │   └── feature_request.md       # Feature Request Template
│   └── pull_request_template.md     # PR Template
├── coevolution_toolkit/
│   ├── __init__.py                  # Paket-Init (2.4 KB)
│   ├── core.py                      # Fundamental (13 KB)
│   ├── feedback.py                  # Mechanismen (13 KB)
│   ├── observables.py               # Größen (11 KB)
│   ├── visualization.py             # Plots (12 KB)
│   ├── Tutorial.ipynb               # Jupyter Tutorial (16 KB)
│   └── README.md                    # Toolkit-Docs (7.6 KB)
├── setup.py                         # pip Installation
├── requirements.txt                 # Dependencies
├── .gitignore                       # Git Ignore Rules
├── LICENSE                          # MIT License
├── CONTRIBUTING.md                  # Contribution Guidelines
└── README.md                        # GitHub README mit Badges

GESAMT: 14 Dateien, ~100 KB
```

---

## 🔧 SCHRITT-FÜR-SCHRITT ANLEITUNG

### 1. **GitHub Repository erstellen**

```bash
# Option A: Via GitHub Web Interface
# 1. Gehe zu https://github.com/new
# 2. Repository Name: coevolution-toolkit
# 3. Description: Python toolkit for VM-DM coevolution analysis
# 4. Public/Private: Wählen Sie
# 5. NICHT initialisieren mit README (Sie haben schon einen)
# 6. Create repository

# Option B: Via GitHub CLI
gh repo create coevolution-toolkit --public --description "Python toolkit for VM-DM coevolution"
```

### 2. **Lokales Git Repository initialisieren**

```bash
cd /path/to/github_repo

# Git initialisieren
git init

# Alle Dateien hinzufügen
git add .

# Initial commit
git commit -m "Initial commit: CoEvolution Toolkit v1.0.0

- Core module with coupled evolution equations
- Feedback mechanisms (SNe, AGN, adiabatic contraction)
- Observables (SHMR, rotation curves, cores)
- Visualization functions
- Comprehensive documentation
- Tutorial notebook
- CI/CD with GitHub Actions
- Full test suite setup"

# Branch umbenennen zu main
git branch -M main
```

### 3. **Mit GitHub verbinden und pushen**

```bash
# Remote hinzufügen (ersetze YOURUSERNAME)
git remote add origin https://github.com/YOURUSERNAME/coevolution-toolkit.git

# Pushen
git push -u origin main
```

### 4. **GitHub Actions aktivieren**

- Gehe zu: `Settings` → `Actions` → `General`
- Aktiviere: "Allow all actions and reusable workflows"
- Der CI/CD Workflow startet automatisch beim nächsten Push

### 5. **Issues und Discussions aktivieren**

```
Settings → Features:
☑ Issues
☑ Discussions (optional)
☐ Wiki (optional)
☐ Projects (optional)
```

### 6. **Branch Protection Rules** (empfohlen)

```
Settings → Branches → Add rule:
Branch name pattern: main
☑ Require pull request reviews before merging
☑ Require status checks to pass before merging
  - CI / test (ubuntu-latest, 3.10)
☑ Require branches to be up to date before merging
```

---

## 📦 PyPI DEPLOYMENT (Optional)

### Vorbereitung

```bash
# Build-Tools installieren
pip install build twine

# Package bauen
python -m build

# Ergebnis: dist/coevolution_toolkit-1.0.0.tar.gz
#          dist/coevolution_toolkit-1.0.0-py3-none-any.whl
```

### Test auf TestPyPI

```bash
# Hochladen zu TestPyPI
twine upload --repository testpypi dist/*

# Testen
pip install --index-url https://test.pypi.org/simple/ coevolution-toolkit
```

### Veröffentlichung auf PyPI

```bash
# Hochladen zu PyPI
twine upload dist/*

# Fertig! Jetzt installierbar via:
pip install coevolution-toolkit
```

---

## 🏷️ RELEASES

### GitHub Release erstellen

```bash
# Tag erstellen
git tag -a v1.0.0 -m "Release v1.0.0: Initial public release"
git push origin v1.0.0

# Oder via GitHub Web Interface:
# Releases → Create a new release
# Tag: v1.0.0
# Title: CoEvolution Toolkit v1.0.0
# Description: [Kopiere aus CHANGELOG]
# Attach: dist/*.whl, dist/*.tar.gz
```

### Release Notes Template

```markdown
# CoEvolution Toolkit v1.0.0

**Initial public release** 🎉

## ✨ Features

- Coupled VM-DM evolution solver
- Feedback mechanisms (SNe, AGN, adiabatic contraction)
- Observable predictions (SHMR, rotation curves, cores)
- Publication-quality visualizations
- Interactive Jupyter tutorial
- Comprehensive test suite

## 📦 Installation

```bash
pip install coevolution-toolkit==1.0.0
```

## 📚 Documentation

- [README](README.md)
- [Tutorial](coevolution_toolkit/Tutorial.ipynb)
- [Contributing](CONTRIBUTING.md)

## 🙏 Acknowledgments

Based on relational cosmology framework uniting physics and philosophy.

**Full Changelog**: Initial release
```

---

## 📊 BADGES AKTUALISIEREN

Nach Deployment, aktualisiere Badges in README.md:

```markdown
[![CI](https://github.com/YOURUSERNAME/coevolution-toolkit/workflows/CI/badge.svg)](https://github.com/YOURUSERNAME/coevolution-toolkit/actions)
[![codecov](https://codecov.io/gh/YOURUSERNAME/coevolution-toolkit/branch/main/graph/badge.svg)](https://codecov.io/gh/YOURUSERNAME/coevolution-toolkit)
[![PyPI version](https://badge.fury.io/py/coevolution-toolkit.svg)](https://pypi.org/project/coevolution-toolkit/)
```

Ersetze `YOURUSERNAME` mit Ihrem GitHub Username.

---

## 🔐 SECRETS FÜR CI/CD (Optional)

Für automatisches PyPI Deployment:

```
Settings → Secrets → Actions → New repository secret:

Name: PYPI_API_TOKEN
Value: [Your PyPI token]
```

Dann in `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
    - run: |
        pip install build twine
        python -m build
        twine upload dist/* -u __token__ -p ${{ secrets.PYPI_API_TOKEN }}
```

---

## 📈 CODECOV INTEGRATION (Optional)

1. Gehe zu https://codecov.io
2. Melde dich mit GitHub an
3. Füge Repository hinzu
4. Kopiere Token
5. Füge als Secret hinzu: `CODECOV_TOKEN`

---

## 🌐 ZENODO DOI (Optional)

Für akademische Zitation:

1. Gehe zu https://zenodo.org
2. Login mit GitHub
3. Aktiviere coevolution-toolkit Repository
4. Erstelle Release auf GitHub
5. Zenodo generiert automatisch DOI
6. Aktualisiere Badges in README

---

## ✅ POST-DEPLOYMENT CHECKLIST

Nach erfolgreichem Deployment:

- [ ] CI/CD läuft erfolgreich
- [ ] Issues Templates funktionieren
- [ ] PR Template funktioniert
- [ ] README wird korrekt angezeigt
- [ ] Tutorial.ipynb ist sichtbar
- [ ] Badges sind aktualisiert
- [ ] LICENSE ist korrekt
- [ ] CONTRIBUTING.md ist lesbar
- [ ] setup.py funktioniert (pip install)
- [ ] PyPI Release (optional)
- [ ] Zenodo DOI (optional)
- [ ] Social Media Ankündigung

---

## 📣 ANKÜNDIGUNG

Nach Deployment, teilen Sie:

### Twitter/X
```
🚀 Introducing CoEvolution Toolkit v1.0.0!

A Python package for analyzing VM-DM coevolution in galaxies 🌌

✨ Features:
- Coupled evolution solver
- Feedback mechanisms
- Observable predictions
- Interactive tutorials

📦 pip install coevolution-toolkit

🔗 github.com/YOURUSERNAME/coevolution-toolkit

#astronomy #cosmology #python
```

### Reddit (r/cosmology, r/Python)
```
[Project] CoEvolution Toolkit - Python package for galaxy formation

I've developed a toolkit for analyzing the coevolution of visible and 
dark matter in galaxies. It implements feedback mechanisms, computes 
observables like rotation curves and SHMR, and includes interactive tutorials.

Key features:
- Coupled VM-DM evolution equations
- SNe and AGN feedback
- Publication-quality visualizations
- Full documentation and tests

MIT licensed and ready for research use!

GitHub: [link]
```

---

## 🐛 TROUBLESHOOTING

### Problem: CI fails on import

**Lösung**: Stelle sicher `__init__.py` hat relative imports:
```python
from .core import CosmologicalBackground
# nicht: from coevolution_toolkit.core import ...
```

### Problem: pip install schlägt fehl

**Lösung**: Prüfe `setup.py` Dependencies:
```bash
python setup.py check
python -m build  # Test build
```

### Problem: Tests finden Module nicht

**Lösung**: Installiere in editable mode:
```bash
pip install -e .
pytest
```

---

## 📞 SUPPORT

Bei Fragen:
1. Prüfe [CONTRIBUTING.md](CONTRIBUTING.md)
2. Öffne ein Issue
3. Kontaktiere Maintainer

---

## 🎉 FERTIG!

**Ihr Repository ist jetzt:**
✅ Auf GitHub  
✅ Mit CI/CD  
✅ pip-installierbar  
✅ Gut dokumentiert  
✅ Bereit für Contributors  
✅ Publikationsreif  

**Viel Erfolg mit Ihrem Open-Source-Projekt!** 🌌🚀
