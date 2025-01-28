from fake_math import divide as fake_divid
from true_math import divid as true_divid

result1 = fake_divid(69, 3)
result2 = fake_divid(3, 0)
result3 = true_divid(49, 7)
result4 = true_divid(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)