%pip install --upgrade tiktoken
%pip install --upgrade openai

import tiktoken
import os
from prettytable import PrettyTable

encoding = tiktoken.get_encoding("cl100k_base")
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# function
def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

# double check directories
print(os.listdir('src/machine_readable'))

# PUBL203

with open('src/machine_readable/PUBL203.txt', 'r') as f:
  PUBL203_text = f.read()

PUBL203_num = num_tokens_from_string(PUBL203_text, "cl100k_base")

# PUBL174

with open('src/machine_readable/PUBL174.txt', 'r') as f:
  PUBL174_text = f.read()

PUBL174_num = num_tokens_from_string(PUBL174_text, "cl100k_base")

# PUBL283

with open('src/machine_readable/PUBL283.txt', 'r') as f:
  PUBL283_text = f.read()

PUBL283_num = num_tokens_from_string(PUBL283_text, "cl100k_base")

# PUBL022

with open('src/machine_readable/PUBL022.txt', 'r') as f:
  PUBL022_text = f.read()

PUBL022_num = num_tokens_from_string(PUBL022_text, "cl100k_base")

# PUBL343

with open('src/machine_readable/PUBL343.txt', 'r') as f:
  PUBL343_text = f.read()

PUBL343_num = num_tokens_from_string(PUBL343_text, "cl100k_base")

# Table

table = PrettyTable()

table.add_column("law text", ["PUBL203", "PUBL174", "PUBL283", "PUBL022", "PUBL343"])
table.add_column("token length", [PUBL203_num, PUBL174_num, PUBL283_num, PUBL022_num, PUBL343_num])

print(table)
