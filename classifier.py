import csv


file_path = 'random_numbers.txt'
number_range = [(0, 10), (11, 20), (21, 30), (31, 40), (41, 50),
                (51, 60), (61, 70), (71, 80), (81, 90), (91, 100)]
range_count = {f"{start}-{end}": 0 for start, end in number_range}
total = 0
with open(file_path, 'r') as file:
    for line in file:
        try:
            number = int(line)
            total += 1
            for start, end in number_range:
                if number >= start and number <= end:
                    range_count[f"{start}-{end}"] += 1
                    break
        except ValueError:
            print(f"Invalid number: {line}")

for start, end in number_range:
    print(f"{start}-{end}: {range_count[f'{start}-{end}']}")
print(f"Total: {total}")

output_file = 'random_numbers_summary.csv'
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Range', 'Count'])
    for start, end in number_range:
        writer.writerow([f"{start}-{end}", range_count[f"{start}-{end}"]])
    writer.writerow(['Total', total])
    file.close()

print(f"Summary written to {output_file}")
