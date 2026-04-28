from src.atlas_score import AtlasScoringEngine, AtlasScores


def main() -> None:
    scores = AtlasScores(
        trust=92,
        latency=88,
        accuracy=90,
        stability=84,
    )

    engine = AtlasScoringEngine()
    report = engine.generate_report(scores)

    print("===== ATLAS RELIABILITY REPORT =====")
    print(f"ATLAS Score : {report['atlas_score']}")
    print(f"Tier        : {report['tier']}")

    print("\nDimensions:")
    for dimension, value in report["dimensions"].items():
        print(f" - {dimension.title():10}: {value}")

    print("\nRecommendation:")
    print(report["recommendation"])


if __name__ == "__main__":
    main()
