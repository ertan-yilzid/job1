n = int(input("taille: "))
height = n
width = n
a = "+"
h = "|"
w = "-"
s = " "
e = "#"
i = 1
def draw_ext(width, height):
    print(a + w * width + a)
    for i in range(height):
        print(h + (e * (width-(i+1))) + s + (e * (width+(i-width))) + h)
    print(a + w * width + a)

draw_ext(width, height)
