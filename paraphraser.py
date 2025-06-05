from transformers import pipeline

paraphraser = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")

def paraphrase_problem(problem_text):
    prompt = f"paraphrase: {problem_text} </s>"
    output = paraphraser(prompt, max_length=256, do_sample=True, top_k=120, num_return_sequences=1)
    return output[0]['generated_text']
