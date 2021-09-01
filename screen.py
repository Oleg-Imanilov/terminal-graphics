import math

def cursor(visible): 
    if (visible): return "\033[?25h"
    return "\033[?25l"
def position(x,y): return "\033[{};{}H".format(x,y)
def px2(c1, c2): return "\033[3{};4{}m\u2584".format(c1, c2)
def color(c1, c2): return "\033[3{};4{}m".format(c1, c2)

def frange(start, stop=None, step=None):
    # if set start=0.0 and step = 1.0 if not specified
    start = float(start)
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0
    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1

class Screen:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.clear()

    def clear(self):
        self.buffer = [ [ 0 for i in range(self.w) ] for j in range(self.h) ]
        self.color = 7
        self.dirty = True

    def setColor(self, col):
        self.color = col % 8

    def put(self, x, y):
        if( x < 0 or x >= self.w or y < 0 or y >= self.h ): return
        self.buffer[y][x] = self.color
        self.dirty = True

    def get(self, x, y):
        return self.buffer[y][x]

    def line(self, x0, y0, x1, y1):
        w = max(x0, x1) - min(x0, x1)
        h = max(y0, y1) - min(y0, y1)
        if (w > h):
            if w == 0: w = 0.001
            (_x, _y) = (x0, y0) if min(x0, x1) == x0 else (x1, y1)
            k = h / w if min(y0, y1) == _y else -h/w
            for x in range(int(w+1)):
                y = int(round(x * k))
                self.put(_x + x, _y + y)
        else:
            if h == 0: h = 0.001
            (_x, _y) = (x0, y0) if min(y0, y1) == y0 else (x1, y1)
            k = w / h if min(x0, x1) == _x else -w / h
            for y in range(int(h+1)):
                x = int(round(y * k))
                self.put(_x + x, _y + y)

    def rect(self, x0, y0, x1, y1, fill = False) : 
        (xmin,xmax,ymin,ymax) = (min(x0, x1), max(x0, x1), min(y0, y1), max(y0, y1))
        if (fill):
            for y in range(ymin, ymax+1):
                for  x in range(xmin, xmax+1):
                    self.put(x, y)
        else:
            self.line(xmin, ymin, xmax, ymin)
            self.line(xmin, ymin, xmin, ymax)
            self.line(xmax, ymax, xmin, ymax)
            self.line(xmax, ymax, xmax, ymin)
     

    def circle (self, x, y, r, fill = False):
        for  a in frange(0, math.pi, math.pi / 180.0):
            _x = int(round(math.cos(a) * r))
            _y = int(round(math.sin(a) * r))
            if (fill):
                self.line(x + _x, y + _y, x + _x, y - _y)
                self.line(x - _x, y + _y, x - _x, y - _y)
            else:
                self.put(x + _x, y + _y)
                self.put(x - _x, y + _y)
                self.put(x + _x, y - _y)
                self.put(x - _x, y - _y)

    def _flood(self, x, y, c):
        if (x < 0 or y < 0 or x >= self.w or y >= self.h): return
        if (self.get(x, y) == c):
            self.put(x, y)
            self._flood(x - 1, y, c)
            self._flood(x + 1, y, c)
            self._flood(x, y - 1, c)
            self._flood(x, y + 1, c)

    def fill(self, x, y):
        curr = self.get(x, y)
        if (curr == self.color): return
        self._flood(x, y, curr)
    
    def img(self, x0, y0, data):
        h = len(data)
        w = len(data[0])
        for y in range(h):
            for x in range(w):
                self.setColor(data[y][x])
                self.put(x0 + x, y0 + y)

    def draw(self):
        if not self.dirty : return
        s = position(0, 0)
        s += cursor(False)
        for y in range(0, self.h, 2):
            for x in range(self.w):
                c1 = self.buffer[y+1][x]
                c2 = self.buffer[y][x]
                s += px2(c1, c2)
            s += "\n"
        print(s)
        print(color(7,0))
        self.dirty = False
