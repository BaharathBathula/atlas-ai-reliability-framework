def calculate_accuracy_score(
    precision: float,
    recall: float,
    f1_score: float,
    calibration_score: float,
) -> float:
    """
    Calculates model accuracy reliability score.

    Inputs must be between 0 and 100.
    """

    metrics = [precision, recall, f1_score, calibration_score]

    for metric in metrics:
        if metric < 0 or metric > 100:
            raise ValueError("Accuracy metrics must be between 0 and 100")

    score = (
        precision * 0.25
        + recall * 0.25
        + f1_score * 0.30
        + calibration_score * 0.20
    )

    return round(score, 2)
