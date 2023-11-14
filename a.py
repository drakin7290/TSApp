# f = open("demofile.txt", "r")
# for x in f:
#   print(x, end='')

arr = [{"abc": "gh"}, {"abc": "gh"}]

f = open("demofile2.txt", "w")
abc = [str(_) for _ in arr]
f.write("\n".join(abc))
f.close()