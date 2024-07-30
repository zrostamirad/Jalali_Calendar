# appointment_app.py
from tkinter import messagebox

from PIL import Image
from customtkinter import *
import jdatetime
from functools import partial

from calendar_app import CalendarApp


class AppointmentApp:
    def __init__(self, root):
        self.root = root
        self.selected_date = None
        self.appointments = {}

        # GUI components
        self.calendar_app = CalendarApp(root, self.select_date)
        self.label_selected_date = CTkLabel(root, text="No date selected", font=("tahoma", 12))
        self.label_selected_date.grid(row=2, column=0, columnspan=3, pady=10)

        # Use CTkEntry for entering description (single line)
        self.entry_description = CTkEntry(root, width=40)
        self.entry_description.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        add_button = CTkButton(root, text="Add Appointment", command=self.add_appointment)
        add_button.grid(row=3, column=2, padx=10, pady=10)

        self.appointment_list = CTkLabel(root, text="Appointments:", font=("tahoma", 12))
        self.appointment_list.grid(row=4, column=0, columnspan=3, pady=10)

        self.update_appointment_list()

    def select_date(self, selected_date):
        self.selected_date = (
            selected_date["year"],
            selected_date["month"],
            selected_date["day"]
        )
        self.label_selected_date.configure(
            text=f"Selected Date: {selected_date['day']:02}/{selected_date['month']:02}/{selected_date['year']} ({selected_date['week']})"
        )
        self.show_appointments_for_date(self.selected_date)

    def add_appointment(self):
        if self.selected_date:
            description = self.entry_description.get()
            if description:
                if self.selected_date not in self.appointments:
                    self.appointments[self.selected_date] = []
                self.appointments[self.selected_date].append(description)
                self.update_appointment_list()

    def update_appointment_list(self):
        appointments_text = ""
        for date, descriptions in self.appointments.items():
            year, month, day = date
            date_str = f"{day:02}/{month:02}/{year} ({days_of_week[jdatetime.date(year, month, day).weekday()]})"
            appointments_text += f"\n{date_str}:\n"
            for desc in descriptions:
                appointments_text += f" - {desc}\n"
        self.appointment_list.configure(text="Appointments:" + appointments_text)

    def show_appointments_for_date(self, selected_date):
        if selected_date in self.appointments:
            appointments_text = ""
            year, month, day = selected_date
            date_str = f"{day:02}/{month:02}/{year} ({days_of_week[jdatetime.date(year, month, day).weekday()]})"
            appointments_text += f"\nAppointments for {date_str}:\n"
            for desc in self.appointments[selected_date]:
                appointments_text += f" - {desc}\n"
            messagebox.showinfo(f"Appointments for {date_str}", appointments_text)
        else:
            pass


days_of_week = ["شنبه", "یکشنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنج شنبه", "جمعه"]
