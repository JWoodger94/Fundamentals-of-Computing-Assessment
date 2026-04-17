#Bro Code (2020) Python Tkinter Full Course for free [Video] https://www.youtube.com/watch?v=TuLxsvK4svQ
#NeuralNine (2021) Tkinter Beginner Course - Python GUI Development [video]. https://www.youtube.com/watch?v=ibf5cx221hk
#Python Tutorial (2021) Tkinter Grid. 
#Geeksforgeeks (2025) How To Align Text In Tkinter Label? https://www.geeksforgeeks.org/python/how-to-align-text-in-tkinter-label/. 
#Geeksforgeeks (2026) Enumerate() in Python. https://www.geeksforgeeks.org/python/enumerate-in-python/
#Stackoverflow (2012) tkinter creating buttons in for loop passing command arguments. https://stackoverflow.com/questions/10865116/tkinter-creating-buttons-in-for-loop-passing-command-arguments
#iditect (n.d.) Tkinter creating buttons in for loop passing command arguments. https://www.iditect.com/faq/python/tkinter-creating-buttons-in-for-loop-passing-command-arguments.html
#geeksforgeeks (2025) Using lambda in GUI programs in Python. https://www.geeksforgeeks.org/python/using-lambda-in-gui-programs-in-python/
#CodeRivers (n.d.) Mastering f-string Formatting in Python. https://coderivers.org/blog/f-string-format-python/
#Stackoverflow (2012) How do I use Tkinter to create line-wrapped text that fills the width of the window? https://stackoverflow.com/questions/11949391/how-do-i-use-tkinter-to-create-line-wrapped-text-that-fills-the-width-of-the-win
#Hu, J. (2025) How to Change the Tkinter Button Size. https://www.delftstack.com/howto/python-tkinter/how-to-change-the-tkinter-button-size/. 

import tkinter as tk

#Main window
root = tk.Tk()
root.geometry("800x1000")
root.title("The Solar System")

label = tk.Label(root, text="Learn about the Solar System", font=("Arial", 24))
label.pack(padx=20, pady=20)

#Planet class to store planet facts
class Planet:
    def __init__(self, name, mass, distance_from_sun, moons=0, moon_names=None):
        self.name = name
        self.mass = mass
        self.distance_from_sun = distance_from_sun
        self.moons = moons
        self.moon_names = moon_names or []

    def __repr__(self):
        if self.moons == 0:
            return f"""{self.name}: 
            Mass = {self.mass} Earths 
            Average Distance from Sun = {self.distance_from_sun} million km 
            Moons = {self.moons}"""
        elif self.name == "Earth":
            return f"""{self.name}: 
            Mass = 5.97217±0.00028x1027 kg 
            Average Distance from Sun = {self.distance_from_sun} million km 
            Moons = {self.moons} 
            Largest Moon = {', '.join(self.moon_names)}"""
        else:
            return f"""{self.name}: 
            Mass = {self.mass} Earths 
            Average Distance from Sun = {self.distance_from_sun} million km
            Moons = {self.moons} 
            Largest Moons = {', '.join(self.moon_names)}"""

#GUI class which creates the planet buttons and opens a new window with planet facts when a button is selected.
class Planet_GUI:
    def __init__(self):
        self.label1 = tk.Label(root, text="The Planets", font=("Arial", 20))
        self.label1.pack(padx=20, pady=20)

        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=10)

        # Create planets
        self.planets = [
            Planet("Mercury", 0.05, 57.9, 0),
            Planet("Venus", 0.82, 108.2, 0),
            Planet("Earth", 1.0, 149.6, 1, ["Moon"]),
            Planet("Mars", 0.11, 227.9, 2, ["Phobos", "Deimos"]),
            Planet("Jupiter", 317.8, 778.5, 115, ["Ganymede", "Callisto", "Io", "Europa"]),
            Planet("Saturn", 95.2, 1434, 292, ["Mimas", "Enceladus", "Tethys", "Dione", "Rhea", "Titan", "Hyperion"]),
            Planet("Uranus", 14.5, 2871, 29, ["Miranda", "Ariel", "Umbriel", "Titania", "Oberon"]),
            Planet("Neptune", 17.1, 4504, 16, ["Triton", "Nereid", "Proteus"]),
        ]

        # Create buttons 
        for i, planet in enumerate(self.planets):
            btn = tk.Button(self.frame, text=planet.name,font=("Arial", 18), width=20, command=lambda p=planet: self.open_planet_window(p))
            btn.grid(row=i, column=0, sticky=tk.W+tk.E, pady=5)

    # Opens new window with planet facts
    def open_planet_window(self, planet):
        new_window = tk.Toplevel(root)
        new_window.geometry("600x200")
        new_window.title(planet.name)

        label = tk.Label(
            new_window,
            text=repr(planet),
            font=("Arial", 14),
            wraplength=550, justify=tk.LEFT
        )
        label.pack(padx=20, pady=20)

#Creates the FAQ GUI which contains a list of 'FAQs' about the solar system. When a question is selected and the submission button is pressed, a new window will appear with the relevant information.
class faq_GUI:

    def __init__(self):
        self.label2 = tk.Label(root, text="FAQs", font=("Arial", 20))
        self.label2.pack(padx=20, pady=20)
        self.listbox = tk.Listbox(root, font=("Arial", 12), width=80)
        self.listbox.pack()

        self.listbox.insert(1, "Tell me everything about Saturn")
        self.listbox.insert(2, "How massive is Neptune?")
        self.listbox.insert(3, "Is Pluto a planet?")
        self.listbox.insert(4, "What is the largest moon in the solar system?")
        self.listbox.config(height=self.listbox.size())

        self.submitButton = tk.Button(root, text="Submit", font=("Arial", 14), command=self.submit)
        self.submitButton.pack(pady=20)

    #FAQ facts function
    def faq_facts(self):
        if self.listbox.get(self.listbox.curselection()) == "Tell me everything about Saturn":
            return f"""Saturn is the sixth planet from the Sun and the second largest in the Solar System, after Jupiter. It is a gas giant primarily consisting of hydrogen and helium. A distinctive feature of Saturn is its array of rings, which are thought to be fragments of comets, asteroids and moons orbiting the planet.
            
            Saturn formed around 4.5 billion years ago and is as old as the solar system itself. It has a dense, metallic core of iron and nickel surrounded by rock and enveloped in liquid metallic hydrogen – much like Jupiter. Interestingly, the average density of Saturn is lighter than water; indeed, if we imagined a ginormous bathtub, Saturn would float in it!
            
            Saturn has the second shortest day in the solar system at 10.7hrs, however, a Saturnian year is equivalent to 29.4 Earth years. Like Earth, however, it experiences seasons due to its axial tilt. Saturn is unlikely to harbour life; its environment is too harsh and extreme for organisms to adapt to it. This however doesn’t necessarily extend to its moons; indeed, Enceladus and Titan are home to internal oceans, and it is posited that these may support life. """
        elif self.listbox.get(self.listbox.curselection()) == "How massive is Neptune?":
            return "Neptune is a massive ice giant with a mass of approximately 1.024 × 10²⁶ kg, which is about 17.15 times the mass of Earth. It is the third-most-massive planet in our solar system, trailing only Jupiter and Saturn, and is the densest of the giant planets."
        elif self.listbox.get(self.listbox.curselection()) == "Is Pluto a planet?":
            return "At the time of its discovery in 1930, Pluto was touted as the ninth planet. However, it is much less massive than the terrestrial planets, and even some of the solar system’s moons. Its planetary status was further challenged when other large objects were discovered in the Kuiper belt during the 1990s and 2000s, including the dwarf planet Eris discovered in 2005. Finally, in 2006, the International Astronomical Union (IAU) formally reclassified Pluto as a dwarf planet following its redefining of what qualities constitute a planet. "
        elif self.listbox.get(self.listbox.curselection()) == "What is the largest moon in the solar system?":
            return "The largest moon in the solar system is Ganymede, a moon of the planet Jupiter. It is the largest and most massive moon in the solar system, larger than the planet Mercury but lower in density. "

    def submit(self):
        selection = self.listbox.curselection()
        if selection:
            self.create_new_window()
            print(self.listbox.get(selection))

    #Creates the new window for FAQs
    def create_new_window(self):
        new_window = tk.Toplevel(root)
        new_window.geometry("800x600")
        new_window.title(self.listbox.get(self.listbox.curselection()))
        label = tk.Label(new_window, text=self.faq_facts(), font=("Arial", 14), wraplength=750)
        label.pack(padx=20, pady=20)   

# Execute Planet GUI    
Planet_GUI()

# Execute FAQ GUI
faq_GUI()

root.mainloop() 