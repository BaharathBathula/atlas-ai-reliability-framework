# ATLAS Architecture

```text
                  ┌──────────────────────┐
                  │  Production AI Model │
                  │ LLM / ML / RAG / API │
                  └──────────┬───────────┘
                             │

     ┌──────────────┬────────┼────────┬──────────────┐
     ▼              ▼        ▼        ▼

┌─────────┐   ┌─────────┐ ┌─────────┐ ┌────────────┐
│ Trust   │   │Latency  │ │Accuracy │ │ Stability │
└────┬────┘   └────┬────┘ └────┬────┘ └─────┬──────┘
     │             │           │            │

 Hallucination   P95/P99     Precision     Drift
 Bias            Throughput  Recall        Decay
 Toxicity        Queue Time  F1 Score      Robustness

                  ┌─────────────────────┐
                  │  ATLAS Score Engine │
                  └──────────┬──────────┘
                             ▼

                    Platinum / Gold / Risk
