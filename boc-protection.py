#!/usr/bin/env python

from compound import *
from calculator import *

reference = Reference("Aminophenol", eqv=1, mm=181.19, mg=218.2)
compounds = [
		reference,
		Compound("Boc Anhydride", eqv=1, mm=218.25),
		Compound("TEA", eqv=1.5, mm=101.19) ]

find_masses(reference, compounds)
print_masses(compounds)
