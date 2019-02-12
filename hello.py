class HelloWorld():
    def __init__(self, name):
        self.name = name
    def greeting(self):
        if self.name == None:
            return ""
        else:
            return f"Hello, {self.name}!"

if __name__ == "__main__":
    hw = HelloWorld(None)
    print (hw.greeting())