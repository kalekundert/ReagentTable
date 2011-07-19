#!/usr/bin/env python

from compound import *
from calculator import *

reference = Reference("Nitrophenol-Acid", eqv=1, mm=211.17, mg=1000)
compounds = [
		reference,
		Compound("Aminophenol-Acid", eqv=1, mm=181.07) ]

find_masses(reference, compounds)
print_masses(compounds)
