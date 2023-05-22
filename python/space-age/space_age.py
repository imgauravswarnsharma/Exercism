class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth = seconds / 31557600
        
    def orbital_ratio(self, orbital_period):        
        return round(self.earth/orbital_period, 2)
    
    def on_mercury(self):
        return self.orbital_ratio(0.2408467)
    
    def on_venus(self):
        return self.orbital_ratio(0.61519726)
    
    def on_earth(self):
        return self.orbital_ratio(1)
    
    def on_mars(self):
        return self.orbital_ratio(1.8808158)
    
    def on_jupiter(self):
        return self.orbital_ratio(11.862615)
    
    def on_saturn(self):
        return self.orbital_ratio(29.447498)
    
    def on_uranus(self):
        return self.orbital_ratio(84.016846)
    
    def on_neptune(self):
        return self.orbital_ratio(164.79132)