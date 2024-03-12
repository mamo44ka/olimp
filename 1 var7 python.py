import csv

with open('books.csv', encoding ='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=','))
    for row in reader:
        if '' in row['']:
            print(f'')

        sum_score[row['class']] = sum_score.get(row['class'], 0) + (int(row['score']) if row['score'] != 'None' else 0)
        count_scores[row['class']] = count_scores.get(row['class'], 0) + 1

    for row in reader:
    writer.writerows(reader)