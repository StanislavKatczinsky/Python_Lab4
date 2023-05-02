class Poly:
    def __init__(self, coef_dict):
        self.coef_dict = coef_dict
    
    def __repr__(self):
        terms = []
        for exp, coef in sorted(self.coef_dict.items(), reverse=True):
            if coef == 0:
                continue
            if exp == 0:
                term = str(coef)
            elif exp == 1:
                if coef == 1:
                    term = 'x'
                elif coef == -1:
                    term = '-x'
                else:
                    term = f'{coef}x'
            else:
                if coef == 1:
                    term = f'x^{exp}'
                elif coef == -1:
                    term = f'-x^{exp}'
                elif coef < 0:
                    term = f'-{-coef}x^{exp}'
                else:
                    term = f'{coef}x^{exp}'
            terms.append(term)
        if not terms:
            return '0'
        return ' + '.join(terms).replace(' + -', ' - ')
    
    def __neg__(self):
        return Poly({exp: -coef for exp, coef in self.coef_dict.items()})
    
    def __add__(self, other):
        result = dict(self.coef_dict)
        for exp, coef in other.coef_dict.items():
            result[exp] = result.get(exp, 0) + coef
            if result[exp] == 0:
                del result[exp]
        return Poly(result)
    
    def __sub__(self, other):
        return self + (-other)
    
    def __mul__(self, other):
        result = {}
        for exp1, coef1 in self.coef_dict.items():
            for exp2, coef2 in other.coef_dict.items():
                exp = exp1 + exp2
                coef = coef1 * coef2
                result[exp] = result.get(exp, 0) + coef
                if result[exp] == 0:
                    del result[exp]
        return Poly(result)
    
    def __rmul__(self, other):
        return Poly({exp: coef * other for exp, coef in self.coef_dict.items()})
    
    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError('Division is only supported for scalar values')
        return Poly({exp: coef / other for exp, coef in self.coef_dict.items()})
    
    def eval(self, x):
        result = 0
        for exp, coef in self.coef_dict.items():
            result += coef * (x ** exp)
        return result
    
    def sub(self, other):
        result = Poly({})
        for exp, coef in self.coef_dict.items():
            result += Poly({0: coef}) * (other ** exp)
        return result
    
    def diff(self, n=1):
        if n <= 0:
            return self
        result = {}
        for exp, coef in self.coef_dict.items():
            if exp == 0:
                continue
            result[exp-1] = exp * coef
        return Poly(result).diff(n-1)
    
    def integrate(self, n=1, a=0, b=1):
        if n <= 0:
            return Poly({0: (b-a) * sum(coef for exp, coef in self.coef_dict.items() if exp == 0)})
        result = {}
        for exp, coef in self.coef_dict.items():
            result[exp+1] = exp * coef
            return Poly(result).integrate(n-1)





# Полиномы
p = Poly({0: 1, 2: -2, 3: 3})     # p(x) = 3x^3 - 2x^2 + 1
q = Poly({1: 2, 2: 4, 4: -1})     # q(x) = - x^4 + 2x + 4x^2
r = Poly({0: -1, 1: 1})           # r(x) = -1 + x

# Операции
s = -p                           # s(x) = -p(x) = -1 + 2x^2 - 3x^3
x = p + q                        # t(x) = p(x) + q(x) = 2x + 2x^2 + 3x^3 - x^4 + 1
y = p - q                        # u(x) = p(x) - q(x) = x^4 + 3x^3 - 6x^2 - 2x + 1
v = p * r                        # v(x) = p(x) * r(x) = 3x^4 - 5x^3 + 2x^2 + x - 1
w = p.eval(2)                    # w = p(2) = 17
z = p / r
# Прочие операции
#a = p.sub(q)                    
#b = p.diff()                     
#c = p.integrate()                

# Вывод результата
print(p)
print(q)
print(s)
print(x)
print(y)
print(v)
print(w)
#print(x)
#print(y)
#print(z)
#print(a)
#print(b)
#print(c)