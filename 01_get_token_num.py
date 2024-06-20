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

# PL106-102

with open('src/machine_readable/PL106_102.txt', 'r') as f:
  PL106_102_text = f.read()

PL106_102_num = num_tokens_from_string(PL106_102_text, "cl100k_base")

# PL105-310

with open('src/machine_readable/PL105_310.txt', 'r') as f:
  PL105_310_text = f.read()

PL105_310_num = num_tokens_from_string(PL105_310_text, "cl100k_base")

# PL104-208

with open('src/machine_readable/PL104_208.txt', 'r') as f:
  PL104_208_text = f.read()

PL104_208_num = num_tokens_from_string(PL104_208_text, "cl100k_base")

# PL103-328

with open('src/machine_readable/PL103_328.txt', 'r') as f:
  PL103_328_text = f.read()

PL103_328_num = num_tokens_from_string(PL103_328_text, "cl100k_base")

# PL103-325

with open('src/machine_readable/PL103_325.txt', 'r') as f:
  PL103_325_text = f.read()

PL103_325_num = num_tokens_from_string(PL103_325_text, "cl100k_base")

# PL103-204

with open('src/machine_readable/PL103_204.txt', 'r') as f:
  PL103_204_text = f.read()

PL103_204_num = num_tokens_from_string(PL103_204_text, "cl100k_base")

# PL102-550-4044

with open('src/machine_readable/PL102_550_4044.txt', 'r') as f:
  PL102_550_4044_text = f.read()

PL102_550_4044_num = num_tokens_from_string(PL102_550_4044_text, "cl100k_base")

# PL102-550-3672

with open('src/machine_readable/PL102_550_3672.txt', 'r') as f:
  PL102_550_3672_text = f.read()

PL102_550_3672_num = num_tokens_from_string(PL102_550_3672_text, "cl100k_base")

# Table

table = PrettyTable()

table.add_column("law text", 
["PL111-203", "PL115-174", "PL116-283", "PL111-022", "PL110-343", "PL110-289",
"PL109-351", "PL108-159", "PL100-108", "PL107-204", "PL107-056", "PL106-102",
"PL105-310", "PL104-208", "PL103-328", "PL103-325", "PL103-204", "PL102-550-4044",
"PL102-550-3672"])

table.add_column("token length", 
[PL111_203_num, PL115_174_num, PL116_283_num, PL111_022_num,
PL110_343_num, PL110_289_num, PL109_351_num, PL108_159_num, PL100_108_num,
PL107_204_num, PL107_056_num, PL106_102_num, PL105_310_num, PL104_208_num, 
PL103_328_num, PL103_325_num, PL103_204_num, PL102_550_4044_num, PL102_550_3672_num])

print(table)
