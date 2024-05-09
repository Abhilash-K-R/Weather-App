import tkinter as tk
from tkinter import ttk

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")

        # Create main frame

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
        # Call function to fetch current weather data
        # Update labels with fetched weather information
        # Example:
        location = "New York"
        temperature = "23°C"
        humidity = "65%"
        wind_speed = "10 km/h"
        visibility = "8 km"

        self.location_label.config(text=location)
        self.temp_label.config(text=temperature)
        self.humidity_label.config(text=humidity)
        self.wind_label.config(text=wind_speed)
        self.visibility_label.config(text=visibility)

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
