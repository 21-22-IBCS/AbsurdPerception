from graphics import*
from Button import*
from math import*

def calcy(f, num):
    if "+" in f:
        l=f.split("+")
        result = 0
        for f in l: 
            result = calcy(f, num)+ result
        return result
    elif "-" in f:
        l=f.split("-")
        result = 0
        for f in l: 
            result = calcy(f, num)- result
        return result
    elif "/" in f:
        l=f.split("/")
        result = 0
        for f in l: 
            result = calcy(f, num)/result
        return result
    elif "*" in f:
        l=f.split("*")
        result = 0
        for f in l: 
            result = calcy(f, num)*result
        return result
    elif "e^x" in f:
        return e**num
    elif "^" in f:
        l=f.split("^")
        result = 0
        for f in l: 
            result = calcy(f, num)**result
        return result

    elif "sqrt(x)" in f:
        return sqrt(num)
    elif "x^2" in f:
    #'elif' only carries if the initial "if" statement is false
    #also works if the first elif doesn't work
    #it means "else if"
        return num**2
    elif "sin(x)" in f:
        return sin(num)
    elif "cos(x)" in f:
        return cos(num)
    elif "tan(x)" in f:
        return tan(num)
    elif "tan(x)/e^x" in f:
        return tan(num)/e^num
    elif "ln(x)" in f:
        if num>0:
            return log(num)
        else:
            return 0 

    elif f == "x":
        return num
    else:
        return float(f)

def main():

    win = GraphWin("calc",800,800)
    title = Text(Point(400,50), "Welcome to the Graphing Calculator")
    title.setSize(32)
    title2 = Text(Point(400,110), "Enter a function you would like to graph")
    title2.setSize(20)
    title.draw(win)
    title2.draw(win)

    yAxis = Line(Point(150,200), Point(150,650))
    yAxis.draw(win)
    xAxis = Line(Point(150,500), Point(650,500))
    xAxis.draw(win)

    funText = Text(Point(200,650), "Y  =  ")
    funText.setSize(24)
    funText.draw(win)

    fun = Entry(Point(340,650),30)
    fun.draw(win)

    graph = Button(win, 'white', "GRAPH", Point(550,650), 75)
    quitB = Button(win, 'red', "QUIT", Point(400,720), 50)

    while True:
        m1 = win.getMouse()
        if graph.isClicked(m1):
            f = fun.getText()

            scale = 50

            points = []
            for i in range(500):
                x = i + 150
                y = 500 - scale*calcy(f,i/scale)
                points.append(Point(x,y))

            for p in points:
                p.draw(win)

        if quitB.isClicked(m1):
            win.close()
            break
                
    

if __name__ == "__main__":
    main()
