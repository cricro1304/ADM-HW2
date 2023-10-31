import json
import time
from collections import Counter

start = time.time()

file = "list.json"

counter = Counter()

with open(file, 'r') as f:
  for i, line in enumerate(f):
    obj = json.loads(line)
    counter.update(obj.get('tags'))

print(counter.most_common(5))

end = time.time()
print(end - start)

