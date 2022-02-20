# from turtle import Turtle, Screen, color

# jimmy = Turtle()
# print(jimmy)
# jimmy.shape("turtle")
# jimmy.forward(100)
# jimmy.color("coral")
# my_screen = Screen()


# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"
print(table)
