import tkinter as tk
from tkinter import ttk
import requests

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")

        # Default preferences
        self.units = tk.StringVar(value="metric")  # Default to metric (Celsius)
        self.theme = tk.StringVar(value="light")  # Default to light theme

        # Create main frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=20, pady=20)

        # Preferences frame
        self.preferences_frame = ttk.Frame(self.main_frame)
        self.preferences_frame.grid(row=0, column=0, columnspan=2)

        # Units label and radio buttons
        ttk.Label(self.preferences_frame, text="Units:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Radiobutton(self.preferences_frame, text="Celsius", variable=self.units, value="metric", command=self.update_weather).grid(row=0, column=1, padx=5, pady=5)
        ttk.Radiobutton(self.preferences_frame, text="Fahrenheit", variable=self.units, value="imperial", command=self.update_weather).grid(row=0, column=2, padx=5, pady=5)

        # Theme label and radio buttons
        ttk.Label(self.preferences_frame, text="Theme:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Radiobutton(self.preferences_frame, text="Light", variable=self.theme, value="light", command=self.set_theme).grid(row=1, column=1, padx=5, pady=5)
        ttk.Radiobutton(self.preferences_frame, text="Dark", variable=self.theme, value="dark", command=self.set_theme).grid(row=1, column=2, padx=5, pady=5)

        # Weather alerts frame
        self.alerts_frame = ttk.Frame(self.main_frame)
        self.alerts_frame.grid(row=1, column=0, columnspan=2)

        # Forecast frame
        self.forecast_frame = ttk.Frame(self.main_frame)
        self.forecast_frame.grid(row=2, column=0, columnspan=2)

        # Alert data
        self.alert_data = []

        # Forecast data
        self.forecast_data = []

        # Initial weather data
        self.update_weather()

    def update_weather(self):
        try:
            # Get search query
            search_query = "New York"  # Default city

            # Call OpenWeatherMap API to fetch forecast weather data
            api_key = "YOUR_OPENWEATHERMAP_API_KEY"
            units = self.units.get()
            forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={search_query}&appid={api_key}&units={units}"
            alert_url = f"http://api.openweathermap.org/data/3.0/alerts?q={search_query}&appid={api_key}"
            
            # Fetch forecast weather data
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json()

            # Fetch weather alerts
            alert_response = requests.get(alert_url)
            alert_data = alert_response.json()

            # Parse forecast weather data
            self.forecast_data = []
            for forecast in forecast_data["list"]:
                forecast_date = forecast["dt_txt"]
                forecast_temp = f"{forecast['main']['temp']}°C"
                forecast_min_temp = f"{forecast['main']['temp_min']}°C"
                forecast_max_temp = f"{forecast['main']['temp_max']}°C"
                forecast_weather = forecast["weather"][0]["description"]

                self.forecast_data.append((forecast_date, forecast_temp, forecast_min_temp, forecast_max_temp, forecast_weather))

            # Parse weather alerts
            self.alert_data = []
            for alert in alert_data["alerts"]:
                event = alert["event"]
                description = alert["description"]
                start_time = alert["start"]
                end_time = alert["end"]
                self.alert_data.append((event, description, start_time, end_time))

            # Update alert labels
            self.update_alert_labels()

            # Update forecast labels
            self.update_forecast_labels()

        except Exception as e:
            # Handle any errors that occur during API request or data parsing
            print("Error fetching weather data:", e)

    def update_alert_labels(self):
        # Clear existing alert labels
        for label in self.alerts_frame.grid_slaves():
            label.grid_forget()

        # Add alert labels
        if self.alert_data:
            for i, (event, description, start_time, end_time) in enumerate(self.alert_data):
                ttk.Label(self.alerts_frame, text=event, font=("Helvetica", 12, "bold")).grid(row=i, column=0, columnspan=2, padx=5, pady=5)
                ttk.Label(self.alerts_frame, text=description, font=("Helvetica", 12)).grid(row=i+1, column=0, columnspan=2, padx=5, pady=5)
                ttk.Label(self.alerts_frame, text=f"Start Time: {start_time}", font=("Helvetica", 12)).grid(row=i+2, column=0, padx=5, pady=5)
                ttk.Label(self.alerts_frame, text=f"End Time: {end_time}", font=("Helvetica", 12)).grid(row=i+2, column=1, padx=5, pady=5)
        else:
            ttk.Label(self.alerts_frame, text="No alerts", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5)

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

    def set_theme(self):
        theme = self.theme.get()
        if theme == "dark":
            self.configure(background="black", foreground="white")
        else:
            self.configure(background="white", foreground="black")

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
