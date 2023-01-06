# args --> variable length arguement -->in from of tuples
# kwargs --> keyworded variable length arguement --> in form of dictionary
# default arguemnt --> dont pass them just declare them in the function that if they will be passes they would be
# overrided else use what is defined in function
#positional arguements -->fixed postions of arguemnts

def func(name,branch="cce", **kwargs):
    print(name)
    for i,j in kwargs.items():
        print(i, j)
    print(branch)


func(name="khushi", cg=7.55, comp="Goldman", age=21, clg="The LNMIIT",branch="cse")
