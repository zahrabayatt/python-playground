class TagCloud:
    def __init__(self):
        # to make a attribute private, prefix the name of it with double underline

        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
# print(cloud.__tags)

# technically, we can still access to these member but it is hard and it is only a convensiotn to warn to don't use this member and it does not hide this member.
# how to access them?
# every class, or object has this property called __dict__, this is a dictionary that holds all attributes of class, and with this we can access them:
print(cloud.__dict__)
# output: {'_TagCloud__tags': {'python': 2}

# python interpreter in runtime rename the name of __tags to _TagCloud__tags:
print(cloud._TagCloud__tags)
