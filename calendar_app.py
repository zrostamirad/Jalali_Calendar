from PIL import Image
from customtkinter import *
import jdatetime
from functools import partial


class CalendarApp:
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback
        self.today = jdatetime.date.today()
        self.year = self.today.year
        self.month = self.today.month
        self.imgBack = CTkImage(light_image=Image.open('img/icons8-back-to.png'), size=(40, 40))
        self.imgNext = CTkImage(light_image=Image.open('img/icons8-next-to.png'), size=(40, 40))

        self.calendar_frame = CTkFrame(root)
        self.calendar_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=20)

        self.month_label_text = StringVar()
        self.month_label = CTkLabel(root, textvariable=self.month_label_text, font=("tahoma", 16))
        self.month_label.grid(row=0, column=1, pady=10)

        prev_button = CTkButton(root,
                                text="",
                                image=self.imgBack,
                                fg_color="transparent",
                                hover_color='#F5CEFB',
                                command=self.previous_month)
        prev_button.grid(row=0, column=0, padx=20)

        next_button = CTkButton(root,
                                text="",
                                image=self.imgNext,
                                fg_color="transparent",
                                hover_color="#F5CEFB",
                                command=self.next_month)
        next_button.grid(row=0, column=2, padx=20)

        self.update_calendar()

    def generate_calendar(self):
        calendar_days = [["" for _ in range(7)] for _ in range(6)]
        first_day = jdatetime.date(self.year, self.month, 1)
        start_day = first_day.weekday()

        day = 1
        for week in range(6):
            for weekday in range(7):
                if week == 0 and weekday < start_day:
                    continue
                try:
                    jdate = jdatetime.date(self.year, self.month, day)
                    calendar_days[week][weekday] = str(day).zfill(2)
                    day += 1
                except ValueError:
                    break

        return calendar_days

    def update_calendar(self):
        calendar_days = self.generate_calendar()
        month_name = persian_months[self.month]
        self.month_label_text.set(f"{month_name} {self.year}")

        # پاکسازی ویجت‌های قبلی
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        # اضافه کردن روزهای هفته به ردیف اول
        for col, day in enumerate(days_of_week):
            label = CTkLabel(self.calendar_frame, text=day, width=40, height=40)
            label.grid(row=0, column=col, padx=5, pady=5)

        # اضافه کردن روزهای ماه به تقویم
        for row in range(6):
            for col in range(7):
                day = calendar_days[row][col] if col < len(calendar_days[row]) else ""
                if day:
                    day_int = int(day)
                    label = CTkButton(self.calendar_frame,
                                      text=day,
                                      width=40,
                                      height=40,
                                      fg_color="#EF7AFF",
                                      corner_radius=15,  # Radius for rounded corners
                                      hover_color="pink",
                                      command=partial(self.this_date, day_int))
                    if self.year == self.today.year and self.month == self.today.month and day_int == self.today.day:
                        label.configure(fg_color="#FCE6FF", corner_radius=15, text_color="black")
                else:
                    label = CTkLabel(self.calendar_frame, text=day, width=40, height=40)
                label.grid(row=row + 1, column=col, padx=5, pady=5)

    def this_date(self, day):
        selected_date = jdatetime.date(self.year, self.month, day)
        day_of_week = days_of_week[selected_date.weekday()]
        x = {"day": day, "month": self.month, "year": self.year, "week": day_of_week}
        print(x)
        self.callback(x)

    def previous_month(self):
        if self.month == 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1
        self.update_calendar()

    def next_month(self):
        if self.month == 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1
        self.update_calendar()


persian_months = {
    1: "فروردین",
    2: "اردیبهشت",
    3: "خرداد",
    4: "تیر",
    5: "مرداد",
    6: "شهریور",
    7: "مهر",
    8: "آبان",
    9: "آذر",
    10: "دی",
    11: "بهمن",
    12: "اسفند"
}

days_of_week = ["شنبه", "یکشنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنج شنبه", "جمعه"]
