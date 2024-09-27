from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(control):
    control.draw()


def anotherDraw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
print(isinstance(ddl, UIControl))
draw(ddl)

textbox = TextBox()
print(isinstance(textbox, UIControl))
draw(textbox)

anotherDraw([ddl, textbox])

# Polymorphism is allowing objects of different types to be treated as instances of the same class. The word comes from the Greek roots "poly" (many) and "morph" (form), meaning "many forms."

# In the example you've provided, polymorphism is illustrated by the draw method, which can be invoked on different objects such as a text box, drop-down list, or radio button. The specific version of the draw method that gets executed depends on the object's actual type at runtime. This is known as runtime polymorphism, or late binding.
