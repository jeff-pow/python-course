# Program computes the final average grade of a course given values for the various grade categories.
# Jeff Powell
# CSC295
# 11/27/23

import tkinter as tk
import tkinter.messagebox


class CalculatorGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('Calculator')
        self.main_window.geometry('2000x1200')

        self.top_frame = tk.Frame(self.main_window)
        self.top_frame.pack()
        self.bottom_frame = tk.Frame(self.main_window)
        self.bottom_frame.pack()

        self.a = tk.Label(self.top_frame, text="Activity Average")
        self.a.pack()
        self.activity_avg = tk.Entry(self.top_frame, width=10)
        self.activity_avg.pack()

        self.b = tk.Label(self.top_frame, text="Lab Average")
        self.b.pack()
        self.lab_avg = tk.Entry(self.top_frame, width=10)
        self.lab_avg.pack()

        self.c = tk.Label(self.top_frame, text="Project Average")
        self.c.pack()
        self.project_avg = tk.Entry(self.top_frame, width=10)
        self.project_avg.pack()

        self.d = tk.Label(self.top_frame, text="Exam Average")
        self.d.pack()
        self.exam_avg = tk.Entry(self.top_frame, width=10)
        self.exam_avg.pack()

        self.include_final_flag = tk.IntVar()
        self.include_final = tk.Checkbutton(self.top_frame, text="Include Final Exam Average?", variable=self.include_final_flag, onvalue=1, offvalue=0)
        self.include_final.pack()

        self.e = tk.Label(self.top_frame, text="Final Exam Average")
        self.e.pack()
        self.final_avg = tk.Entry(self.top_frame, width=10)
        self.final_avg.pack()

        self.calc_button = tk.Button(
            self.bottom_frame, text="Calculate Grade", command=self.calculate_grade)
        self.calc_button.pack()

        self.quit = tk.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)
        self.quit.pack()
        tk.mainloop()

    def calculate_grade(self):
        print(self.include_final_flag.get())
        # Divide by 100% if we're including the final, otherwise divide by 80%.
        if (self.include_final_flag.get() == 1):
            denom = 100
        else:
            denom = 80
        grade = float(self.activity_avg.get()) * 15 / denom + float(self.lab_avg.get()) * 15 / denom + float(self.project_avg.get()) * 20 / denom \
            + float(self.exam_avg.get()) * 30 / denom + float(self.final_avg.get()) * self.include_final_flag.get() * 20 / denom
        # If we include the final, the flag variable will be set to one so we multiply by one to include the value parsed from the box.
        # Otherwise, the flag variable is set to zero so whatever is in the final_avg box will be ignored.
        message = f'Grade calculated is {grade:.2f}%'
        tk.messagebox.showinfo('Response', message)


if __name__ == "__main__":
    calculator = CalculatorGUI()
