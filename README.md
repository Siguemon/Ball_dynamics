This is just a simple program that simulates point-like ball dynamics within a [0, 1]^2 box. 

If contains as "ball" class that is defined by its position and velocity in 2D space.
Said class features get/set methods, two methods that calculate the acceleration from position/velocity on x/y axis using Newton's 2nd law (?!)
The acceleration calculation methods are set to zero, and commented damping possibilities for loss energy processes.

Then the class features update methods for x/y position/velocity using Euler's caracteristic methods (which has its limits but is fine as long as you're 
updating within small time frames, like 1ms). I may update it with RK methods.


The second part of the code is just a small application of the class to show dynamics in the [0,1]^2 box and animation.
Matplotlib's animation.FuncAnimation update time may not be set below 30 ms or else it'll be laggy. This is why i pick one each ten frames 
to allow calculation precision with Euler's method while still having coherent animation results.

this was fun to do
