import tkinter as tk
import datetime

def count_calories():
    date = date_entry.get()
    calories_per_serving = int(calories_per_serving_entry.get())
    servings_eaten = int(servings_eaten_entry.get())
    result = calories_per_serving * servings_eaten
    result_label.config(text="Total calories consumed: " + str(result))
    with open("calories_consumed.txt", "a") as f:
        f.write(f"{date},{result}\n")

app = tk.Tk()
app.geometry("400x250")
app.title("Calorie Counter")

date_label = tk.Label(text="Date (YYYY-MM-DD):")
date_entry = tk.Entry()
calories_per_serving_label = tk.Label(text="Calories per serving:")
calories_per_serving_entry = tk.Entry()
servings_eaten_label = tk.Label(text="Servings eaten:")
servings_eaten_entry = tk.Entry()
count_button = tk.Button(text="Count", command=count_calories)
result_label = tk.Label(text="")

date_label.pack()
date_entry.pack()
calories_per_serving_label.pack()
calories_per_serving_entry.pack()
servings_eaten_label.pack()
servings_eaten_entry.pack()
count_button.pack()
result_label.pack()

app.mainloop()
