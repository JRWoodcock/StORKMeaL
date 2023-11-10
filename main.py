import simplekml

import models
import shapes


if __name__ == "__main__":

  # Radius of the circle in feet
  radius = 3000

  # Import the data from the CSV
  data = models.csv_to_dict("Long-Beach.csv")

  #Create a blank list to store the instances in
  places = []

  #Append instances to the list with data from the CSV
  for each in data:
    places.append(shapes.GeoCircle(latitude=each['Latitude'], longitude=each['Longitude'], 
                                   radius=radius, name=each['Name'], description=each['Address']))

  # Create an instance of Kml
  kml = simplekml.Kml(name="Non-Compliance", open=1)

  # Create a new document
  # doc = kml.newdocument(name="A Document")

  # Folder containing polygons with style
  fol = kml.newfolder(name="Schools", description="Known Points of Noncompliance")

  for place in places:
    pol = fol.newpolygon(name=place.name, description=place.description, 
                        outerboundaryis=place.plots)
    pol.style.linestyle.color = 'ff000099'
    pol.linestyle.width = 2
    pol.style.polystyle.color = 'AA000099' #This Red gives a transparent effect

  # Save the file
  kml.save("Long_Beach.kml")