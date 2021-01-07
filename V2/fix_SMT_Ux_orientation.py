#!/usr/bin/env python3

# fix header names
# fix rotation of ICs (all U*), rotate by +90°

import re
import fileinput
import csv

filename = "Plots/Greaseweazle_F7_Plus_V2-top-pos.csv"
filenameOut = "Plots/Greaseweazle_F7_Plus_V2-top-pos_fixed.csv"

fieldsIn =  ['Ref',        'Val', 'Package', 'PosX',  'PosY',  'Rot',      'Side']
fieldsOut = ['Designator', 'Val', 'Package', 'Mid X', 'Mid Y', 'Rotation', 'Layer']

enc = 'utf-8'

# define the transformations
# each transformation can contain multiple conditions which must all be true to execute the 'rotOffset' action
# additional actions could be defined, e.g. for the position
transformations = [
	#{'conditions': [{'field': 'Ref', 'pattern': re.compile("^U\d+$")}], 'rotOffset': -90},
	{'conditions': [{'field': 'Ref', 'pattern': re.compile("^(U1|U2|Q1)$")}], 'rotOffset': 180},
	{'conditions': [{'field': 'Ref', 'pattern': re.compile("^(U5|U6)$")}], 'rotOffset': -90},
	# {'conditions': [{'field': 'LCSC', 'pattern': re.compile("^(C477988|C7809|C184582|C6060)$")}], 'rotOffset': -90} # TODO: field LCSC no available in normal export
]

with open(filenameOut, 'w', newline='') as csvfileout:
    writer = csv.DictWriter(csvfileout, fieldsOut, restval='', extrasaction='raise', dialect='excel')
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        writer.writeheader()
        for row in reader:
            #print(row)
            rot = float(row['Rot'])
            
            for trans in transformations:
                allCondMatch = True
                for cond in trans['conditions'] :
                    m = cond['pattern'].fullmatch(row[cond['field']])
                    if not m:
                        allCondMatch = False
                        break
                if allCondMatch:
                    rot = (rot + trans['rotOffset'] + 360) % 360
                    print("Ref=", row['Ref'], "  rotOffset=", trans['rotOffset'], "  rot=", rot)
                    break

            writer.writerow({'Designator': row['Ref'],'Val': row['Val'], 'Package': row['Package'], 'Mid X': row['PosX'], 'Mid Y': row['PosY'], 'Rotation': rot, 'Layer': row['Side']})

#:vim ts=4 sw=4 expandtab
