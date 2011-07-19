class Compound(object):

	def __init__(self, name, eqv, mm):
		self.name = name
		self.equivalents = eqv
		self.molar_mass = mm

class Reference(Compound):

	def __init__(self, name, eqv, mm, mg):
		Compound.__init__(self, name, eqv, mm)
		self.mass = mg
		

