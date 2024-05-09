import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image

class WelcomePage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Welcome to BMI Calculator")

        # Set frame size
        self.root.geometry("500x500")

        # Set background image for welcome frame
        self.bg_image = Image.open("bmi-2.jpg")
        self.bg_image_resized = self.bg_image.resize((500, 500))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image_resized)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Welcome message
        self.label_welcome = tk.Label(self.bg_label, text="Welcome to BMI Calculator", font=("Helvetica", 20), fg="green", bg="white")
        self.label_welcome.pack(pady=20)

        # Instruction message
        self.label_instruction = tk.Label(self.bg_label, text="Please click below to start calculating your BMI", font=("Helvetica", 14), bg="white")
        self.label_instruction.pack(pady=10)

        # Start BMI Calculator button
        self.button_start = tk.Button(self.bg_label, text="Start BMI Calculator", command=self.start_bmi_calculator, font=("Helvetica", 16), bg="blue", fg="white")
        self.button_start.pack(pady=20)

        # View Data button
        self.button_view = tk.Button(self.bg_label, text="View Data", command=self.view_data, font=("Helvetica", 16), bg="orange", fg="white")
        self.button_view.pack(pady=10)

    def start_bmi_calculator(self):
        # Close the welcome page
        self.root.withdraw()

        # Start the BMI calculator application
        BMI()

    def view_data(self):
        # Close the welcome page
        self.root.withdraw()

        # Show data window
        data_window = DataWindow()
        data_window.show_data()


class BMI:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("BMI Calculator")

        # Set frame size
        self.root.geometry("500x500")

        # Set background image for calculator frame
        self.bg_image = Image.open("bmi-image.jpg")
        self.bg_image_resized = self.bg_image.resize((500, 500))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image_resized)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Increase font size and make labels colorful
        self.label = tk.Label(self.bg_label, text="BMI Calculator", font=("Helvetica", 24), fg="blue", bg="white")
        self.label.pack(pady=20)

        # Creating labels and entry fields for name, age, height, and weight
        self.label_name = tk.Label(self.bg_label, text="Name:", font=("Helvetica", 14), bg="white")
        self.label_name.pack()
        self.entry_name = tk.Entry(self.bg_label, font=("Helvetica", 14))
        self.entry_name.pack(pady=5)

        self.label_age = tk.Label(self.bg_label, text="Age:", font=("Helvetica", 14), bg="white")
        self.label_age.pack()
        self.entry_age = tk.Entry(self.bg_label, font=("Helvetica", 14))
        self.entry_age.pack(pady=5)

        self.label_height = tk.Label(self.bg_label, text="Height (cm):", font=("Helvetica", 14), bg="white")
        self.label_height.pack()
        self.entry_height = tk.Entry(self.bg_label, font=("Helvetica", 14))
        self.entry_height.pack(pady=5)

        self.label_weight = tk.Label(self.bg_label, text="Weight (kg):", font=("Helvetica", 14), bg="white")
        self.label_weight.pack()
        self.entry_weight = tk.Entry(self.bg_label, font=("Helvetica", 14))
        self.entry_weight.pack(pady=5)

        # Increase button size and change color
        self.button = tk.Button(self.bg_label, text="Calculate", command=self.calculate_bmi, font=("Helvetica", 16), bg="green", fg="white")
        self.button.pack(pady=10)

        # Back button
        self.button_back = tk.Button(self.bg_label, text="Back", command=self.go_back, font=("Helvetica", 16))
        self.button_back.pack(pady=10)

        # Connect to MySQL database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aaaa",
            database="bmi_calculator_db"
        )
        self.cursor = self.db.cursor()

    def calculate_bmi(self):
        try:
            name = self.entry_name.get()
            age = int(self.entry_age.get())
            height = float(self.entry_height.get())
            weight = float(self.entry_weight.get())

            if age <= 0 or height <= 0 or weight <= 0:
                messagebox.showerror("Error", "Please enter valid positive values for age, height, and weight.")
                return

            # Calculate BMI
            height_in_meters = height / 100
            bmi = weight / (height_in_meters ** 2)

            # Insert user data into the database
            sql = "INSERT INTO user_data (name, age, height, weight, bmi) VALUES (%s, %s, %s, %s, %s)"
            values = (name, age, height, weight, bmi)
            self.cursor.execute(sql, values)
            self.db.commit()

            # Display BMI category and advice
            if bmi <= 16:
                category = "Severe Thinness"
                advice = "Consider consulting a healthcare professional for immediate support and guidance."
            elif 16 < bmi <= 17:
                category = "Mild Thinness"
                advice = "Focus on a balanced diet and regular exercise for gradual weight gain."
            elif 17 < bmi <= 18.5:
                category = "Moderate Thinness"
                advice = "Focus on a balanced diet and regular exercise for gradual weight gain."
            elif 18.5 < bmi <= 25:
                category = "Normal"
                advice = "Maintain a healthy lifestyle with balanced nutrition and regular physical activity."
            elif 25 < bmi <= 30:
                category = "Overweight"
                advice = "Consider making dietary and lifestyle changes for weight management."
            elif 30 <= bmi <= 35:
                category = "Obese Class I"
                advice = "Focus on adopting healthier habits for weight management."
            elif 35 <= bmi <= 40:
                category = "Obese Class II"
                advice = "Seek support from a healthcare professional for weight management."
            elif bmi > 40:
                category = "Obese Class III"
                advice = "Consult a healthcare professional for personalized weight management advice."

            messagebox.showinfo("BMI Category", f"{category}\n\nAdvice: {advice}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for age, height, and weight.")

    def go_back(self):
        self.root.destroy()
        welcome.root.deiconify()

    def run(self):
        self.root.mainloop()


class DataWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BMI Data")

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        # Connect to MySQL database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aaaa",
            database="bmi_calculator_db"
        )
        self.cursor = self.db.cursor()

    def delete_record(self, id):
        sql = "DELETE FROM user_data WHERE id = %s"
        self.cursor.execute(sql, (id,))
        self.db.commit()
        self.show_data()

    def show_data(self):
        self.frame.destroy()  # Destroy previous frame if it exists
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.cursor.execute("SELECT * FROM user_data")
        data = self.cursor.fetchall()
        for row in data:
            record_frame = tk.Frame(self.frame)
            record_frame.pack(fill="x")

            record_text = "\t".join(str(value) for value in row)
            data_label = tk.Label(record_frame, text=record_text, width=50)
            data_label.pack(side="left", padx=10, pady=5)

            delete_button = tk.Button(record_frame, text="Delete", command=lambda id=row[0]: self.delete_record(id))
            delete_button.pack(side="right", padx=10, pady=5)

            # Add a separator between data entries
            separator = tk.Frame(self.frame, height=1, bg="gray")
            separator.pack(fill="x", pady=5)

        self.root.mainloop()


# Start the welcome page
welcome = WelcomePage()
welcome.root.mainloop()
