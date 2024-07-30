from calendar_app import CalendarApp
from customtkinter import *
from appointment_app import AppointmentApp  # Import the AppointmentApp class


def selected_date(date_info):
    print(f" Date: {date_info}")


def main():
    set_appearance_mode("dark")
    set_default_color_theme("blue")

    app = CTk()
    app.title("تقویم جلالی")

    calendar_app = CalendarApp(app, selected_date)

    # Adding appointment functionality
    appointment_app = AppointmentApp(app)

    app.mainloop()


if __name__ == "__main__":
    main()
