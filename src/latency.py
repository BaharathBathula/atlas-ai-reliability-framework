def calculate_latency_score(
    p95_latency_ms: float,
    p99_latency_ms: float,
    target_p95_ms: float,
    target_p99_ms: float,
    throughput_retention_rate: float,
) -> float:
    """
    Calculates latency score based on tail latency and throughput retention.
    """

    if target_p95_ms <= 0 or target_p99_ms <= 0:
        raise ValueError("Latency targets must be greater than 0")

    if throughput_retention_rate < 0 or throughput_retention_rate > 100:
        raise ValueError("Throughput retention rate must be between 0 and 100")

    p95_score = min(target_p95_ms / p95_latency_ms, 1.0) * 100
    p99_score = min(target_p99_ms / p99_latency_ms, 1.0) * 100

    final_score = (p95_score * 0.35) + (p99_score * 0.35) + (throughput_retention_rate * 0.30)
    return round(final_score, 2)
