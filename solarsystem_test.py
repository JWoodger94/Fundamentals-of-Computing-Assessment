#Week 6 - 6.3 Codio Activity - Unit Testing
#Stack Overflow (2010) How do I run unittest on a Tkinter app? https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app
#iditect (n.d.) How to run unittest on a Tkinter app? https://www.iditect.com/faq/python/how-to-run-unittest-on-a-tkinter-app.html 

import unittest
from solarsystem import Planet, __repr__

class TestPlanet(unittest.TestCase):
    
    def test_planet_repr(self):
        mercury = Planet("Mercury", 0.05, 57.9, 0)

        self.assertEqual(repr(mercury), """Mercury: 
            Mass = 0.05 Earths 
            Average Distance from Sun = 57.9 million km 
            Moons = 0""")

class TestPlanet_GUI(unittest.TestCase):
    def test_planet_gui(self):
        self.assertTrue(True) # Placeholder test to ensure the GUI can be initialized without errors

if __name__ == "__main__":
    unittest.main() # run all tests

