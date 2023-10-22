import math

class GeoCircle:

  def __init__(self, latitude, longitude, radius, name, description, **kwargs):
    self.latitude = float(latitude)
    self.longitude = float(longitude)
    self.radius = float(radius)
    self.plots = self.generate_plots(self.latitude, self.longitude, self.radius)
    self.name = ""
    if name:
      self.name = name
    self.description = ""
    if description:
      self.description = description

  def generate_plots(self, latitude, longitude, radius):
    '''(float, float, number) -> list
    
      Creates plts list of 360 points around longitude and latitude radius_feet in radius.
    
      Precondition: radius is the radius of the plot circle in feet.
      >>>generate_plots(33.54505548413079, -89.27338097601184, 3000)
    
      '''
    plts = []
    for angle in range(0, 360, 1):  # Create points for the circle
      x = radius * math.cos(math.radians(angle))
      y = radius * math.sin(math.radians(angle))
      plts += [(longitude + x / 364573, latitude + y / 364573)
               ]  # Convert feet to degrees
    return (plts)
