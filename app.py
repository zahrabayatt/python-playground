class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    # it tasks two arguments: self, key
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    # it tasks three arguments: self, key, value
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        # iter is a built in function to get an iterator from an object.
        return iter(self.tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)

cloud.add("Python")
print(cloud.tags)

# reimplement __getitem__ magic method to unable to read count of tags like this:
print(cloud["python"])

# reimplement __getitem__ magic method to unable to set count of tags like this:
cloud["python"] = 2
print(cloud.tags)

# reimplement __len__ magic method to unable to get numbers of tags like this:
print(len(cloud))

# reimplement __iter__ magic method to make it iterable, so we can iterate over it using a for loop:
for tag in cloud:
    print(tag)
