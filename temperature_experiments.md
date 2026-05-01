# Temperature Experiments

## Goal

We used the parameter experiment to test how generation temperature affects cybersecurity answer quality. The baseline used `temperature = 0`, and the finalists were tested again at:

- `temperature = 0.5`
- `temperature = 1.0`

Evaluator settings stayed fixed for all evaluations. Only the tested model generation temperature changed.

## Finalist models tested

| Model | Size category | Type |
|---|---|---|
| Qwen2.5-3B-Instruct | ≤7B | General-purpose instruct |
| Phi-3.5-mini-instruct | ≤7B | General-purpose instruct |
| Qwen2.5-Coder-7B-Instruct | 7B–13B | Code-focused instruct |
| Mistral-Nemo-Instruct-2407 | 7B–13B | General-purpose instruct |

## Score summary

| Model | Temp | Overall | Trap Avg | Hallucination | Practical | Code Review |
|---|---|---|---|---|---|---|
| Qwen2.5-3B-Instruct | 0 | 3.99 | 4.22 | 3.5 | 3.83 | 4.8 |
| Qwen2.5-3B-Instruct | 0.5 | 3.94 | 4.56 | 4.25 | 3.71 | 4.8 |
| Qwen2.5-3B-Instruct | 1.0 | 4.07 | 3.67 | 2.0 | 4.19 | 5.0 |
| Phi-3.5-mini-instruct | 0 | 4.01 | 4.22 | 3.25 | 3.79 | 5.0 |
| Phi-3.5-mini-instruct | 0.5 | 4.05 | 4.22 | 3.25 | 3.92 | 5.0 |
| Phi-3.5-mini-instruct | 1.0 | 3.96 | 4.0 | 3.0 | 4.0 | 4.8 |
| Qwen2.5-Coder-7B-Instruct | 0 | 4.08 | 3.67 | 2.0 | 4.54 | 5.0 |
| Qwen2.5-Coder-7B-Instruct | 0.5 | 3.96 | 4.0 | 3.0 | 4.0 | 4.8 |
| Qwen2.5-Coder-7B-Instruct | 1.0 | 4.19 | 4.11 | 3.0 | 4.5 | 5.0 |
| Mistral-Nemo-Instruct-2407 | 0 | 4.36 | 3.78 | 2.25 | 4.71 | 5.0 |
| Mistral-Nemo-Instruct-2407 | 0.5 | 4.32 | 3.56 | 1.75 | 4.62 | 5.0 |
| Mistral-Nemo-Instruct-2407 | 1.0 | 4.23 | 3.33 | 1.25 | 4.5 | 5.0 |

## Main observations

### Qwen2.5-3B-Instruct

Qwen2.5-3B was relatively strong at all temperatures. At `temperature = 0.5`, hallucination-trap performance improved compared with baseline, but practical command quality slightly decreased. At `temperature = 1.0`, the overall score increased, but hallucination resistance dropped. Higher temperature produced more variable results.

### Phi-3.5-mini-instruct

Phi-3.5-mini was the most stable small model. `temperature = 0.5` slightly improved the overall score and practical score. `temperature = 1.0` reduced the overall score and slightly weakened trap performance. For this model, moderate temperature was acceptable, but high temperature was not clearly beneficial.

### Qwen2.5-Coder-7B-Instruct

Qwen2.5-Coder was strong on code-review and practical tasks across temperatures. The evaluator gave its highest score at `temperature = 1.0`, but this should be interpreted carefully because high-temperature outputs can become more verbose and may score well while still needing manual verification. For professional cybersecurity use, its code and command answers should still be checked.

### Mistral-Nemo-Instruct-2407

Mistral-Nemo had the best baseline result at `temperature = 0`. Its score decreased at `temperature = 0.5` and decreased further at `temperature = 1.0`. The hallucination-trap score also declined as temperature increased. This was the clearest case where higher temperature reduced reliability.

## Conclusion

The safest setting for cybersecurity evaluation was `temperature = 0`. It gave the most reproducible outputs and avoided unnecessary randomness. `temperature = 0.5` sometimes improved detail or trap behavior, but the effect was not consistent. `temperature = 1.0` increased variability and, for some models, reduced hallucination resistance.

For professional cybersecurity work, lower temperature is preferred. Higher temperatures may be useful for brainstorming, but they are less suitable for tasks where factual accuracy, command correctness, and hallucination resistance matter.
