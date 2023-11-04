# Select one alternative library to Pandas, upload authors.json dataset, and filter authors with at least 100 reviews.

import dask.dataframe as dd
import dask
import time
import pandas as pd

start = time.time()

df = dd.read_json('authors.json', blocksize=2e7)
filtered_data_frame = df[df['text_reviews_count'] > 100]
filtered_data_frame = filtered_data_frame.compute()
print(filtered_data_frame[["name", "text_reviews_count"]])

end = time.time()
print(end - start)

# by running this script with dask, it took 276.53 seconds

# Do the same using Pandas and compare performance in terms of milliseconds.
import pandas as pd
start = time.time()

chunk_size = 100000  

json_reader = pd.read_json('authors.json', lines=True, chunksize=chunk_size)


filtered_chunks = []


filter_value = 100


for chunk in json_reader:
    
    filtered_chunk = chunk[chunk['text_reviews_count'] > 100]
    filtered_chunks.append(filtered_chunk)


filtered_data = pd.concat(filtered_chunks)

print(filtered_data)

end = time.time()
print(end - start)

# by running this script with pandas, it took 1762.75 seconds. it has been slightly changed if compared with the one used with dask
# since it was taking too much using the same script. to optimize the code a bit we chose to split the dataset in more chunks.
# even by adopting these changes, it took about 5 times longer than when we used dask.
