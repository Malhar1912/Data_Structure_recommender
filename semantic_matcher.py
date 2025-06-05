import json
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("data/problem_embeddings.json") as f:
    known_problems = json.load(f)

def find_closest_problem(user_input):
    user_vec = model.encode(user_input, convert_to_tensor=True)
    similarities = {
        name: float(util.pytorch_cos_sim(user_vec, model.encode(desc, convert_to_tensor=True))[0])
        for name, desc in known_problems.items()
    }
    best_match = max(similarities, key=similarities.get)
    return best_match, similarities[best_match]