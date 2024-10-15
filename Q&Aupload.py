import pandas as pd

#file_path = 'C:\Users\panho\Documents\2. DARIA\Python vol.2 - Quiz Game\Q&A.csv' - not needed
questions_df = pd.read_csv(file_path) #add file name in apostrophies

def ask_questions(questions_df):
    for index, row in questions_df.iterrows():

        print(f"question {index + 1}: {row['question']}")
        print(f"A) {row['answer_a']}")
        print(f"B) {row['answer_b']}")
        print(f"C) {row['answer_c']}")
        print(f"D) {row['answer_d']}")


        answer = input("Choose your answer: A, B, C, D").strip().upper()


        while answer not in ['A', 'B', 'C', 'D']:
            print("Incorrect. Choose answer A, B, C or D")
            answer = input("Choose answer:").strip().upper()

        print("\n")

ask_questions(questions_df)

# Overall good job! It does what it's supposed to do. Please change the file name to smth without spaces. 
# Try thinking of how you'll be checking if the answer is correct and how to make the questions random :)
