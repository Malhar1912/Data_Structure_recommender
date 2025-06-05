from transformers import BertTokenizer, BertForSequenceClassification
import torch

label_mapping = {0: "stack", 1: "queue", 2: "heap", 3: "hash table", 4: "graph", 5: "tree", 6: "trie"}
model = BertForSequenceClassification.from_pretrained("models/intent_classifier")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

def classify_intent(problem_text):
    inputs = tokenizer(problem_text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    logits = outputs.logits
    pred = torch.argmax(logits, dim=1).item()
    return label_mapping[pred]