from dataclasses import dataclass
from typing import Dict


@dataclass
class AtlasWeights:
    trust: float = 0.30
    latency: float = 0.20
    accuracy: float = 0.30
    stability: float = 0.20

    def validate(self) -> None:
        total = self.trust + self.latency + self.accuracy + self.stability
        if round(total, 2) != 1.00:
            raise ValueError("ATLAS weights must add up to 1.0")


@dataclass
class AtlasScores:
    trust: float
    latency: float
    accuracy: float
    stability: float

    def validate(self) -> None:
        for name, value in self.__dict__.items():
            if value < 0 or value > 100:
                raise ValueError(f"{name} score must be between 0 and 100")


class AtlasScoringEngine:
    def __init__(self, weights: AtlasWeights = AtlasWeights()):
        self.weights = weights
        self.weights.validate()

    def calculate_score(self, scores: AtlasScores) -> float:
        scores.validate()

        final_score = (
            scores.trust * self.weights.trust
            + scores.latency * self.weights.latency
            + scores.accuracy * self.weights.accuracy
            + scores.stability * self.weights.stability
        )

        return round(final_score, 2)

    def assign_tier(self, score: float) -> str:
        if score >= 95:
            return "Platinum"
        elif score >= 85:
            return "Gold"
        elif score >= 70:
            return "Silver"
        elif score >= 50:
            return "Bronze"
        return "Critical Risk"

    def generate_report(self, scores: AtlasScores) -> Dict[str, object]:
        final_score = self.calculate_score(scores)

        return {
            "atlas_score": final_score,
            "tier": self.assign_tier(final_score),
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
        elif score >= 85:
            return "AI system is enterprise ready with minor monitoring improvements."
        elif score >= 70:
            return "AI system requires reliability improvements before high-risk deployment."
        elif score >= 50:
            return "AI system should be restricted to controlled environments."
        return "AI system should not be deployed until major issues are resolved."
