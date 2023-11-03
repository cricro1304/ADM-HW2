jq -r '.[] | {id, title, sum_books_count: ([.works[].books_count | tonumber] | add)} | "\(.sum_books_count) \(.title) \(.id)"' series.json | sort -nr | head -n5

# this is the solution given by gpt4, but apparently it does not work.
