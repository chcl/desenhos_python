#------------
# parametros
#------------

x, y = 243, 268

s1 = 184

s2 = s1 + 143
s2_stroke = 32

s3 = s2 + 147
s3_stroke = 32

r_steps = 9
r_stroke = 64

origin = False

#-------
# desenho
#-------

background(0)

translate(x, y)
transform(CENTER)

# oval 3
nofill()
stroke(10)
strokewidth(s3_stroke)
oval(-s3/2, -s3/2, s3, s3)
# raios
stroke(.0)
strokewidth(r_stroke)
transform(CORNER)
push()
for i in range(r_steps):
    rotate(360.0/r_steps)
    line(0, 0, 0, HEIGHT)
pop()

# oval 1
nostroke()
fill(1)
oval(-s1/2, -s1/2, s1, s1)

# oval 2
nofill()
stroke(1)
strokewidth(s2_stroke)
oval(-s2/2, -s2/2, s2, s2)

# origin
if origin:
    reset()
    stroke(1, 0, 0)
    strokewidth(1)
    line(x+.5, 0, x+.5, HEIGHT)
    line(0, y+.5, WIDTH, y+.5)
