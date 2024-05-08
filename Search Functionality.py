import tkinter as tk
from tkinter import ttk
import requests

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")

        # Create main frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=20, pady=20)

        # Search frame
        self.search_frame = ttk.Frame(self.main_frame)
        self.search_frame.grid(row=0, column=0, columnspan=2)

        # Search entry and button
        self.search_entry = ttk.Entry(self.search_frame, width=30)
        self.search_entry.grid(row=0, column=0, padx=5, pady=5)
        self.search_button = ttk.Button(self.search_frame, text="Search", command=self.update_weather)
        self.search_button.grid(row=0, column=1, padx=5, pady=5)

        # Forecast frame
        self.forecast_frame = ttk.Frame(self.main_frame)
        self.forecast_frame.grid(row=1, column=0, columnspan=2)

        # Forecast data
        self.forecast_data = []

        # Initial weather data
        self.update_weather()

    def update_weather(self):
        try:
            # Get search query
            search_query = self.search_entry.get()

            # Call OpenWeatherMap API to fetch forecast weather data
            api_key = "YOUR_OPENWEATHERMAP_API_KEY"
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={search_query}&appid={api_key}&units=metric"
            
            # Fetch forecast weather data
            response = requests.get(url)
            forecast_data = response.json()

            # Parse forecast weather data
            self.forecast_data = []
            for forecast in forecast_data["list"]:
                forecast_date = forecast["dt_txt"]
                forecast_temp = f"{forecast['main']['temp']}°C"
                forecast_min_temp = f"{forecast['main']['temp_min']}°C"
                forecast_max_temp = f"{forecast['main']['temp_max']}°C"
                forecast_weather = forecast["weather"][0]["description"]

                self.forecast_data.append((forecast_date, forecast_temp, forecast_min_temp, forecast_max_temp, forecast_weather))

            # Update forecast labels
            self.update_forecast_labels()

        except Exception as e:
            # Handle any errors that occur during API request or data parsing
            print("Error fetching weather data:", e)

    def update_forecast_labels(self):
        # Clear existing forecast labels
        for label in self.forecast_frame.grid_slaves():
            label.grid_forget()

        # Add forecast labels
        for i, (date, temp, min_temp, max_temp, weather) in enumerate(self.forecast_data[:4]):
            ttk.Label(self.forecast_frame, text=date, font=("Helvetica", 12)).grid(row=i+1, column=0, padx=5, pady=5)
            ttk.Label(self.forecast_frame, text=temp, font=("Helvetica", 12)).grid(row=i+1, column=1, padx=5, pady=5)
            ttk.Label(self.forecast_frame, text=f"Min: {min_temp}, Max: {max_temp}", font=("Helvetica", 12)).grid(row=i+1, column=2, padx=5, pady=5)
            ttk.Label(self.forecast_frame, text=weather, font=("Helvetica", 12)).grid(row=i+1, column=3, padx=5, pady=5)

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
