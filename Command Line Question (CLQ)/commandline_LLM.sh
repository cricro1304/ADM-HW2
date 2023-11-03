jq -r '([.works[].books_count | tonumber] | add) as $sum | "\($sum) \(.title) \(.id)"' series.json | sort -nr | head -n5
