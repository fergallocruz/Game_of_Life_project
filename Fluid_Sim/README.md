### Features

- Fluid simulation usign the [com139-class](http:/https://github.com/gcastillo56/com139-class/ "com139-class") repo implementation
- Customization using an input file with setting options

# Fluid Simulation ~ Project II

##Description
This is a project for the second term of the Simulation and Visualization Course at Universidad Panamericana Campus Guadalajara for the Computer Systems career. The following is the implementation of a customization option in python to make personalized simulations.
The output after running the project is an mp4 with the result animation.
##Customization using input file
You will have a document on the main folder called custom.json (link to file) where you can place the input data to make fluid simulation videos.
###Create multiple sources for velocity and density
#####Velocity vectors
Under the Velocity tag on the customization file you will place n vectors and its value separated by space as follows:
```json
"velocity": {
        "20 40": "-2 2",
        "20 8": "179 20"
    }
```
the code above would make the grid change the vector values:
> velocity[20, 40] = [-2, 2]
velocity[20, 8] = [179 20]

#####Density vectors
Under the "density" tag on the customization file you will place n points and the value (positive or negative)  to change the density on such place. Example below:
```json
  "density": {
    "20:40 25:30": 5,
    "25 26": -10
  },
```
the code above would make the grid change the density values:
```python
# increased density value in the range 20 to 40 in x and 25 to 30 in y 
[20:40, 25:30] += 5 
# decresed density in just one point x = 25 and y = 26
density[25, 26] -= 10 
```
###Create color schemas for the simulation
Inside the "Color Scheme" tag there are following tags:
```json
  "Color Scheme":{
    "cmap": [
        "#86CDE0",
        "#5ABAD3",
        "#47B3CF",
        "#23A4C4",
        "#0B97BA",
        "#138BAE",
        "#197A9D",
        "#217091",
        "#2C5F84",
        "#314B6C"
    ],
    "Axes Color": "#000000",
    "Title Color": "#000000",
	"Title"			: "Fluid Simulation",
    "Background Color": "#FFFFFF",
    "Objects Color": "#FFFFFF",
    "Arrows Color": "#FFFFFF"
  }
```
#####cmap
Under this tag place as many colors you wish in form of a range of color. This means the values in the plot area with have its color depending on the range they fall. The first colors are related to the smallest values as the last colors correspond to those higher.

#####Axes, Labels, Title and Background Color
Place the hex color value :tw-1f3a8: for each of the labels and play with color combinations.
![alt text](https://github.com/fergallocruz/Simulation_and_Visualization_projects/blob/Game_of_life_p1/Fluid_Sim/Screenshots/Figure%202021-04-18%20133511.png?raw=true)
![alt text](https://github.com/fergallocruz/Simulation_and_Visualization_projects/blob/Game_of_life_p1/Fluid_Sim/Screenshots/Figure%202021-04-18%20215715.png?raw=true)
![alt text](https://github.com/fergallocruz/Simulation_and_Visualization_projects/blob/Game_of_life_p1/Fluid_Sim/Screenshots/Figure%202021-04-18%20215734.png?raw=true)

###Simulate the presence of objects
In order to place some solids you can do so by placing the starting point of them as the tag inside "objects" and placing an array of [width, height] as it's value.
```json
  "objects": {
      "0 50": [20, 5],
      "30 40": [20, 5],
      "10 30": [20, 5]
    }
```
