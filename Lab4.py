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
        # Здесь будет реализация метода
        pass
    
    def __sub__(self, other):
        # Здесь будет реализация метода
        pass
    
    def __mul__(self, other):
        # Здесь будет реализация метода
        pass
    
    def __rmul__(self, other):
        # Здесь будет реализация метода
        pass
    
    def __truediv__(self, other):
        # Здесь будет реализация метода
        pass
    
    def eval(self, x):
        # Здесь будет реализация метода
        pass
    
    def sub(self, other):
        # Здесь будет реализация метода
        pass
    
    def diff(self, n=1):
        # Здесь будет реализация метода
        pass
    
    def integrate(self, n=1, a=0, b=1):
        # Здесь будет реализация метода
        pass