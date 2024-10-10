import csv
import random
file_name = 'Q&A.csv'
output_file_name = 'Q&A_points.csv'

with open(file_name, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    # great work with the file reading/writing

    headers = next(csv_reader)
    questions_list = list(csv_reader)
    random.shuffle(questions_list)

    updated_rows = [headers + ['points']] # why use this structure in the result file? Why not just show final result or which answer was correct?
    # do you intend to use that information later?

    total_points = 0

    for row in questions_list:
        # Wyświetlanie pytania i odpowiedzi
        print(f"Question: {row[0]}")
        print(f"A) {row[1]}")
        print(f"B) {row[2]}")
        print(f"C) {row[3]}")
        print(f"D) {row[4]}")

        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        while answer not in ['A', 'B', 'C', 'D']:
            print("Invalid answer. Please enter A, B, C, or D.")
            answer = input("Enter your answer (A, B, C, or D): ").strip().upper() # doubling of almost the same print, try to simplify it

        correct_answer = row[5].strip().upper() # i don't really understand the intent here? do you want to add the correct answer as another column in the csv?
        if answer == correct_answer:
                print("Correct!")
                points = 1
                total_points += 1
        else:
                print(f"Incorrect! The correct answer was: {correct_answer}")
                points = 0
        updated_rows.append(row + [points])

        print("\n")

with open(output_file_name, mode='w', encoding='utf-8', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerows(updated_rows)

print(f"Quiz completed! You scored {total_points} points. Results saved to 'Q&A_points'.")


# overall good job :) you have some place to improve as it won't run in the current form, but you're going in the right direction :)
