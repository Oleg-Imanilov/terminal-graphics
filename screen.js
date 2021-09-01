const ESC = String.fromCharCode(27)

const COLOR = { black: 0, red: 1, green: 2, yellow: 3, blue: 4, magenta: 5, cyan: 6, white: 7 }

const TERM = {
    cursor: (visible) => visible ? `${ESC}[?25h` : `${ESC}[?25l`,
    position: (x, y) => `${ESC}[${y};${x}H`,
    px2: (c1, c2) => `${ESC}[3${c1};4${c2}m\u2584`,
    color: (c1, c2) => `${ESC}[3${c1};4${c2}m`
}

class Screen {
    constructor(w, h) {
        this.w = w
        this.h = h
        this.clear()
    }

    clear = () => {
        this.buffer = Array.from({ length: this.h }, () => Array(this.w).fill(0));
        this.color = 7
        this.dirty = true
    }

    setColor = (c) => {
        this.color = c % 8
    }

    set = (x, y) => {
        if (x < 0 || y < 0 || x >= this.w || y >= this.h) return
        this.buffer[y][x] = this.color
        this.dirty = true
    }

    get = (x, y) => {
        return this.buffer[y % this.h][x % this.w]
    }

    _flood(x, y, c) {
        if (x < 0 || y < 0 || x >= this.w || y >= this.h) return
        if (this.get(x, y) === c) {
            this.set(x, y)
            this._flood(x - 1, y, c)
            this._flood(x + 1, y, c)
            this._flood(x, y - 1, c)
            this._flood(x, y + 1, c)
        }
    }

    fill = (x, y) => {
        const curr = this.get(x, y)
        if (curr === this.color) return
        this._flood(x, y, curr)
    }

    circle = (x, y, r, fill = false) => {
        for (let a = 0; a < Math.PI / 2; a += Math.PI / 180) {
            const _x = Math.round(Math.cos(a) * r)
            const _y = Math.round(Math.sin(a) * r)
            if (fill) {
                this.line(x + _x, y + _y, x + _x, y - _y)
                this.line(x - _x, y + _y, x - _x, y - _y)
            } else {
                this.set(x + _x, y + _y)
                this.set(x - _x, y + _y)
                this.set(x + _x, y - _y)
                this.set(x - _x, y - _y)
            }
        }
    }

    rect = (x0, y0, x1, y1, fill = false) => {
        const xmin = Math.min(x0, x1)
        const xmax = Math.max(x0, x1)
        const ymin = Math.min(y0, y1)
        const ymax = Math.max(y0, y1)
        if (fill) {
            for (let y = ymin; y <= ymax; y++) {
                for (let x = xmin; x <= xmax; x++) {
                    this.set(x, y)
                }
            }
        } else {
            this.line(xmin, ymin, xmax, ymin)
            this.line(xmin, ymin, xmin, ymax)
            this.line(xmax, ymax, xmin, ymax)
            this.line(xmax, ymax, xmax, ymin)
        }
    }

    line = (x0, y0, x1, y1) => {
        let w = Math.max(x0, x1) - Math.min(x0, x1)
        let h = Math.max(y0, y1) - Math.min(y0, y1)
        if(w===0)w=0.001
        if(h===0)h=0.001
        if (w > h) {
            const [_x, _y] = Math.min(x0, x1) === x0 ? [x0, y0] : [x1, y1]
            const k = Math.min(y0, y1) === _y ? h / w : -h / w
            for (let x = 0; x <= w; x++) {
                let y = Math.round(x * k)
                this.set(_x + x, _y + y)
            }
        } else {
            const [_x, _y] = Math.min(y0, y1) === y0 ? [x0, y0] : [x1, y1]
            const k = Math.min(x0, x1) === _x ? w / h : -w / h
            for (let y = 0; y <= h; y++) {
                let x = Math.round(y * k)
                this.set(_x + x, _y + y)
            }
        }
    }

    img = (x0, y0, data) => {
        const h = data.length
        const w = data[0].length
        for (let y = 0; y < h; y++) {
            for (let x = 0; x < w; x++) {
                this.setColor(data[y][x])
                this.set(x0 + x, y0 + y)
            }
        }
    }

    go = () => {
        if (this.dirty) {
            let s = TERM.cursor(false) + TERM.position(0, 0)
            for (let y = 0; y < this.h; y += 2) {
                for (let x = 0; x < this.w; x++) {
                    const c2 = this.buffer[y][x]
                    const c1 = this.buffer[y + 1][x]
                    s += TERM.px2(c1, c2)
                }
                s += '\n'
            }
            console.log(s)
            this.dirty = false
        }
        setTimeout(this.go, 10)
    }
}

module.exports = {
    Screen,
    COLOR
}
