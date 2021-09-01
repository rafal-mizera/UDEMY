class NoDuplicates:
    def __init__(self):
        self.list = []

    def __call__(self,new_items):
        for a in new_items:
            if not a in self.list:
                self.list.append(a)


new_item = NoDuplicates()
new_item(["chair","table","mirror"])
new_item(["chair","table","mirror","bed"])
print(new_item.list)