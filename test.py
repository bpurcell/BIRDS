from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
from datetime import datetime

# Load and initialize the BirdNET-Analyzer models.
analyzer = Analyzer()

recording = Recording(
    analyzer,
    "sample/American Goldfinch.mp3",
    lat=35.4244,
    lon=-120.7463,
    date=datetime.now().date(), 
    min_conf=0.25,
)
recording.analyze()
print(recording.detections)