regex_pattern = r"(^(?=[MDCLXVI])M{,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$)"	# Do not delete 'r'.
#regex_pattern = r"([IXCLDM]{,3}[V]{,2})*$"
import re

N = input()
VAL = re.match(regex_pattern, N)
print(str(bool(VAL)))
# print(True if VAL else False)
print(str(bool(re.match(regex_pattern, input()))))

