# we can also inherits from built in class like str and extend it:
class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.lower())  # we has access to built in str methods
print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
print(list.append("1"))
