class Factor(object):
    def __init__(self, number):
        self.number = number

    @property
    def raindrops(self):
        drops = ((3,'Pling'), (5,'Plang'), (7,'Plong'));

        list = [s for f, s in drops if self.number % f == 0]
	return "".join(list) if list else str(self.number)

    @property
    def getFactor(self):
        factors=[];

        for i in range(1, self.number + 1):
            if self.number % i == 0:
                factors.append(i)

        return factors
