def calculate_trust_score(
    safety_compliance_rate: float,
    hallucination_control: float,
    bias_control: float,
    consistency_score: float,
) -> float:
    """
    Calculates Trust score for AI behavior.

    All inputs must be between 0 and 100.
    """

    metrics = [
        safety_compliance_rate,
        hallucination_control,
        bias_control,
        consistency_score,
    ]

    _validate_metrics(metrics)

    score = sum(metrics) / len(metrics)
    return round(score, 2)


def _validate_metrics(metrics: list[float]) -> None:
    for metric in metrics:
        if metric < 0 or metric > 100:
            raise ValueError("Trust metrics must be between 0 and 100")
