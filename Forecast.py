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

        # Current weather frame
        self.current_weather_frame = ttk.Frame(self.main_frame)
        self.current_weather_frame.grid(row=0, column=0, columnspan=2, pady=10)

        # Forecast frame
        self.forecast_frame = ttk.Frame(self.main_frame)
        self.forecast_frame.grid(row=1, column=0, columnspan=2)

        # Current weather labels
        ttk.Label(self.current_weather_frame, text="Current Weather", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(self.current_weather_frame, text="Location:").grid(row=1, column=0, sticky="E", padx=5)
        self.location_label = ttk.Label(self.current_weather_frame, text="", font=("Helvetica", 12))
        self.location_label.grid(row=1, column=1, sticky="W", padx=5)
        
        ttk.Label(self.current_weather_frame, text="Temperature:").grid(row=2, column=0, sticky="E", padx=5)
        self.temp_label = ttk.Label(self.current_weather_frame, text="", font=("Helvetica", 12))
        self.temp_label.grid(row=2, column=1, sticky="W", padx=5)

        ttk.Label(self.current_weather_frame, text="Humidity:").grid(row=3, column=0, sticky="E", padx=5)
        self.humidity_label = ttk.Label(self.current_weather_frame, text="", font=("Helvetica", 12))
        self.humidity_label.grid(row=3, column=1, sticky="W", padx=5)

        ttk.Label(self.current_weather_frame, text="Wind Speed:").grid(row=4, column=0, sticky="E", padx=5)
        self.wind_label = ttk.Label(self.current_weather_frame, text="", font=("Helvetica", 12))
        self.wind_label.grid(row=4, column=1, sticky="W", padx=5)

        ttk.Label(self.current_weather_frame, text="Visibility:").grid(row=5, column=0, sticky="E", padx=5)
        self.visibility_label = ttk.Label(self.current_weather_frame, text="", font=("Helvetica", 12))
        self.visibility_label.grid(row=5, column=1, sticky="W", padx=5)

        # Update weather information button
        self.update_button = ttk.Button(self.current_weather_frame, text="Update", command=self.update_weather)
        self.update_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Forecast labels
        ttk.Label(self.forecast_frame, text="Weather Forecast", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=4, pady=10)

        # Forecast data
        self.forecast_data = []

        # Initial weather data
        self.update_weather()

    def update_weather(self):
        try:
            # Call OpenWeatherMap API to fetch current weather data
            api_key = "YOUR_OPENWEATHERMAP_API_KEY"
            city = "New York"  # Example city
            current_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
            
            # Fetch current weather data
            current_response = requests.get(current_url)
            current_data = current_response.json()

            # Fetch forecast weather data
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json()

            # Parse current weather data
            location = current_data["name"]
            temperature = f"{current_data['main']['temp']}°C"
            humidity = f"{current_data['main']['humidity']}%"
            wind_speed = f"{current_data['wind']['speed']} m/s"
            visibility = f"{current_data['visibility'] / 1000} km"

            # Update labels with current weather information
            self.location_label.config(text=location)
            self.temp_label.config(text=temperature)
            self.humidity_label.config(text=humidity)
            self.wind_label.config(text=wind_speed)
            self.visibility_label.config(text=visibility)

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
