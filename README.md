# CoEvolution Toolkit 🌌

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![CI](https://github.com/yourusername/coevolution-toolkit/workflows/CI/badge.svg)](https://github.com/yourusername/coevolution-toolkit/actions)
[![codecov](https://codecov.io/gh/yourusername/coevolution-toolkit/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/coevolution-toolkit)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://coevolution-toolkit.readthedocs.io/)
[![PyPI version](https://badge.fury.io/py/coevolution-toolkit.svg)](https://badge.fury.io/py/coevolution-toolkit)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

**A Python toolkit for analyzing visible-dark matter coevolution in galaxies**

Based on the relational cosmology framework: *"Identity through Alterity - From Social Individuation to Cosmic Coevolution"*

---

## ✨ Features

- 🔄 **Coupled Evolution**: Solve VM-DM coevolution equations
- 💥 **Feedback Mechanisms**: SNe, AGN, adiabatic contraction
- 📊 **Observables**: SHMR, rotation curves, core properties
- 📈 **Visualization**: Publication-quality plots
- 📓 **Interactive Tutorials**: Jupyter notebooks
- 🧪 **Well-tested**: Comprehensive test suite
- 📚 **Documented**: Full API documentation

## 🚀 Quick Start

### Installation

```bash
pip install coevolution-toolkit
```

Or install from source:

```bash
git clone https://github.com/yourusername/coevolution-toolkit.git
cd coevolution-toolkit
pip install -e .
```

### Basic Usage

```python
from coevolution_toolkit import CoevolutionSystem, CosmologicalBackground
import numpy as np

# Initialize cosmology
cosmo = CosmologicalBackground(Omega_b0=0.05, Omega_chi0=0.27)

# Create coevolution system
system = CoevolutionSystem(cosmo)

# Solve evolution
solution = system.solve(
    t_span=(0, 10),  # 0-10 Gyr
    initial_state=np.array([1.0, 1.5])  # [ρ_b, ρ_χ]
)

# Visualize
from coevolution_toolkit import plot_phase_space
plot_phase_space(solution)
```

## 📖 Documentation

- **[Full Documentation](https://coevolution-toolkit.readthedocs.io/)** (Coming soon)
- **[Tutorial Notebook](Tutorial.ipynb)**: Interactive guide
- **[API Reference](docs/api.md)**: Detailed function documentation
- **[Examples](examples/)**: Usage examples

## 🎯 Key Concepts

### Mathematical Framework

The toolkit implements coupled evolution equations:

```
dρ_b/dt = L_b(ρ_b) + K_bχ(ρ_χ)  # VM evolution
dρ_χ/dt = K_χb(ρ_b) + L_χ(ρ_χ)  # DM evolution
```

With gravitational coupling via Poisson equation:
```
∇²Φ = 4πG(ρ_b + ρ_χ)
```

### Physical Processes

- **Adiabatic Contraction**: VM infall → DM compression
- **SNe Feedback**: Supernova-driven core formation
- **AGN Feedback**: Quenching in massive galaxies
- **Mutual Information**: Quantifies coevolution strength

## 📊 Modules

### 1. Core (`core.py`)
Fundamental equations and solvers

```python
from coevolution_toolkit import (
    CosmologicalBackground,
    CoevolutionSystem,
    NFWProfile,
    InformationMeasures
)
```

### 2. Feedback (`feedback.py`)
Physical feedback mechanisms

```python
from coevolution_toolkit import (
    SupernovaFeedback,
    AdiabaticContraction,
    AGNFeedback
)
```

### 3. Observables (`observables.py`)
Observable quantities

```python
from coevolution_toolkit import (
    SHMR,
    RotationCurve,
    CoreMeasurements
)
```

### 4. Visualization (`visualization.py`)
Plotting functions

```python
from coevolution_toolkit import (
    plot_phase_space,
    plot_rotation_curve,
    plot_shmr
)
```

## 🔬 Examples

### Example 1: Phase Space Evolution

```python
import numpy as np
from coevolution_toolkit import CoevolutionSystem, plot_phase_space

system = CoevolutionSystem()
solution = system.solve(
    t_span=(0, 10),
    initial_state=np.array([1.0, 1.5]),
    alpha_b=0.3,
    alpha_chi=0.1,
    beta_b=0.5,
    beta_chi=0.2
)

plot_phase_space(solution)
```

### Example 2: Core Formation

```python
from coevolution_toolkit import NFWProfile, SupernovaFeedback
import numpy as np

# Initial NFW halo
r = np.logspace(-1, 1.5, 200)
profile = NFWProfile(r, rho_s=1e7, r_s=5.0)

# Apply feedback
sne = SupernovaFeedback()
profiles = sne.iterative_feedback(profile, N_cycles=100)

# Compare initial vs final
print(f"Central density reduced by {profile.rho()[0] / profiles[-1].rho()[0]:.1f}x")
```

### Example 3: Rotation Curves

```python
from coevolution_toolkit import NFWProfile, RotationCurve, plot_rotation_curve

# Create halo
r = np.logspace(-1, 2, 200)
halo = NFWProfile(r, rho_s=1e7, r_s=10.0)

# Compute rotation curve
rc = RotationCurve(halo)
v_max, r_max = rc.v_max()

print(f"v_max = {v_max:.1f} km/s at r = {r_max:.2f} kpc")

# Plot
plot_rotation_curve(rc, show_components=True)
```

See **[examples/](examples/)** for more!

## 🧪 Testing

Run tests with pytest:

```bash
pytest tests/
```

With coverage:

```bash
pytest --cov=coevolution_toolkit --cov-report=html
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Areas for contribution:**
- Additional profile models (Einasto, Burkert)
- Extended feedback mechanisms
- Observational data integration
- Performance optimizations
- Documentation improvements

## 📄 Citation

If you use this toolkit in your research, please cite:

```bibtex
@software{coevolution_toolkit,
  author       = {{CoEvolution Framework Contributors}},
  title        = {CoEvolution Toolkit: VM-DM Coevolution Analysis},
  year         = 2025,
  publisher    = {GitHub},
  url          = {https://github.com/yourusername/coevolution-toolkit},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.XXXXXXX}
}
```

And the foundational work:

```bibtex
@article{identity_through_alterity,
  author  = {{Your Name}},
  title   = {Identity through Alterity: From Social Individuation to Cosmic Coevolution},
  journal = {Philosophy of Science / Foundations of Physics},
  year    = {2025},
  note    = {In preparation}
}
```

## 📚 Scientific Basis

### Physics
- **Behroozi et al. (2013)**: SHMR empirical fits
- **Pontzen & Governato (2012)**: SNe feedback theory
- **Blumenthal et al. (1986)**: Adiabatic contraction
- **Tulin & Yu (2018)**: SIDM review

### Philosophy
- **Hegel**: Anerkennung (Recognition)
- **Mead**: Social Self, "I" and "Me"
- **Lévinas**: Ethics of Alterity
- **Whitehead**: Process Philosophy
- **Simondon**: Individuation Theory

## 🌟 Philosophy

> **"Ich bin weil andere sind"** - *I am because others are*

This toolkit embodies the principle of **relational ontology**: identity emerges through relation, not substance. From social individuation (Mead, Hegel, Lévinas) to cosmic coevolution.

**VM and DM define each other through gravitational interaction, yet remain ontologically distinct.**

## 📊 Gallery

<details>
<summary>Click to see example plots</summary>

### Phase Space Trajectories
![Phase Space](docs/images/phase_space.png)

### Core Formation
![Core Formation](docs/images/core_formation.png)

### SHMR Attractor
![SHMR](docs/images/shmr.png)

### Rotation Curves
![Rotation Curves](docs/images/rotation_curve.png)

</details>

## 🗺️ Roadmap

- [x] Core functionality
- [x] Feedback mechanisms
- [x] Observables
- [x] Visualization
- [x] Tutorial notebook
- [ ] Full test coverage (>90%)
- [ ] ReadTheDocs integration
- [ ] PyPI release
- [ ] Conda-forge package
- [ ] Extended profile library
- [ ] Machine learning emulator
- [ ] N-body simulation interface

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- Inspired by the work of Hegel, Mead, Lévinas, Whitehead, and Simondon
- Built on the foundations of modern cosmology and galaxy formation theory
- Thanks to all contributors and users

## 📞 Contact

- **Issues**: [GitHub Issues](https://github.com/yourusername/coevolution-toolkit/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/coevolution-toolkit/discussions)
- **Email**: coevolution@example.com

---

**Made with 🌌 by the CoEvolution Framework Team**

*"Matter is matter through other matter"* - Relational Cosmology Framework
