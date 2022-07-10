# child nu :
# parent nte properties venam + child nte properties venam
class Ide:
    def functionalities(self):
        funcs=["create file","rename","delete"]
        return funcs
class Pycharm(Ide):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("execute")
        funcs.append("debug")
        return funcs

py=Pycharm()
print(py.functionalities())

