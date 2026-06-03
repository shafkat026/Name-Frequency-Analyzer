# Name Frequency Analyzer

I vibe-coded this tool; you might find it useful too.

This script processes a text file (`names.txt`) to count how many times each name appears; 
sorts them alphabetically and saves the results into a new file (`QN_BAnk.txt`).

How it works:

1. Read: Pulls names from the source file while stripping whitespace.
2. Count: Uses `collections.Counter` to tally occurrences efficiently.
3. Sort: Organizes the data alphabetically.
4. Export: Writes the final count list to `QN_BAnk.txt` for your records.

This tool is ideal for quickly generating clean, summarized reports from raw text lists.

