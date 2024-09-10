import json
import tkinter as tk

#Access the data file 
with open('data_file.json', 'r') as file:
    data = json.load(file)
  
#Accept entry and verify it
score = 0
counter = 0
def get_answer():
    global score
    global counter
    answer = entry.get()
    
    if answer.capitalize() == correct_answer:
        score += 1
        for widget in window.winfo_children():
            widget.destroy()
        next_question = 'You got it rigth! Here is the next question'
        tk_next_question = tk.Label( window, text = next_question, width=52, height=5, anchor="center", justify="center")
        tk_next_question.pack()
        tk_score = tk.Label( window, text = f'Your score is now {score}.', width=52, anchor="center", justify="center")
        tk_score.pack()
        window.after(2000, window.destroy)
    elif answer.capitalize() in suggestions:
        entry.delete(0, tk.END)
        counter += 1
        number_tries = 3 - counter
        feedback = f'It is an incorrect answer!   You got {number_tries} tries left.'
        if counter == 3:
            window.after(2000, window.destroy)
        
    else:
        entry.delete(0, tk.END)
        counter += 1
        number_tries = 3 - counter
        feedback = f'The answer is different from the suggestions!   You got {number_tries} tries left.'
        if counter == 3:
            window.after(2000, window.destroy)
    
    output.config(text=feedback)
    
    

#Access the questions, the suggestions and the sollutions one by one
number_of_questions = len(data['quiz']["questions"])
question_number = 0

for number_of_question_data in range(number_of_questions):
    #creating a new window
    window = tk.Tk()
    window.resizable(height=5, width=52)
    window.title('Quiz')
    #Question number
    question_number += 1
    tk_question_number = tk.Label( window, text = f"Question {question_number}", width=52, anchor="center", justify="center")
    tk_question_number.pack()
    #Question
    question = data['quiz']["questions"][number_of_question_data]['question']
    tk_question = tk.Label( window, text = question, width=52, anchor="center", justify="center")
    tk_question.pack()
    #Suggestions
    suggestions = data['quiz']["questions"][number_of_question_data]['options']
    option_number = 0
    for option in suggestions:
        option_number += 1
        option_text = f'{option_number}) {option}'
        tk_option_text = tk.Label( window, text = option_text, width=52, anchor="center", justify="center")
        tk_option_text.pack()
    #Correct answer
    correct_answer = data['quiz']["questions"][number_of_question_data]['answer']
    #Entry area
    entry_text = 'Write your answer here: '
    tk_entry_text = tk.Label(window, text=entry_text, anchor="center", justify="center")
    tk_entry_text.pack()
    entry = tk.Entry()
    entry.pack()
    #Accept button
    button = tk.Button(window, text="Submit", command=get_answer)
    button.pack()
    # Feedback label
    output = tk.Label(window, height=2, width=52, anchor="center", justify="center")
    output.pack()
    window.mainloop()
#Finishing window
window = tk.Tk()
window.resizable(height=5, width=52)
window.title('Quiz')
finish_text = 'You finished the game!        Good job!'
tk_finish_text = tk.Label(window, height=2, width=52, anchor="center", justify="center", text = finish_text )
tk_finish_text.pack()
tk_score = tk.Label( window, text = f'Your score is now {score}.', width=52, anchor="center", justify="center")
tk_score.pack()
window.after(3000, window.destroy)
window.mainloop()
