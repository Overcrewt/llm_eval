# Screening Log

## Screening Methodology

The screening phase was used to compare candidate models and decide which models should be selected as finalists.

The screening considered:

- factual cybersecurity accuracy
- completeness of explanations
- practical command and code usability
- code review trap performance
- hallucination trap resistance
- refusal behavior
- hardware feasibility

The same general question set was used across models. The evaluation included factual questions, practical security tasks, sensitive/offensive security questions, code review traps, hallucination traps, and custom web application security questions.

Models were accepted as finalists if they performed strongly and contributed useful comparison value across model size or model type.

Models were rejected if they produced too many incorrect practical answers, failed hallucination traps, performed worse than similar models, or were not useful enough compared to stronger candidates.

---

## Model Screening Decisions

### TinyLlama-1.1B-Chat-v1.0

**Status:** Rejected  
**Size:** 1.1B  
**Type:** General chat baseline  

TinyLlama was included as a very small baseline model. It was fast and easy to run, but its technical reliability was weak.

Main observations:

- produced several incomplete answers
- made mistakes in practical command questions
- performed poorly on hallucination traps
- often sounded confident even when incorrect

**Decision:** Rejected.  
**Reason:** Useful as a baseline, but not reliable enough for professional cybersecurity work.

---

### Qwen2.5-3B-Instruct

**Status:** Finalist  
**Size:** 3B  
**Type:** General instruct  

Qwen2.5-3B-Instruct performed strongly for its size. It showed good factual accuracy and good hallucination trap performance compared to many larger models.

Main observations:

- strong small-model baseline
- good performance on factual questions
- good trap-question performance
- practical enough for limited hardware environments

**Decision:** Accepted as finalist.  
**Reason:** Strong small model with good quality-to-resource balance.

---

### Llama-3.2-3B-Instruct

**Status:** Rejected  
**Size:** 3B  
**Type:** General instruct  

Llama-3.2-3B-Instruct produced acceptable answers, but it did not outperform Qwen2.5-3B-Instruct or Phi-3.5-mini-instruct.

Main observations:

- acceptable small-model performance
- weaker than selected small finalists
- did not add enough comparative value

**Decision:** Rejected.  
**Reason:** Good enough to test, but weaker than other small finalists.

---

### Phi-3.5-mini-instruct

**Status:** Finalist  
**Size:** 3.8B  
**Type:** General instruct  

Phi-3.5-mini-instruct was one of the strongest small models. It provided a good balance between quality, speed, and hardware requirements.

Main observations:

- strong small-model performance
- good overall score
- good trap handling
- practical for local use on limited hardware

**Decision:** Accepted as finalist.  
**Reason:** Best small-model balance of performance and resource use.

---

### Phi-4-mini-instruct

**Status:** Skipped  
**Size:** 3.8B  
**Type:** General instruct  

Phi-4-mini-instruct was considered, but it failed to load correctly in the local setup during testing.

Main observations:

- model download was possible
- local loading failed
- not evaluated fully

**Decision:** Skipped.  
**Reason:** Technical loading issue prevented a reliable evaluation.

---

### Mistral-7B-Instruct-v0.3

**Status:** Strong candidate  
**Size:** 7B  
**Type:** General instruct  

Mistral-7B-Instruct-v0.3 performed well on normal questions and practical tasks. However, it was weaker than the final selected models in some trap categories.

Main observations:

- strong factual and practical answers
- good normal score
- weaker hallucination trap performance than some finalists
- useful comparison model

**Decision:** Strong candidate, not finalist.  
**Reason:** Good model, but Qwen2.5-Coder-7B and Mistral-Nemo provided stronger final comparison value.

---

### Qwen2.5-7B-Instruct

**Status:** Strong candidate  
**Size:** 7B  
**Type:** General instruct  

Qwen2.5-7B-Instruct performed well overall, but it was not selected as a finalist because Qwen2.5-Coder-7B provided stronger code/practical value.

Main observations:

- good general performance
- good trap score
- stable output quality
- less distinctive than Qwen2.5-Coder-7B

**Decision:** Strong candidate, not finalist.  
**Reason:** Good model, but the coder version was more useful for cybersecurity tasks.

---

### Qwen2.5-Coder-7B-Instruct

**Status:** Finalist  
**Size:** 7B  
**Type:** Code-focused instruct  

Qwen2.5-Coder-7B-Instruct was selected because it performed strongly on practical tasks, code-related questions, command generation, and code review traps.

Main observations:

- strong command and script quality
- good code review performance
- good practical cybersecurity usefulness
- useful comparison against cybersecurity fine-tunes

**Decision:** Accepted as finalist.  
**Reason:** Best practical/code-oriented model.

---

### WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B

**Status:** Strong candidate  
**Size:** 7B  
**Type:** Cybersecurity / coder  

WhiteRabbitNeo was included as a cybersecurity-oriented coder model. It performed well enough to be useful for comparison, but it did not clearly outperform Qwen2.5-Coder-7B.

Main observations:

- good cybersecurity relevance
- good practical answers
- did not clearly beat the base coder model
- some hallucination/trap weaknesses remained

**Decision:** Strong candidate, not finalist.  
**Reason:** Useful cybersecurity comparison model, but not the strongest final choice.

---

### Lily-Cybersecurity-7B-v0.2

**Status:** Rejected  
**Size:** 7B  
**Type:** Cybersecurity fine-tune  

Lily-Cybersecurity was included to test whether cybersecurity fine-tuning improves performance. It answered many cybersecurity questions, but its trap performance and overall reliability were weaker than stronger general-purpose and coder models.

Main observations:

- cybersecurity-focused model
- acceptable normal answers
- weaker hallucination trap performance
- did not outperform stronger general-purpose models

**Decision:** Rejected.  
**Reason:** Cybersecurity label did not translate into better overall performance.

---

### SenecaLLM Qwen2.5-7B CyberSecurity

**Status:** Strong candidate  
**Size:** 7B  
**Type:** Cybersecurity fine-tune  

SenecaLLM performed better than some cybersecurity-focused alternatives and was useful for comparison. However, it was not selected as a finalist because other models had stronger overall or practical performance.

Main observations:

- good cybersecurity-focused comparison model
- acceptable normal and trap performance
- did not clearly outperform Qwen2.5-Coder or Mistral-Nemo

**Decision:** Strong candidate, not finalist.  
**Reason:** Useful for analysis, but not the best model in its category.

---

### Gemma-2-9B-it

**Status:** Rejected  
**Size:** 9B  
**Type:** General instruct  

Gemma-2-9B-it performed acceptably, but it did not provide enough advantage over smaller or stronger models.

Main observations:

- reasonable general performance
- good trap average
- not the strongest practical model
- less useful than Mistral-Nemo or Qwen2.5-Coder

**Decision:** Rejected.  
**Reason:** Good but not competitive enough for finalist selection.

---

### Mistral-Nemo-Instruct-2407

**Status:** Finalist  
**Size:** 12B  
**Type:** General instruct  

Mistral-Nemo was the best overall model in the baseline evaluation. It scored highest overall and performed well across factual, practical, and custom cybersecurity questions.

Main observations:

- best overall score
- strong normal-answer performance
- good practical usefulness
- higher hardware cost than smaller models

**Decision:** Accepted as finalist.  
**Reason:** Best overall model in the evaluation.

---

## Screening Conclusion

The screening showed that cybersecurity-specific fine-tuning did not automatically produce the best model.

The strongest models were general-purpose or coder models:

- Mistral-Nemo-Instruct-2407
- Qwen2.5-Coder-7B-Instruct
- Phi-3.5-mini-instruct
- Qwen2.5-3B-Instruct

The most important screening finding was that model branding is not enough. A model with "cybersecurity" in the name can still hallucinate, miss deeper vulnerabilities, or produce weaker practical output than a strong general-purpose or coder model.