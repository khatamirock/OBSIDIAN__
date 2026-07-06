import csv, re

input_file = "my_local/1/1_1-40.md"
output_file = "questions.csv"

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# Split on a marker like '### ' (adjust depending on your file)
blocks = re.split(r'\n\s*###\s*', content)
rows = []

for block in blocks:
    if not block.strip():
        continue
    # Assuming first line is the question, then options, then answer and maybe explanation.
    lines = block.strip().splitlines()
    question = lines[0].strip()
    optionA = optionB = optionC = optionD = ""
    answer = ""
    explanation = ""
    
    # Get options (assuming they are lines that start with (a), (b), (c), (d))
    for line in lines:
        if line.strip().lower().startswith("(a)"):
            optionA = re.sub(r'^\(a\)\s*', '', line.strip())
        elif line.strip().lower().startswith("(b)"):
            optionB = re.sub(r'^\(b\)\s*', '', line.strip())
        elif line.strip().lower().startswith("(c)"):
            optionC = re.sub(r'^\(c\)\s*', '', line.strip())
        elif line.strip().lower().startswith("(d)"):
            optionD = re.sub(r'^\(d\)\s*', '', line.strip())
        elif line.strip().startswith("Ans:"):
            # Remove "Ans:" and any trailing punctuation/whitespace
            answer = line.split("Ans:")[-1].strip(" ?")
        # You can add extra parsing for "Note:" if available
    rows.append([question, optionA, optionB, optionC, optionD, answer, explanation])

with open(output_file, "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Question", "Option A", "Option B", "Option C", "Option D", "Answer", "Explanation"])
    writer.writerows(rows)
