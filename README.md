# terminal-graphics

Simple graphics in terminal.

> 145 lines of javascript code

* No browser needed
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
  * 7 colors
  * animation

Run it in terminal:
```bash
node demo/index.js
```
or
```bash
python demo.py
```

# How it works

The main idea is to use `\u2584` char (half char filled) and change front and back colors for every character. 
This results in 2 vertical pixels per character on the screen. Pixel values stored in buffer. `screen.go` function renders everything in background.  
