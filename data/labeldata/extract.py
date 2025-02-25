# read the content from static_analysis.md line by line
with open('static_analysis.md') as f:
    content = f.readlines()

cnt = 0
new_lines = set([])
for line in content:
    if line == '\n':
        continue
    cnt += 1
    
    # fill [5] LLM Meets Bounded Model Checking: Neuro-symbolic Loop Invariant Inference (ASE2024) 5 with line
    # extract the index number and the title and venue
    line = line.strip()
    idx = line.find(']')
    title = line[idx+2:line.find('(')-1]
    venue = line[line.find('(')+1:line.find(')')]
    print(f"Title: {title}, Venue: {venue}")
    new_line = f"{title}"
    new_lines.add(new_line)
    print(cnt)

print(len(new_lines))
# # dump to static_analysis.md
# with open('static_analysis.md', 'w') as f:
#     f.writelines("\n".join(new_lines))


    
