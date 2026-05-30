# Unified Information Dynamics of High‑Temperature Superconductivity

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20140312.svg)](https://doi.org/10.5281/zenodo.20140312)

This repository contains the code, data, and LaTeX source for our paper:

**"Unified Information Dynamics Description of Strongly Coupled Gapless States, d-wave Pairing, and the Superconducting Dome"**

> We introduce a single parameter – the *information purity* `p` – that unifies three long‑standing puzzles of high‑temperature cuprate superconductors:
> - dome‑shaped `T_c`,
> - `d_{x^2-y^2}` pairing symmetry,
> - strange metal Planckian dissipation.

## 🔬 Scientific breakthrough – what this work achieves

### 🧠 Microscopic insight: strongly coupled gapless states explained
The strange metal and pseudogap – known as *strongly coupled gapless states* – are not separate anomalies. They are the macroscopic manifestation of a **critical coherent state** where the information purity `p` is slightly below its maximum (`0.97`). This reveals the hidden order behind their seemingly exotic behaviour.

### 📊 Three macroscopic unifying results
1. **One parameter for the dome** – `T_c = s * p/(1-p)` fits LSCO and YBCO with `R² > 0.95` using only three material parameters.
2. **Planckian dissipation from geometry** – The linear‑in‑`T` resistivity coefficient `α = C(1-p)` with `C ≈ 31` derived purely from the Dirac‑cone geometry of the `d`-wave nodes (no free parameters).
3. **Bridge to automatic control** – The theory is faithfully embedded into control theory: dome ↔ passivity, `d`-wave ↔ symmetry‑dominated mode, dissipation ↔ reachable set. This opens the door to engineering‑guided superconductor design.

## 📁 Repository contents

| File / Folder | Description |
|---------------|-------------|
| `fit_cuprate_dome.py` | Least‑squares fit of `T_c(x) = s * p/(1-p)` to LSCO and YBCO data – produces Table 1 and dome plot. |
| `dome_validation.py` | Standard Ginzburg‑Landau simulation: shows that setting `ε(x) ∝ T_c(x)` reproduces the dome perfectly (Figure 2). |
| `inversion_coupling_matrix.py` | Inverts the coupling matrix strength `δK(x)` from superfluid density data using linear response (Figure 4). |

## 🚀 Getting started

### Requirements
- Python 3.7+
- NumPy, SciPy, Matplotlib

Install dependencies:
```bash
pip install numpy scipy matplotlib
```

### Run the dome fit
```bash
python fit_cuprate_dome.py
```
This outputs the fit parameters (same as Table 1) and saves `dome_fit.pdf`.

### Run the validation simulation
```bash
python dome_validation.py
```
Generates `dome_validation.png` – shows perfect overlap between the GL simulation and the dome curve.

### Run the coupling matrix inversion (synthetic data)
```bash
python inversion_coupling_matrix.py
```
Generates `inversion_coupling_matrix.png` – demonstrates recovery of `δK(x)` peak at the quantum critical point `x ≈ 0.19`.

## 📖 How to use this code
- **Reproduce our results:** Run the three scripts above; they require no additional input.
- **Adapt to your own data:** Modify `fit_cuprate_dome.py` to load your own `T_c(x)` points. The same fitting model can be applied to other cuprate families or nickelates.

## 📝 Citation
If you use this code or the framework in your research, please cite our paper:

> K. Huang, H. Liu, Z. Huang, *Unified Information Dynamics Description of Strongly Coupled Gapless States, d-wave Pairing, and the Superconducting Dome*, Zenodo (2026). DOI: [10.5281/zenodo.20139964](https://doi.org/10.5281/zenodo.20139964)

BibTeX entry:
```bibtex
@misc{Huang2026InfoDynamics,
  author       = {Kai Huang and Hongkui Liu and Ziwei Huang},
  title        = {Unified Information Dynamics Description of Strongly Coupled Gapless States, d-wave Pairing, and the Superconducting Dome},
  year         = {2026},
  doi          = {10.5281/zenodo.20139964},
  url          = {https://github.com/hkaiopen/InformationDynamics_Cuprates}
}
```

**Questions?** Open an issue or contact the authors.
