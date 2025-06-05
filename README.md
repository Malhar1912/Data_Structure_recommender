
---

# 🧠 Advanced Data Structure Recommender

**An AI-powered system to recommend optimal data structures for algorithmic problems based on semantic understanding, paraphrasing, and FSM-style reasoning.**

---

## 🚀 Overview

This project analyzes algorithmic problem statements (like those found on LeetCode) and recommends the most appropriate data structure (e.g., stack, queue, heap) using a multi-stage natural language processing pipeline.

It integrates:

* **Paraphrasing** to reframe questions
* **Linguistic analysis** for entity and structure extraction
* **Semantic similarity** matching with known problems
* **Fine-tuned intent classification** for DS recommendation
* **Explanation generation** using FSM-inspired reasoning

---

## 📁 Directory Structure

```
advanced_ds_recommender/
├── main.py                       # Entry point for testing the pipeline
├── paraphraser.py               # Uses T5 model to paraphrase input
├── nlp_pipeline.py              # spaCy-based linguistic parser
├── semantic_matcher.py          # Matches problem to known embeddings
├── intent_classifier.py         # Classifies intent using fine-tuned BERT
├── explanation_generator.py     # Generates "why this DS?" explanation
├── config/
│   └── rules_config.py          # Keyword hints for FSM-style insights
├── data/
│   └── problem_embeddings.json  # Example problem embeddings
└── models/
    └── intent_classifier/       # (Optional) Fine-tuned classifier model
```

---

## 🛠️ Features

✅ **Paraphrasing with T5**
✅ **Linguistic Analysis (NER, POS, chunks, dependencies)**
✅ **Semantic Matching with Sentence Transformers**
✅ **Intent Classification with Fine-tuned BERT**
✅ **FSM-style Explanation Generator**

---

## 🧪 Sample Use Case

```bash
python main.py
```

### Input

```
You are given a list of jobs with deadlines and profits. Schedule the jobs to maximize total profit where only one job can be done at a time.
```

### Output

```
🔁 Paraphrased: Given a list of jobs with deadlines and profits, select jobs to maximize profit under the constraint of scheduling only one at a time.

🏗️ Recommended Data Structure: HEAP  
🔍 Closest Match: priority queue scheduler (87.13% match)

📚 Explanation:
🔹 Why Heap?
Heaps implement priority queues, ideal for greedy problems and dynamically maintaining min/max.

🔸 FSM-style Insight:
FSM-style reasoning: state transitions are driven by operations implied in problem (e.g., LIFO for stack).

🧠 Contextual Clues: ['list of jobs', 'deadlines', 'profits', 'schedule', 'maximize total profit']
```

---

## 🧠 NLP Pipeline

1. **Paraphrasing**: Rewrites the problem using `T5` (Vamsi/T5\_Paraphrase\_Paws).
2. **Linguistic Analysis**: spaCy transformer model extracts syntactic and semantic info.
3. **Semantic Matching**: Compares with `problem_embeddings.json` using `Sentence-BERT`.
4. **Intent Classification**: Predicts most suitable DS with fine-tuned BERT.
5. **Explanation**: Context-aware rationale + FSM-style justification.

---

## 📦 Requirements

* Python ≥ 3.8
* Transformers (HuggingFace)
* spaCy (`en_core_web_trf`)
* Sentence Transformers
* NLTK
* PyTorch

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_trf
```

---

## 🔍 Customization

* Add more known problems to `problem_embeddings.json` to improve matching.
* Fine-tune `intent_classifier.py` on your own dataset for higher accuracy.
* Enhance explanations in `explanation_generator.py` for richer reasoning.

---

## 🧩 FSM-style Reasoning

Inspired by finite-state machines, we include cues like:

* **State transitions** implied by stack (e.g., push/pop = call/return)
* **Traversal modes** in trees, graphs
* **Priority-driven scheduling** in heaps

This layer adds interpretability to the recommendation.

---

## 📚 Example Problems (`problem_embeddings.json`)

```json
{
  "priority queue scheduler": "Design a system that always picks the highest priority task first.",
  "LRU cache": "Implement a fixed-size cache that removes the least recently used item first.",
  "autocomplete system": "Build a system that suggests completions based on typed prefixes."
}
```

---

## 📈 Future Work

* Add support for **multiple DS recommendations** with confidence scores
* Integrate **LeetCode API** to fetch real-time problems
* Add **visualization** of FSM reasoning or dependency parse trees
* Include **explanation traceability** back to sentence cues

---

## 🤝 Contributing

Feel free to fork, improve or expand this system for better problem understanding and personalized DSA tutoring tools.

---

## 📜 License

MIT License. Feel free to use, share, or adapt this for research, educational, or dev purposes.

---

## 👤 Author

**Malhar Pangarkar**
🧠 Let's make algorithmic learning intelligent and intuitive!

---
