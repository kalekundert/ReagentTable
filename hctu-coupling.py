#!/usr/bin/env python

from compound import *
from calculator import *

reference = Reference("Aminophenol", eqv=1, mm=181.19, mg=87.8)
compounds = [
		reference,
		Compound("Nitrophenyl-Amine", eqv=1, mm=202.64),
		Compound("HCTU", eqv=1, mm=413.7),
		Compound("TEA", eqv=3, mm=101.19), 
		Compound("Coupled Product", eqv=1, mm=329.14) ]

find_masses(reference, compounds)
print_masses(compounds)
