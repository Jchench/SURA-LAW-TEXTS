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

# PL111-203

with open('src/machine_readable/PL111_203.txt', 'r') as f:
  PL111_203_text = f.read()

PL111_203_num = num_tokens_from_string(PL111_203_text, "cl100k_base")

# PL115-174

with open('src/machine_readable/PL115_174.txt', 'r') as f:
  PL115_174_text = f.read()

PL115_174_num = num_tokens_from_string(PL115_174_text, "cl100k_base")

# PL116-283

with open('src/machine_readable/PL116_283.txt', 'r') as f:
  PL116_283_text = f.read()

PL116_283_num = num_tokens_from_string(PL116_283_text, "cl100k_base")

# PL111-022

with open('src/machine_readable/PL111_022.txt', 'r') as f:
  PL111_022_text = f.read()

PL111_022_num = num_tokens_from_string(PL111_022_text, "cl100k_base")

# PL110-343

with open('src/machine_readable/PL110_343.txt', 'r') as f:
  PL110_343_text = f.read()

PL110_343_num = num_tokens_from_string(PL110_343_text, "cl100k_base")

# PL110-289

with open('src/machine_readable/PL110_289.txt', 'r') as f:
  PL110_289_text = f.read()

PL110_289_num = num_tokens_from_string(PL110_289_text, "cl100k_base")

# PL109-351

with open('src/machine_readable/PL109_351.txt', 'r') as f:
  PL109_351_text = f.read()

PL109_351_num = num_tokens_from_string(PL109_351_text, "cl100k_base")

# PL108-159

with open('src/machine_readable/PL108_159.txt', 'r') as f:
  PL108_159_text = f.read()

PL108_159_num = num_tokens_from_string(PL108_159_text, "cl100k_base")

# PL100-108

with open('src/machine_readable/PL100_108.txt', 'r') as f:
  PL100_108_text = f.read()

PL100_108_num = num_tokens_from_string(PL100_108_text, "cl100k_base")

# PL107-204

with open('src/machine_readable/PL107_204.txt', 'r') as f:
  PL107_204_text = f.read()

PL107_204_num = num_tokens_from_string(PL107_204_text, "cl100k_base")

# PL107-056

with open('src/machine_readable/PL107_056.txt', 'r') as f:
  PL107_056_text = f.read()

PL107_056_num = num_tokens_from_string(PL107_056_text, "cl100k_base")

# Table

table = PrettyTable()

table.add_column("law text", )
table.add_column("token length", )

print(table)
