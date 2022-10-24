import matplotlib.pyplot as plt
import numpy as np

def fungsi(x):
    return x**3 + x**2 - x*3 - 3

def kartesian():
    x = np.linspace(-3,3,100)
    y = x**3 + x**2 - x*3 - 3
    
    plt.plot(x,y)
    plt.show()

def bolzano(x1, x2):
    kartesian()

    xt = (x1 + x2) / 2
    y1 = fungsi(x1)
    y2 = fungsi(x2)
    yt = fungsi(xt)

    if (y1 * y2 >= 0):
        print("Nilai yang dimasukkan tidak sah\n")
        return

    i = 1
    while ((x2 - x1) >= 0.01 and i <= 10):
        xt = float("{:.5f}".format((x1 + x2) / 2))
        y1 = float("{:.5f}".format(fungsi(x1)))
        y2 = float("{:.5f}".format(fungsi(x2)))
        yt = float("{:.5f}".format(fungsi(xt)))
        print("i=", i, "| x1=", x1, "| x2=", x2, "| xt=", xt, "| y1=", y1, "| y2=", y2, "| yt=", yt)

        if (yt == 0.0):
            break

        if (yt * y1 < 0):
            x2 = xt
        else:
            x1 = xt

        i += 1

x1 = 1
x2 = 2
bolzano(x1, x2)