'''FUNCTIONS
(1) Define vs Call
(2) Parametr vs Argument
(3) Keyword & default argument
(4) Scope 
'''

print("=====define vs Call=====")
# build in function > print()  type()
# Funtion - reseusable block of code!
# Instead of block{} in JAVA, Python uses indentation(:)!


# DEFINE - paramtr 
def add(a):
    print(f"whatts up {a}")


def add2(b):
    print("add2 is done")
    return f"hello {b}"


# CALL - argument
result = add("Chris")
print(result)

result2 = add2("Jake")
