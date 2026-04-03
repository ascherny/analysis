TRUE = lambda x: lambda y: x # Принимает x, возвращает функцию, принимающую y c аргументом x
FALSE = lambda x: lambda y: y # Принимает x, возвращает функцию, принимающую y c аргументом y


AND = lambda p: lambda q: p(q)(p) # Принимает p, возвращает функцию, принимающую q c аргументом p от q, которая принимает p (p(q))(p) // AND(T)(F) -> AND(T(F)(T)) -> T(F)(T) - F
OR = lambda p: lambda q: p(p)(q) # Принимает p, возвращает функцию, принимающую q c аргументом p от p, которая принимает p (p(p))(q)
NOT = lambda p: p(FALSE)(TRUE) # NOT(TRUE) -> TRUE(FALSE)(TRUE) -> FALSE // NOT(FALSE) -> FALSE(FALSE)(TRUE) -> TRUE


print(TRUE("да")("нет"))        # → "да"
print(FALSE("да")("нет"))       # → "нет"
print(AND(TRUE)(TRUE)("T")("F")) # → "T"
print(AND(TRUE)(FALSE)("T")("F")) # → "F"
print(NOT(TRUE)("T")("F"))      # → "F"
print(TRUE(FALSE("нет")("да"))("нет"))        # → "нет"

PAIR = lambda h:lambda i:lambda j:j(h)(i)



