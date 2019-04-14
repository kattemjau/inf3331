class Polynomial:

    def __init__(self, coefficient):
        """coefficients should be a list of numbers with
        the i-th element being the coefficient a_i."""
        self.coefficient=coefficient

        length=self.coefficient
        for n in reversed(self.coefficient):
            if(n==0):
                self.coefficient.pop()

            else:
                return

    def degree(self):
        """Return the index of the highest nonzero coefficient.
        If there is no nonzero coefficient, return -1."""

        return len(self.coefficient)-1

        """highest=self.coefficient[0]
        index=0
        counter=0
        for temp in self.coefficient:
            if temp > highest:
                highest=temp
                index=counter

            counter+=1

        if highest==0:
            return -1

        return index

        raise NotImplemented """

    def coefficients(self):
        """Return the list of coefficients.

        The i-th element of the list should be a_i, meaning that the last
        element of the list is the coefficient of the highest degree term."""

        return self.coefficient

        raise NotImplemented

    def __call__(self, x):
        """Return the value of the polynomial evaluated at the number x"""

        suum=0
        temp=1
        counter=-1
        for num in self.coefficient:
            counter+=1
            if counter != 0:
                temp=x**counter

            suum+=temp*num

        return suum

        raise NotImplemented


    def __add__(self, p):
        """Return the polynomial which is the sum of p and this polynomial
        Should assume p is Polynomial([p]) if p is int.

        If p is not an int or Polynomial, should raise ArithmeticError."""

        result=[]

        if isinstance(p, (int, Polynomial)):
            if isinstance(p, int):
                p=Polynomial([p])

            length= len(p.coefficients())

            counter=-1
            for num in self.coefficient:
                counter+=1
                if counter<length:
                    result.append(num+p.coefficient[counter])
                else:
                    result.append(num)

            for kk in range(len(self.coefficient), len(p.coefficients())):
                result.append(p.coefficient[kk])


            return Polynomial(result)

        else:
            raise ArithmeticError

    def __sub__(self, p):
        """Return the polynomial which is the difference of p and this polynomial
        Should assume p is Polynomial([p]) if p is int.

        If p is not an int or Polynomial, should raise ArithmeticError."""

        result=[]

        if isinstance(p, (int, Polynomial)):
            if isinstance(p, int):
                p=Polynomial([p])

            length= len(p.coefficients())

            counter=-1
            for num in self.coefficient:
                counter+=1
                if counter<length:
                    result.append(num-p.coefficient[counter])
                else:
                    result.append(num)

            for kk in range(len(self.coefficient), len(p.coefficients())):
                result.append(p.coefficient[kk])


            return Polynomial(result)

        else:
            raise ArithmeticError


    def __mul__(self, c):
        """Return the polynomial which is this polynomial multiplied by given integer.
        Should raise ArithmeticError if c is not an int."""

        result=[]

        if isinstance(c, int):
            counter=-1
            for num in self.coefficient:
                counter+=1
                result.append(num*c)


            return Polynomial(result)

        else:
            raise ArithmeticError


    def __rmul__(self, c):
        """Return the polynomial which is this polynomial multiplied by some integer"""

        result=[]

        if isinstance(c, int):
            counter=-1
            for num in self.coefficient:
                counter+=1
                result.append(num*c)


            return Polynomial(result)

        else:
            raise ArithmeticError

    def __repr__(self):
        """Return a nice string representation of polynomial.

        E.g.: x^6 - 5x^3 + 2x^2 + x - 1
        """
        string=" "
        counter = len(self.coefficient)
        counter=counter-1
        mak=counter
        c=0
        for i in reversed(self.coefficient):
            if mak==c:
                string+= str(i) + " "
            elif i==0:
                counter=counter-1
                c+=1
                continue;
            else:
                string+= str(i) + "x^" + str(counter) + " + "

            counter=counter-1

            c+=1
        return string

    def __eq__(self, p):
        """Check if two polynomials have the same coefficients."""

        return p.coefficients() == self.coefficients()

def sample_usage():
    p = Polynomial([1, 2, 1]) # 1 + 2x + x^2
    q = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3


    print("The value of {} at {} is {}".format(p, 7, p(7)))

    print("The coefficients of {} are {}".format(p, p.coefficients()))


    print("\nAdding {} and {} yields {}".format(p, q, p+q))

    p, q, r = map(Polynomial,
                  [
                      [1, 0, 1], [0, 2, 0], [1, 2, 1]
                  ]
    )

    print("\nWill adding {} and {} be the same as {}? Answer: {}".format(
        p, q, r, p+q == r
    ))
    print("\nIs {} - {} the same as {}? Answer: {}".format(
        p, q, r, p-q == r
    ))
