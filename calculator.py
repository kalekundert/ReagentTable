#!/usr/bin/env python

from compound import *

def find_masses(known, compounds):
    known.moles = known.mass / known.molar_mass

    for compound in compounds:
        compound.moles = known.moles * compound.equivalents
        compound.mass = compound.moles * compound.molar_mass

def print_masses(compounds):
    print "Compound                eqv     mmol       mg     "
    print "====================    ====    =======    ======="

    template = "%-20s    %-4.1f    %-7.2f    %-7.2f"
              
    for compound in compounds:
        print template % (
                compound.name,
                compound.equivalents,
                compound.moles,
                compound.mass)
