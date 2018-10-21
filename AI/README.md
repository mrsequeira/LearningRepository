## Baby steps on Matlab
* MATLAB is case-sensitive.
* Comments using %

### Basics:
```matlab
%Semicolon indicates end of statement
x = 3;
y = x + 5

clc % clear commands
clear % clear workspace
F1 % Help documentation

array = [7 8 9 3 5]
matrix= [1 2 3; 4 5 6; 7 8 9] % 3x3
```
### Creating plots:
* plot -> 2D 
* plot3 -> 3D

```matlab
x = [0:5:100]; %range of values for x from 0 to 100, with an increment of 5. (this increment is important if we want a smoother graph)
y = sin(x);
plot(x, y), xlabel('x'), ylabel('Sin(x)'), title('Sin(x) Graph'), grid on, axis equal

m = [1 2 3; 4 5 6; 7 8 9] 
max(m) or min(m)
size(m)
Squareroot: 2 ^(1/2)
mean(B) %media
median(B) %mediana

m(3, :) % Go through last row
plot(m(:,1),m(:,2)) %X over 

xlsread('filename', 'A1:A1') 
```




### Refs:
https://www.tutorialspoint.com/matlab/matlab_quick_guide.htm    
