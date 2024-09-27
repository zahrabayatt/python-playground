from abc import ABC, abstractmethod


# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass

# Because python is a dynamic, without the abstract class the polymorphism is still walking, and this is called duck typing (if it walks like a duck and talks like a duck it is a duck), but good practice is to use abstract class:

class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()

draw([ddl, textbox])
