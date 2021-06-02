# Conway's Game of Life
First Partial Project for Simulation & Visualization Class  
_María Fernanda Gallo Cruz_
## 1) How to run it?
>> python conway.py "path_to_config_file"

## 2) Config file format
-> each number is separated by a blank space
    height width  
    x1   y1  
    x2   y2  
    .    .  
    .    .  
    .    .  
    x_n  y_n  
    
## 3) Output file :file_cabinet:
The execution of this program will write out a file called 'report.log' with the count of each shape within the game at every frame.
Each fram will output something like this:  
INFO:root:  Frame 2  
INFO:root:	Glider: 0  
INFO:root:	Block: 1  
INFO:root:	Behive: 0  
INFO:root:	Loaf: 0  
INFO:root:	Boat: 0  
INFO:root:	Tub: 0  
INFO:root:	Blinker: 1  
INFO:root:	Toad: 0  
INFO:root:	Spaceship: 1  
INFO:root:	Beacon: 1  
INFO:root:	Others: 0  
