import re

with open('scratch/tiramisu.js', 'r', encoding='utf-8') as f:
    content = f.read()

pos = 3324359
with open('scratch/tiramisu.js', 'r', encoding='utf-8') as f:
    content = f.read()

start = pos - 100
end = pos + 2500
print(content[start:end])

