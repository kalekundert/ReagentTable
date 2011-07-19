#!/usr/bin/env python

from compound import *
from calculator import *

reference = Reference("Aminophenol", eqv=1, mm=181.19, mg=175.9)
compounds = [
		reference,
		Compound("Trityl Chloride", eqv=1, mm=278.78),
		Compound("Triethylamine", eqv=3, mm=101.19) ]

find_masses(reference, compounds)
print_masses(compounds)
