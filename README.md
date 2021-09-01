# terminal-graphics

Simple graphics in terminal.
Less then 200 lines of code (each js and python)

* No browser needed
* No graphic environment
* No dependencies 
* Runs in terminal
* Color graphics supported:
  * draw line
  * draw circle
  * fill circle
  * draw rectangle
  * fill rectangle
  * set pixel
  * get pixel
  * draw image (sprite)
  * flood fill
  * 8 colors
  * animation

Run it in terminal:
```
node demo/index.js
```
or
```
python demo.py
```

# How it works

The main idea is to use `\u2584` char (half char filled) and change front and back colors for every character. 
This results in 2 vertical pixels per character on the screen. 
