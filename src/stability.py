def calculate_stability_score(
    drift_resistance: float,
    performance_resilience: float,
    adversarial_robustness: float,
    degradation_control: float,
) -> float:
    """
    Calculates stability score for long-term AI reliability.

    Inputs must be between 0 and 100.
    """

    metrics = [
        drift_resistance,
        performance_resilience,
        adversarial_robustness,
        degradation_control,
    ]

    for metric in metrics:
        if metric < 0 or metric > 100:
            raise ValueError("Stability metrics must be between 0 and 100")

    score = (
        drift_resistance * 0.30
        + performance_resilience * 0.30
        + adversarial_robustness * 0.20
        + degradation_control * 0.20
    )

    return round(score, 2)
