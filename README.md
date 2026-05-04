# Information Dynamics – Cuprate Superconducting Dome Fitting

This repository contains Python scripts that quantitatively fit the superconducting dome (transition temperature \(T_c\) vs. hole doping \(x\)) of cuprate high‑temperature superconductors using the **Information Dynamics** framework.

## Key idea

In Information Dynamics, the superconducting dome is described by a single parameter – the **information purity** \(p_{\mathrm{ID}}\).  
The model assumes a parabolic doping dependence of \(p_{\mathrm{ID}}(x) = p_{\mathrm{max}} - A (x - x_{\mathrm{opt}})^2\) with \(p_{\mathrm{max}} = 0.97\) fixed from independent high‑energy experiments and strange‑metal Planckian dissipation.  
The critical temperature then scales as  

\[
T_c(x) = s \cdot \frac{p_{\mathrm{ID}}(x)}{1 - p_{\mathrm{ID}}(x)},
\]

where \(s\) is a material‑dependent scale factor (effective mass, carrier density).  

The script fits this relation to published experimental data for **LSCO** and **YBCO**, extracts the optimal doping \(x_{\mathrm{opt}}\), curvature \(A\), and scale factor \(s\), and generates the dome plot used in the accompanying paper.

## Repository contents

| File | Description |
|------|-------------|
| `fit_cuprate_dome.py` | Main script: loads data, defines model, performs least‑squares fits, prints parameters, and generates `dome_fit.pdf`. |
| `dome_fit.pdf` | Example output plot (can be regenerated). |
| `README.md` | This file. |

## Requirements

- Python 3.6+
- `numpy`, `scipy`, `matplotlib`

Install dependencies with:

```bash
pip install numpy scipy matplotlib
```

## Usage

Clone the repository and run the script:

```bash
git clone https://github.com/hkaiopen/InformationDynamics_Cuprates.git
cd InformationDynamics_Cuprates
python fit_cuprate_dome.py
```

The script will print the fitted parameters to the console and save the figure as `dome_fit.pdf`.

## Output example

```
LSCO : s = 1.30, A = 4.87, x_opt = 0.157
YBCO: s = 2.90, A = 3.97, x_opt = 0.165
```

## Citation

If you use this code or the results in your research, please cite the accompanying paper:

> K. Huang, H. Liu, Z. Huang, F. Kuang, *Information Dynamics of High‑Temperature Superconductivity: Unifying Strange Metal, d‑Wave Pairing, and the Superconducting Dome*. Preprint: [Zenodo](https://doi.org/10.5281/zenodo.xxxxxx)

## License

This project is licensed under the CC‑BY‑NC‑SA 4.0 International License.  
See the [LICENSE](LICENSE) file for details.

---

*For questions or suggestions, please open an issue or contact the corresponding author.*
```
