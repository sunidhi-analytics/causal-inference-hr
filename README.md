# Causal Inference for HR Interventions

**Estimating the true impact of a manager training program on team attrition using quasi-experimental methods.**

HR invested in a leadership development program. Managers who attended now show lower team attrition. But did the training cause that improvement, or were better managers simply more likely to be selected? This project applies propensity score matching and difference-in-differences to isolate the genuine causal effect from selection bias, revealing that naive before/after comparisons overstate the impact by approximately 2x. The analysis then identifies which departments benefit most and translates causal estimates into dollar-valued ROI recommendations for HR leadership.

---

## Business Impact

| Finding | Evidence | Action Enabled |
|---|---|---|
| **Naive comparisons overstate impact by ~2x** | Naive: ~8pp vs Causal: ~4pp reduction | Every program evaluation should use causal methods, not simple before/after |
| **~4pp causal reduction in team attrition** | Confirmed by both PSM and DiD (converging estimates) | Continue and expand the training program with confidence |
| **$57,600 savings per manager trained** | 12 employees x 0.04 x $120K replacement cost | Clear ROI case for budget allocation |
| **Support and Sales benefit 1.2 to 1.5x more** | Heterogeneous treatment effect analysis by department | Prioritize these departments for the next training cohort |
| **Result is robust to moderate unmeasured confounding** | Rosenbaum sensitivity analysis (critical gamma reported) | Stakeholders can assess plausibility of alternative explanations |

---

## What This Project Demonstrates

- **Propensity Score Matching (PSM):** Constructing a valid counterfactual by matching treated and control managers on observable characteristics, with caliper enforcement, covariate balance diagnostics, and bootstrapped confidence intervals
- **Difference-in-Differences (DiD):** Estimating causal effects using pre/post and treatment/control variation with clustered standard errors
- **Sensitivity Analysis:** Rosenbaum bounds quantifying how strong an unmeasured confounder would need to be to invalidate the result
- **Heterogeneous Treatment Effects:** Identifying which departments benefit most from the intervention to inform targeting
- **ROI Translation:** Converting causal estimates into dollar-valued business cases for HR leadership and CFO-level communication

---

## Project Structure

```
├── notebooks/
│   └── causal_inference_hr.ipynb   # Complete analysis (single end-to-end notebook)
├── src/
│   └── simulation.py               # Data generation function (importable)
├── data/
│   └── README.md                    # Data documentation
├── outputs/
│   └── figures/                     # Generated visualizations
├── requirements.txt
├── .gitignore
└── README.md
```

## Key Results

| Method | Estimated Effect | 95% CI | Bias vs True Effect |
|---|---|---|---|
| Naive Comparison | ~8 pp | n/a | ~4 pp (overstated) |
| Propensity Score Matching | ~4 pp | reported in notebook | minimal |
| Difference-in-Differences | ~4 pp | reported in notebook | minimal |
| True Effect (ground truth) | 4.0 pp | n/a | 0 |

Note: Exact values depend on simulation seed. Run the notebook to reproduce.

## How to Run

```bash
git clone https://github.com/sunidhi-analytics/causal-inference-hr.git
cd causal-inference-hr
pip install -r requirements.txt
jupyter notebook notebooks/causal_inference_hr.ipynb
```

## Tech Stack

Python, pandas, scikit-learn (LogisticRegression, NearestNeighbors), statsmodels (OLS with clustered SE), scipy (bootstrap, Rosenbaum bounds), matplotlib, seaborn

## Why Simulated Data?

Real organizational HR data is proprietary. This project uses a carefully designed simulation that encodes realistic selection bias (better managers are more likely to be trained), confounding (department, experience, and ratings affect both treatment assignment and outcomes), and heterogeneous treatment effects (Support and Sales benefit more). The known ground truth (4pp true effect) lets us validate that our methods actually work, something impossible with real observational data.

The same methods demonstrated here can be applied directly to real HRIS data from Workday, SAP SuccessFactors, or any similar system.

## About

Built by [Sunidhi Sharma](https://www.linkedin.com/in/sunidhisharma28/) | Senior Data Scientist specializing in People Analytics, Causal Inference, and Responsible AI in HR. 5+ years across Publicis Sapient, Korn Ferry, Infosys, and TCS.

[Portfolio](https://sunidhi-analytics.github.io/Portfolio-Sunidhi/) · [LinkedIn](https://www.linkedin.com/in/sunidhisharma28/) · [GitHub](https://github.com/sunidhi-analytics)
