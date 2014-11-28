CITIES = [
('Chicago', 'chicago'),
('New_York_City', 'newyork'),
('Paris', 'paris'),
('Tokyo', 'tokyo'),
('London','london'),
]

command_str ="""
~/Documents/Northwestern/Clases/Senior/Fall/DSGN\ 395/capturejs/capture.js --uri http://en.wikipedia.org/wiki/%s \
            --viewportsize 9000x1000 \
            --zoomfactor 3 \
            --javascript-file ~/Documents/Northwestern/Clases/Senior/Fall/DSGN\ 395/wikiLinks/'injector%s.js' \
            --output ~/Dropbox/DSGN395/prints/'%s_%s.png'
"""


for endpoint, name in CITIES:
	for injector in ['1','2']:
	  print command_str % (endpoint, injector, name, injector)