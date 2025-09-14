# pip install mypy
def myfunction(myparameter: int) -> str:
    return f"{myparameter + 10}"
def otherfunction(otherparameter:str) -> str:
    print(otherparameter)

otherfunction(myfunction(10))



def dosth(param: list[int]):
    pass