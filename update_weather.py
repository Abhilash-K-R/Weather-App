import tkinter as tk
from tkinter import ttk

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")

        # Create main frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=20, pady=20)

        # Weather information labels
        ttk.Label(self.main_frame, text="Current Weather", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(self.main_frame, text="Location:").grid(row=1, column=0, sticky="E", padx=5)
        self.location_label = ttk.Label(self.main_frame, text="", font=("Helvetica", 12))
        self.location_label.grid(row=1, column=1, sticky="W", padx=5)
        
        ttk.Label(self.main_frame, text="Temperature:").grid(row=2, column=0, sticky="E", padx=5)
        self.temp_label = ttk.Label(self.main_frame, text="", font=("Helvetica", 12))
        self.temp_label.grid(row=2, column=1, sticky="W", padx=5)

        ttk.Label(self.main_frame, text="Humidity:").grid(row=3, column=0, sticky="E", padx=5)
        self.humidity_label = ttk.Label(self.main_frame, text="", font=("Helvetica", 12))
        self.humidity_label.grid(row=3, column=1, sticky="W", padx=5)

        ttk.Label(self.main_frame, text="Wind Speed:").grid(row=4, column=0, sticky="E", padx=5)
        self.wind_label = ttk.Label(self.main_frame, text="", font=("Helvetica", 12))
        self.wind_label.grid(row=4, column=1, sticky="W", padx=5)

        ttk.Label(self.main_frame, text="Visibility:").grid(row=5, column=0, sticky="E", padx=5)
        self.visibility_label = ttk.Label(self.main_frame, text="", font=("Helvetica", 12))
        self.visibility_label.grid(row=5, column=1, sticky="W", padx=5)

        # Update weather information button
        self.update_button = ttk.Button(self.main_frame, text="Update", command=self.update_weather)
        self.update_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Initial weather data
        self.update_weather()

    def update_weather(self):

