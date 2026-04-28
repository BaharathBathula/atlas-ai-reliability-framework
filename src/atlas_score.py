from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class AtlasWeights:
    trust: float = 0.30
    latency: float = 0.20
    accuracy: float = 0.30
    stability: float = 0.20

    def validate(self) -> None:
        total = self.trust + self.latency + self.accuracy + self.stability
        if round(total, 4) != 1.0:
            raise ValueError("ATLAS weights must add up to 1.0")


@dataclass
class AtlasScores:
    trust: float
    latency: float
    accuracy: float
    stability: float

    def validate(self) -> None:
        for metric_name, metric_value in self.__dict__.items():
            if not isinstance(metric_value, (int, float)):
                raise TypeError(f"{metric_name} must be numeric")

            if metric_value < 0 or metric_value > 100:
                raise ValueError(f"{metric_name} score must be between 0 and 100")


class AtlasScoringEngine:
    def __init__(self, weights: AtlasWeights | None = None):
        self.weights = weights or AtlasWeights()
        self.weights.validate()

    def calculate_score(self, scores: AtlasScores) -> float:
        scores.validate()

        atlas_score = (
            scores.trust * self.weights.trust
            + scores.latency * self.weights.latency
            + scores.accuracy * self.weights.accuracy
            + scores.stability * self.weights.stability
        )

        return round(atlas_score, 2)

    def assign_tier(self, score: float) -> str:
        if score >= 95:
            return "Platinum"
        if score >= 85:
            return "Gold"
        if score >= 70:
            return "Silver"
        if score >= 50:
            return "Bronze"
        return "Critical Risk"

    def generate_report(self, scores: AtlasScores) -> Dict[str, Any]:
        final_score = self.calculate_score(scores)
        tier = self.assign_tier(final_score)

        return {
            "atlas_score": final_score,
            "tier": tier,
            "dimensions": {
                "trust": scores.trust,
                "latency": scores.latency,
                "accuracy": scores.accuracy,
                "stability": scores.stability,
            },
            "recommendation": self._recommendation(final_score),
        }

    def _recommendation(self, score: float) -> str:
        if score >= 95:
            return "AI system is production-critical ready."
        if score >= 85:
            return "AI system is enterprise ready with minor monitoring improvements."
        if score >= 70:
            return "AI system requires reliability improvements before high-risk deployment."
        if score >= 50:
            return "AI system should be restricted to controlled environments."
        return "AI system should not be deployed until major reliability issues are resolved."
