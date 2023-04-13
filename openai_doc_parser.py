# Import Modules
# import openai
from transformers import pipeline
from pdf_to_txt import pdf_to_txt
import sys

# Fetch file paths.
pdf_file_path  = sys.argv[1]
save_path = sys.argv[2]

# Define open ai paramters.
# MODEL = "gpt-3.5-turbo"


# Read API Key from a text file.
secret_key = ""
secret_key = open("key.txt", "r").readline().strip()

# Assign secret key to api_key attribute.
# openai.api_key = secret_key



# Convert pdf to text data.
pdf_to_txt(pdf_file_path, save_path)

# Print the content that was saved to the text file.
content_lines = open(save_path, "r").readlines()
content_lines = "".join(content_lines)
print(content_lines)


qa_model = pipeline("question-answering")
question = "What's the best way to earn money?"
context = content_lines
answer_dict = qa_model(question = question, context = context)
print(answer_dict['answer'])
# prompt = f"I want to answer my questions in context to this data \"{content_lines}\""


# print(prompt)


# completion = openai.ChatCompletion.create(
# model = MODEL,
# message = [{"role":"user", "content":prompt}],

# )

# print(completion)