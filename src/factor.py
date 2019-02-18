class Factor(object):
    def __init__(self, number):
        self.number = number

    @property
    def raindrops(self):
        drops = ((3,'Pling'), (5,'Plang'), (7,'Plong'));

        list = [s for f, s in drops if self.number % f == 0]
	return "".join(list) if list else str(self.number)
