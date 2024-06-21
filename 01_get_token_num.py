# %pip install --upgrade tiktoken
# %pip install --upgrade openai

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

# Table

table = PrettyTable()

# PL111-203

with open('src/machine_readable/PL111_203.txt', 'r') as f:
  PL111_203_text = f.read()

PL111_203_num = num_tokens_from_string(PL111_203_text, "cl100k_base")

table.add_column("law text", ["PL111-203"])
table.add_column("token length", [PL111_203_num])

# PL115-174

with open('src/machine_readable/PL115_174.txt', 'r') as f:
  PL115_174_text = f.read()

PL115_174_num = num_tokens_from_string(PL115_174_text, "cl100k_base")

table.add_row(["PL115-174", PL115_174_num])

# PL116-283

with open('src/machine_readable/PL116_283.txt', 'r') as f:
  PL116_283_text = f.read()

PL116_283_num = num_tokens_from_string(PL116_283_text, "cl100k_base")

table.add_row(["PL116-283", PL116_283_num])

# PL111-022

with open('src/machine_readable/PL111_022.txt', 'r') as f:
  PL111_022_text = f.read()

PL111_022_num = num_tokens_from_string(PL111_022_text, "cl100k_base")

table.add_row(["PL111-022", PL111_022_num])

# PL110-343

with open('src/machine_readable/PL110_343.txt', 'r') as f:
  PL110_343_text = f.read()

PL110_343_num = num_tokens_from_string(PL110_343_text, "cl100k_base")

table.add_row(["PL110-343", PL110_343_num])

# PL110-289

with open('src/machine_readable/PL110_289.txt', 'r') as f:
  PL110_289_text = f.read()

PL110_289_num = num_tokens_from_string(PL110_289_text, "cl100k_base")

table.add_row(["PL110-289", PL110_289_num])

# PL109-351

with open('src/machine_readable/PL109_351.txt', 'r') as f:
  PL109_351_text = f.read()

PL109_351_num = num_tokens_from_string(PL109_351_text, "cl100k_base")

table.add_row(["PL109-351", PL109_351_num])

# PL108-159

with open('src/machine_readable/PL108_159.txt', 'r') as f:
  PL108_159_text = f.read()

PL108_159_num = num_tokens_from_string(PL108_159_text, "cl100k_base")

table.add_row(["PL108-159", PL108_159_num])

# PL100-108

with open('src/machine_readable/PL100_108.txt', 'r') as f:
  PL100_108_text = f.read()

PL100_108_num = num_tokens_from_string(PL100_108_text, "cl100k_base")

table.add_row(["PL100-108", PL100_108_num])

# PL107-204

with open('src/machine_readable/PL107_204.txt', 'r') as f:
  PL107_204_text = f.read()

PL107_204_num = num_tokens_from_string(PL107_204_text, "cl100k_base")

table.add_row(["PL107-204", PL107_204_num])

# PL107-056

with open('src/machine_readable/PL107_056.txt', 'r') as f:
  PL107_056_text = f.read()

PL107_056_num = num_tokens_from_string(PL107_056_text, "cl100k_base")

table.add_row(["PL107-056", PL107_056_num])

# PL106-102

with open('src/machine_readable/PL106_102.txt', 'r') as f:
  PL106_102_text = f.read()

PL106_102_num = num_tokens_from_string(PL106_102_text, "cl100k_base")

table.add_row(["PL106-102", PL106_102_num])

# PL105-310

with open('src/machine_readable/PL105_310.txt', 'r') as f:
  PL105_310_text = f.read()

PL105_310_num = num_tokens_from_string(PL105_310_text, "cl100k_base")

table.add_row(["PL105-310", PL105_310_num])

# PL104-208

with open('src/machine_readable/PL104_208.txt', 'r') as f:
  PL104_208_text = f.read()

PL104_208_num = num_tokens_from_string(PL104_208_text, "cl100k_base")

table.add_row(["PL104-208", PL104_208_num])

# PL103-328

with open('src/machine_readable/PL103_328.txt', 'r') as f:
  PL103_328_text = f.read()

PL103_328_num = num_tokens_from_string(PL103_328_text, "cl100k_base")

table.add_row(["PL103-328", PL103_328_num])

# PL103-325

with open('src/machine_readable/PL103_325.txt', 'r') as f:
  PL103_325_text = f.read()

PL103_325_num = num_tokens_from_string(PL103_325_text, "cl100k_base")

table.add_row(["PL103-325", PL103_325_num])

# PL103-204

with open('src/machine_readable/PL103_204.txt', 'r') as f:
  PL103_204_text = f.read()

PL103_204_num = num_tokens_from_string(PL103_204_text, "cl100k_base")

table.add_row(["PL103-204", PL103_204_num])

# PL102-550-4044

with open('src/machine_readable/PL102_550_4044.txt', 'r') as f:
  PL102_550_4044_text = f.read()

PL102_550_4044_num = num_tokens_from_string(PL102_550_4044_text, "cl100k_base")

table.add_row(["PL102-550-4044", PL102_550_4044_num])

# PL102-550-3672

with open('src/machine_readable/PL102_550_3672.txt', 'r') as f:
  PL102_550_3672_text = f.read()

PL102_550_3672_num = num_tokens_from_string(PL102_550_3672_text, "cl100k_base")

table.add_row(["PL102-550-3672", PL102_550_3672_num])

# PL102-242-2334

with open('src/machine_readable/PL102_242_2334.txt', 'r') as f:
  PL102_242_2334_text = f.read()

PL102_242_2334_num = num_tokens_from_string(PL102_242_2334_text, "cl100k_base")

table.add_row(["PL102-242-2334", PL102_242_2334_num])

# PL102-242

with open('src/machine_readable/PL102_242.txt', 'r') as f:
  PL102_242_text = f.read()

PL102_242_num = num_tokens_from_string(PL102_242_text, "cl100k_base")

table.add_row(["PL102-242", PL102_242_num])

# PL101-647

with open('src/machine_readable/PL101_647.txt', 'r') as f:
  PL101_647_text = f.read()

PL101_647_num = num_tokens_from_string(PL101_647_text, "cl100k_base")

table.add_row(["PL101-647", PL101_647_num])

# PL101-073

with open('src/machine_readable/PL101_073.txt', 'r') as f:
  PL101_073_text = f.read()

PL101_073_num = num_tokens_from_string(PL101_073_text, "cl100k_base")

table.add_row(["PL101-073", PL101_073_num])

# PL100-086

with open('src/machine_readable/PL100_086.txt', 'r') as f:
  PL100_086_text = f.read()

PL100_086_num = num_tokens_from_string(PL100_086_text, "cl100k_base")

table.add_row(["PL100-086", PL100_086_num])

# PL099-570-3207

with open('src/machine_readable/PL099_570_3207.txt', 'r') as f:
  PL099_570_3207_text = f.read()

PL099_570_3207_num = num_tokens_from_string(PL099_570_3207_text, "cl100k_base")

table.add_row(["PL099-570-3207", PL099_570_3207_num])

# PL098-181-1278

with open('src/machine_readable/PL098_181_1278.txt', 'r') as f:
  PL098_181_1278_text = f.read()

PL098_181_1278_num = num_tokens_from_string(PL098_181_1278_text, "cl100k_base")

table.add_row(["PL098-181-1278", PL098_181_1278_num])

# PL097-320

with open('src/machine_readable/PL097_320.txt', 'r') as f:
  PL097_320_text = f.read()

PL097_320_num = num_tokens_from_string(PL097_320_text, "cl100k_base")

table.add_row(["PL097-320", PL097_320_num])

# PL095-630-3697

with open('src/machine_readable/PL095_630_3697.txt', 'r') as f:
  PL095_630_3697_text = f.read()

PL095_630_3697_num = num_tokens_from_string(PL095_630_3697_text, "cl100k_base")

table.add_row(["PL095-630-3697", PL095_630_3697_num])

# PL096-221

with open('src/machine_readable/PL096_221.txt', 'r') as f:
  PL096_221_text = f.read()

PL096_221_num = num_tokens_from_string(PL096_221_text, "cl100k_base")

table.add_row(["PL096-221", PL096_221_num])

# PL095-369

with open('src/machine_readable/PL095_369.txt', 'r') as f:
  PL095_369_text = f.read()

PL095_369_num = num_tokens_from_string(PL095_369_text, "cl100k_base")

table.add_row(["PL095-369", PL095_369_num])

# PL095-109

with open('src/machine_readable/PL095_109.txt', 'r') as f:
  PL095_109_text = f.read()

PL095_109_num = num_tokens_from_string(PL095_109_text, "cl100k_base")

table.add_row(["PL095-109", PL095_109_num])

# PL094-239

with open('src/machine_readable/PL094_239.txt', 'r') as f:
  PL094_239_text = f.read()

PL094_239_num = num_tokens_from_string(PL094_239_text, "cl100k_base")

table.add_row(["PL094-239", PL094_239_num])

# PL094-240

with open('src/machine_readable/PL94_240.txt', 'r') as f:
  PL094_240_text = f.read()

PL094_240_num = num_tokens_from_string(PL094_240_text, "cl100k_base")

table.add_row(["PL094-240", PL094_240_num])

# PL094-200

with open('src/machine_readable/PL094_200.txt', 'r') as f:
  PL094_200_text = f.read()

PL094_200_num = num_tokens_from_string(PL094_200_text, "cl100k_base")

table.add_row(["PL094-200", PL094_200_num])

# PL093-495-1551

with open('src/machine_readable/PL093_495_1551.txt', 'r') as f:
  PL093_495_1551_text = f.read()

PL093_495_1551_num = num_tokens_from_string(PL093_495_1551_text, "cl100k_base")

table.add_row(["PL093-495-1551", PL093_495_1551_num])

# PL093-234

with open('src/machine_readable/PL093_234.txt', 'r') as f:
  PL093_234_text = f.read()

PL093_234_num = num_tokens_from_string(PL093_234_text, "cl100k_base")

table.add_row(["PL093-234", PL093_234_num])

# PL091-508

with open('src/machine_readable/PL091_508.txt', 'r') as f:
  PL091_508_text = f.read()

PL091_508_num = num_tokens_from_string(PL091_508_text, "cl100k_base")

table.add_row(["PL091-508", PL091_508_num])

# PL091-507

with open('src/machine_readable/PL091_507.txt', 'r') as f:
  PL091_507_text = f.read()

PL091_507_num = num_tokens_from_string(PL091_507_text, "cl100k_base")

table.add_row(["PL091-507", PL091_507_num])

# PL090-321

with open('src/machine_readable/PL090_321.txt', 'r') as f:
  PL090_321_text = f.read()

PL090_321_num = num_tokens_from_string(PL090_321_text, "cl100k_base")

table.add_row(["PL090-321", PL090_321_num])

# PL090-284

with open('src/machine_readable/PL090_284.txt', 'r') as f:
  PL090_284_text = f.read()

PL090_284_num = num_tokens_from_string(PL0390_284_text, "cl100k_base")

table.add_row(["PL090-284", PL090_284_num])

# PL089-695

with open('src/machine_readable/PL089_695.txt', 'r') as f:
  PL089_695_text = f.read()

PL089_695_num = num_tokens_from_string(PL089_695_text, "cl100k_base")

table.add_row(["PL089-695", PL089_695_num])

# PL084-511

with open('src/machine_readable/PL084_511.txt', 'r') as f:
  PL084_511_text = f.read()

PL084_511_num = num_tokens_from_string(PL084_511_text, "cl100k_base")

table.add_row(["PL084-511", PL084_511_num])

# PL081-797

with open('src/machine_readable/PL081_797.txt', 'r') as f:
  PL081_797_text = f.read()

PL081_797_num = num_tokens_from_string(PL081_797_text, "cl100k_base")

table.add_row(["PL081-797", PL081_797_num])

# PL074-305

with open('src/machine_readable/PL074_305.txt', 'r') as f:
  PL074_305_text = f.read()

PL074_305_num = num_tokens_from_string(PL074_305_text, "cl100k_base")

table.add_row(["PL074-305", PL074_305_num])

# PL073-066

with open('src/machine_readable/PL073_066.txt', 'r') as f:
  PL073_066_text = f.read()

PL073_066_num = num_tokens_from_string(PL073_066_text, "cl100k_base")

table.add_row(["PL073-066", PL073_066_num])

# PL069-639

with open('src/machine_readable/PL069_639.txt', 'r') as f:
  PL069_639_text = f.read()

PL069_639_num = num_tokens_from_string(PL069_639_text, "cl100k_base")

table.add_row(["PL069-639", PL069_639_num])

# PL063-043

with open('src/machine_readable/PL063_043.txt', 'r') as f:
  PL063_043_text = f.read()

PL063_043_num = num_tokens_from_string(PL063_043_text, "cl100k_base")

table.add_row(["PL063-0439", PL063_043_num])

# CHPT-106

with open('src/machine_readable/CHPT_106.txt', 'r') as f:
  CHPT_106_text = f.read()

CHPT_106_num = num_tokens_from_string(CHPT_106_text, "cl100k_base")

table.add_row(["CHPT-106", CHPT_106_num])

# print table

print(table)

# save table out

import csv

with open('table.csv', 'w', newline='') as f_output:
    f_output.write(table.get_csv_string())
    

