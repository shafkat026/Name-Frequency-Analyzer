from collections import Counter

# Input and output file names
input_file = "names.txt"
output_file = "QN_BAnk.txt"

# Read names from file
with open(input_file, "r", encoding="utf-8") as file:
    names = [line.strip() for line in file if line.strip()]

# Count occurrences
name_count = Counter(names)

# Sort alphabetically
sorted_names = sorted(name_count.items())

# Display results
print("Name Counts:\n")

for name, count in sorted_names:
    print(f"{name}: {count}")

# Save results to another file
with open(output_file, "w", encoding="utf-8") as file:
    for name, count in sorted_names:
        file.write(f"{name}: {count}\n")

print(f"\nSorted results saved in '{output_file}'")