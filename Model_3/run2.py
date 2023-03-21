"""
Alex Krysztofiak, Tien Dam, Jason Rosales
"""
from model_viz import server
from Timer import Timer
t= Timer()
a = t.start()
try:
 server.launch()
except KeyboardInterrupt:
 t.stop()