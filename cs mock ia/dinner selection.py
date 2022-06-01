from graphics import*
from Button import*


def main():

    f = open("Recepies.txt", "r")
    text = f.read( 958 - 0 )
    text2 = f.read( 1975 - 959)
    text3 = f.read( 3400 - 1976)
    text4 = f.read( 4840 - 3401)
    text5 = f.read( 6101 - 4841)
    text6 = f.read( 7332 - 6102)
    text7 = f.read( 9460 - 7333)
    
    win = GraphWin("dinner generator" , 800,600)

    dinner = Image(Point(400,300), "dinner.png")
    dinner.draw(win)

    crazyText = Text(Point(400,50), " Welcome to the dinner generator! ")
    crazyText.setSize(30)
    crazyText.setStyle("bold")
    crazyText.setFill("white")
    crazyText.draw(win)

    
    funText = Text(Point(150,400), " Products available ")
    funText.setSize(24)
    funText.setStyle("bold")
    funText.setFill("white")
    funText.draw(win)

    fun = Entry(Point(150,350),30)
    fun.draw(win)

    sadText = Text(Point(650,400), " Who is coming? ")
    sadText.setSize(24)
    sadText.setStyle("bold")
    sadText.setFill("white")
    sadText.draw(win)

    sad = Entry(Point(650,350),30)
    sad.draw(win)
    
    graph = Button(win, 'pink', "Generate the dinner", Point(250,520), 85)
    quitB = Button(win, 'purple', "Quit", Point(500,520), 85)

    while True:
        m1 = win.getMouse()
        if graph.isClicked(m1):
            d = fun.getText()
            s = sad.getText()
            
            if "Family" in s:
                if "chicken" in d:
                    win2 = GraphWin("recipies results" , 600,850)
                    recipetext = Text(Point(300,400), " ")
                    recipetext.setText(text4)
                    recipetext.draw(win2)

            if "relatives" in s:
                if "pork" in d:
                    win2 = GraphWin("recipies results" , 600,600)
                    recipetext = Text(Point(300,300), " ")
                    recipetext.setText(text6)
                    recipetext.draw(win2)


            if "school" in s:
                if "fish" in d:
                    win2 = GraphWin("recipies results" , 600,600)
                    recipetext = Text(Point(300,300), " ")
                    recipetext.setText(text2)
                    recipetext.draw(win2)

            if "neighborhood" in s:
                if "gnocchi" in d:
                    win2 = GraphWin("recipies results" , 600,600)
                    recipetext = Text(Point(300,300), " ")
                    recipetext.setText(text)
                    recipetext.draw(win2)

            if "party" in s:
                if "bacon" in d:
                    win2 = GraphWin("recipies results" , 600,600)
                    recipetext = Text(Point(300,300), " ")
                    recipetext.setText(text3)
                    recipetext.draw(win2)


            if "vegetarian" in s:
                if "cauliflower" in d:
                    win2 = GraphWin("recipies results" , 800,900)
                    recipetext = Text(Point(350,450), " ")
                    recipetext.setText(text7)
                    recipetext.draw(win2)

            if "date" in s:
                if "turkey" in d:
                    win2 = GraphWin("recipies results" , 600,600)
                    recipetext = Text(Point(300,300), " ")
                    recipetext.setText(text5)
                    recipetext.draw(win2)
                    






        if quitB.isClicked(m1):
            win.close()
            win2.close()
            break
                

    



if __name__ == "__main__":
    main()
