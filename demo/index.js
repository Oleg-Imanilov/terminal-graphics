const { Screen } = require('../screen')

const flag1 = require('./flag1.json')
const flag2 = require('./flag2.json')

const scr = new Screen(80, 50)
scr.go()

let dx = (Math.random() * 2 + 1) - 1.5
let dy = (Math.random() * 2 + 1) - 1.5
let x = 20
let y = 20

let ang = 0
let dAng = Math.PI / 45

setInterval(() => {
    x += dx
    y += dy

    if (x < 5 || x > 60) {
        dx = -dx
    }
    if (y < 5 || y > 40) {
        dy = -dy
    }

    const xx = Math.cos(ang) * 60
    const yy = Math.sin(ang) * 60
    ang += dAng

    scr.clear()

    scr.img(5, 5, flag2)

    scr.setColor(5)
    scr.line(Math.round(40 + xx), Math.round(25 + yy), Math.round(40 - xx), Math.round(25 - yy))
    scr.line(Math.round(40 - xx), Math.round(25 + yy), Math.round(40 + xx), Math.round(25 - yy))

    scr.setColor(2)
    scr.circle(40, 25, 5, true)

    scr.setColor(5)
    scr.circle(40, 25, 5)
    scr.circle(40, 25, 2, true)

    scr.img(Math.round(x), Math.round(y), flag1)
}, 20)
