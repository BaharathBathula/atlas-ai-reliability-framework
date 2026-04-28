import pytest

from src.atlas_score import AtlasScoringEngine, AtlasScores, AtlasWeights
from src.trust import calculate_trust_score
from src.latency import calculate_latency_score
from src.accuracy import calculate_accuracy_score
from src.stability import calculate_stability_score


def test_score_calculation():
    engine = AtlasScoringEngine()

    scores = AtlasScores(
        trust=90,
        latency=80,
        accuracy=95,
        stability=85,
    )

    assert engine.calculate_score(scores) == 88.5


def test_tier_assignment():
    engine = AtlasScoringEngine()

    assert engine.assign_tier(96) == "Platinum"
    assert engine.assign_tier(89) == "Gold"
    assert engine.assign_tier(75) == "Silver"
    assert engine.assign_tier(55) == "Bronze"
    assert engine.assign_tier(30) == "Critical Risk"


def test_invalid_score_range():
    engine = AtlasScoringEngine()

    with pytest.raises(ValueError):
        engine.calculate_score(
            AtlasScores(
                trust=101,
                latency=80,
                accuracy=90,
                stability=85,
            )
        )


def test_invalid_weights():
    with pytest.raises(ValueError):
        AtlasScoringEngine(
            AtlasWeights(
                trust=0.5,
                latency=0.5,
                accuracy=0.5,
                stability=0.5,
            )
        )


def test_trust_score():
    assert calculate_trust_score(90, 80, 85, 95) == 87.5


def test_latency_score():
    score = calculate_latency_score(
        p95_latency_ms=250,
        p99_latency_ms=500,
        target_p95_ms=300,
        target_p99_ms=600,
        throughput_retention_rate=90,
    )

    assert score == 100.0


def test_accuracy_score():
    assert calculate_accuracy_score(90, 85, 88, 92) == 88.5


def test_stability_score():
    assert calculate_stability_score(80, 85, 75, 90) == 82.5
