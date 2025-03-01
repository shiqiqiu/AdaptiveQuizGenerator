
import spacy
import random
import pandas as pd

# Load spaCy language model
nlp = spacy.load("en_core_web_sm")

# Function to extract key concepts from text
def extract_concepts(text):
    doc = nlp(text)
    concepts = [ent.text for ent in doc.ents if ent.label_ in {"PERSON", "ORG", "GPE", "DATE", "EVENT", "NORP"}]
    nouns = [chunk.text for chunk in doc.noun_chunks]
    return set(concepts + nouns)

# Function to generate MCQs
def generate_mcqs(concepts):
    questions = []
    for concept in concepts:
        question = f"What is {concept}?"
        distractors = [f"Not {concept}", f"Something else", f"Not related to {concept}"]
        random.shuffle(distractors)
        questions.append({
            "question": question,
            "choices": [concept] + distractors,
            "answer": concept
        })
    return questions

# Sample input text
text = """
Artificial Intelligence is a field of computer science focused on building intelligent machines.
Alan Turing introduced the Turing Test in 1950 to determine if a machine can exhibit human intelligence.
"""

# Extract concepts and generate questions
concepts = extract_concepts(text)
quiz = generate_mcqs(concepts)

# Display generated questions
for q in quiz:
    print(f"Question: {q['question']}")
    print(f"Choices: {q['choices']}")
    print(f"Answer: {q['answer']}\n")




