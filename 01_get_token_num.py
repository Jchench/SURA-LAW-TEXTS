%pip install --upgrade tiktoken
%pip install --upgrade openai

import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens
  
# PUBL203

with open('clean_law_texts/src/machine_readable/PUBL203.txt', 'r') as f:
  PUBL203_text = f.read()

PUBL203_num = num_tokens_from_string(PUBL203_text, "cl100k_base")

# PUBL174

with open('clean_law_texts/src/machine_readable/PUBL174.txt', 'r') as f:
  PUBL174_text = f.read()

PUBL174_num = num_tokens_from_string(PUBL174_text, "cl100k_base")
