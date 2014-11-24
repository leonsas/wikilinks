CITIES = [
('Chicago', 'chicago'),
('New_York_City', 'newyork'),
('Paris', 'paris'),
('Tokyo', 'tokyo'),
('London','london'),
]

command_str ="""
/Users/leonsas/projects/temp/capturejs/capture.js --uri http://en.wikipedia.org/wiki/%s \
            --viewportsize 9000x1400 \
            --zoomfactor 3 \
            --javascript-file /Users/leonsas/Dropbox/FALL2014/DSGN395/WikiLinks/injector.js \
            --output '%s/%s.png'

"""

for endpoint, name in CITIES:
  print command_str % (endpoint, name, name)