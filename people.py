class person:
    """represents a human"""
    def __init__(self, first_name, last_name, age, weight, height) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self.height = height

    def __str__(self) -> str:
        s = f"Name: {self.first_name} {self.last_name}\n"
        s += f"Age: {self.age}\nWeight: {self.weight}\nHeight: {self.height}"
        return s

    def __lt__(self, other: object) -> bool:
        if self.last_name != other.last_name:
            return self.last_name < other.last_name
        else:
            return self.first_name < other.first_name
        
    def __gt__(self, other: object) -> bool:
        if self.last_name != other.last_name:
            return self.last_name > other.last_name
        else:
            return self.first_name > other.first_name
        
p1 = person("mike","larson", 32, 156, "5\'11")
p2 = person("mike","larson", 43, 178, "6\'7")
p3 = person("susy","ghett", 22, 126, "5\'01")
p4 = person("ann","peen", 39, 189, "6\'1")

print(p1)