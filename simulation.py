"""
Data simulation for the Causal Inference HR project.

Generates a manager-level dataset with realistic selection bias,
confounding, and heterogeneous treatment effects for evaluating
quasi-experimental causal inference methods.
"""

import numpy as np
import pandas as pd


def simulate_manager_training_data(n=500, true_ate=-0.04, seed=42):
    """
    Simulate manager-level data with a training intervention.

    Key design: treatment assignment is NOT random. Better managers
    (higher ratings, more experience) are more likely to be selected,
    creating the selection bias that makes causal inference necessary.

    Parameters
    ----------
    n : int
        Number of managers to simulate.
    true_ate : float
        True average treatment effect on attrition rate (negative = reduction).
    seed : int
        Random seed for reproducibility.

    Returns
    -------
    df : pd.DataFrame
        Manager-level dataset with pre/post attrition and treatment assignment.
    true_ate : float
        The true ATE used in simulation (for validation).
    """
    np.random.seed(seed)

    # Manager characteristics (confounders)
    manager_experience = np.random.gamma(shape=5, scale=2, size=n)
    team_size = np.random.poisson(lam=12, size=n).clip(3, 40)
    department = np.random.choice(
        ['Engineering', 'Sales', 'Operations', 'Support'],
        size=n, p=[0.3, 0.25, 0.25, 0.2]
    )
    manager_rating = np.random.normal(3.5, 0.7, size=n).clip(1, 5)

    # Department-level attrition baselines
    dept_baseline = {
        'Engineering': 0.12, 'Sales': 0.18,
        'Operations': 0.10, 'Support': 0.22
    }
    base_attrition = np.array([dept_baseline[d] for d in department])

    # Pre-treatment attrition (function of confounders + noise)
    pre_attrition = (
        base_attrition
        - 0.008 * manager_experience
        - 0.015 * (manager_rating - 3.5)
        + 0.001 * team_size
        + np.random.normal(0, 0.03, size=n)
    ).clip(0.02, 0.40)

    # Treatment assignment: biased toward better managers
    propensity = (
        -1.0
        + 0.08 * manager_experience
        + 0.4 * manager_rating
        + 0.02 * team_size
        + np.where(department == 'Engineering', 0.3, 0)
        + np.random.normal(0, 0.5, size=n)
    )
    treatment_prob = 1 / (1 + np.exp(-propensity))
    treatment = np.random.binomial(1, treatment_prob)

    # Post-treatment attrition with heterogeneous effects
    time_trend = -0.01
    hte = np.where(
        department == 'Support', true_ate * 1.5,
        np.where(department == 'Sales', true_ate * 1.2, true_ate)
    )

    post_attrition = (
        pre_attrition + time_trend + treatment * hte
        + np.random.normal(0, 0.025, size=n)
    ).clip(0.01, 0.40)

    df = pd.DataFrame({
        'manager_id': range(1, n + 1),
        'manager_experience': manager_experience.round(1),
        'team_size': team_size,
        'department': department,
        'manager_rating': manager_rating.round(2),
        'pre_attrition_rate': pre_attrition.round(4),
        'post_attrition_rate': post_attrition.round(4),
        'treatment': treatment,
        'treatment_prob': treatment_prob.round(4),
    })

    return df, true_ate


if __name__ == '__main__':
    df, ate = simulate_manager_training_data()
    print(f"Generated {len(df)} managers")
    print(f"Treatment rate: {df['treatment'].mean():.1%}")
    print(f"True ATE: {ate}")
    print(df.head())
