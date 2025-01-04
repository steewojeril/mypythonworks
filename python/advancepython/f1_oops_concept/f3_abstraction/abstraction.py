'''
ABSTRACTION: showing only necessary details and hiding unnecessary deatails

Abstraction allows you to define common features or methods that must be implemented by every subclass, 
while the subclasses provide their own specific implementations of these features.

It specifies what needs to be done, but not how it is done.'''
from abc import ABC, abstractmethod

# Let's say every app must have these features.
class AppFeatures(ABC):
    @abstractmethod
    def brightness(self):  #(only declaration)
        pass  # Abstract method for brightness feature

    @abstractmethod
    def notification(self):
        pass  # Abstract method for notification feature

'''
Now, for each specific app, you create a subclass (e.g., MusicApp, WeatherApp) 
that inherits from AppFeatures. Each subclass must provide its own implementation 
for all methods defined in the abstract class, else there will be an error.
'''

class MusicApp(AppFeatures):
    def brightness(self):
        print("Adjusting brightness for Music App...")

    def notification(self):
        print("Displaying notification for Music App...")

class WeatherApp(AppFeatures):
    def brightness(self):
        print("Adjusting brightness for Weather App...")

    def notification(self):
        print("Displaying notification for Weather App...")

# Example of usage:
music_app = MusicApp()
music_app.brightness()  # Output: Adjusting brightness for Music App...
music_app.notification()  # Output: Displaying notification for Music App...

weather_app = WeatherApp()
weather_app.brightness()  # Output: Adjusting brightness for Weather App...
weather_app.notification()  # Output: Displaying notification for Weather App...
