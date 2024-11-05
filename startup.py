fname = "D:\\hello.txt"
data = "Script working!"

with open(fname, "r") as fobj:
    content = fobj.read()


if data not in content:
    with open(fname, "a") as fobj:
        fobj.write(data + "\n")  

