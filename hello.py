class Hello:
    """class just does hello"""

    def __init__(self, name, age, favLang):
        self.Name = name
        self.Age = age
        self.FavLang = favLang

    def SayHello(self):
        print(f'Hello {self.Name}')
        return self.Name
    
    def ReturnList(self):
        for lang in self.FavLang:
            if lang.lower() == 'golang':
                return "golang"
            
        return "python"
    
    def ReturnDict(self):
        return {"name" : self.Name, "Age" : self.Age}