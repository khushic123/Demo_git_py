# args --> variable length arguement

def func(name,branch="cce", **kwargs):
    print(name)
    for i,j in kwargs.items():
        print(i, j)
    print(branch)


func(name="khushi", cg=7.55, comp="Goldman", age=21, clg="The LNMIIT",branch="cse")
