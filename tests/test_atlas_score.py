from src.atlas_score import AtlasScoringEngine, AtlasScores


def test_score_calculation():
    engine = AtlasScoringEngine()

    scores = AtlasScores(
        trust=90,
        latency=80,
        accuracy=95,
        stability=85
    )

    result = engine.calculate_score(scores)

    assert result == 88.5


def test_tier_assignment():
    engine = AtlasScoringEngine()

    assert engine.assign_tier(96) == "Platinum"
    assert engine.assign_tier(89) == "Gold"
    assert engine.assign_tier(75) == "Silver"
    assert engine.assign_tier(55) == "Bronze"
    assert engine.assign_tier(30) == "Critical Risk"
