#!/usr/bin/env python3

# A: Ala, name: Alanine
# I: Ile, name: Isoleucine
# R: Arg, name: Arginine
# L: Leu, name: Leucine
# N: Asn, name: Asparagine
# K: Lys, name: Lysine
# D: Asp, name: Aspartic Acid
# M: Met, name: Methionine (START)
# F: Phe, name: Phenylalanine
# C: Cys, name: Cysteine
# P: Pro, name: Proline
# Q: Gln, name: Glutamine
# S: Ser, name: Serine
# E: Glu, name: Glutamic Acid
# T: Thr, name: Threonine
# W: Trp, name: Tryptophan
# G: Gly, name: Glycine
# Y: Tyr, name: Tyrosine
# H: His, name: Histidine
# V: Val, name: Valine
#
# U: Sec, name: Selenocysteine | uga (STOP)
# O: Pyl | uag (STOP)

nucleotides = ['A', 'C', 'G', 'T', 'N'] # N = Unknown | T (DNA) > U (RNA) in transcription

def RNA():
    table = {
        'Ala / A': ['GCU', 'GCC', 'GCA', 'GCG'],
        'Ile / I': ['AUU', 'AUC', 'AUA'],
        'Arg / R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
        'Leu / L': ['CUU', 'CUC', 'CUA', 'CUG', 'UUA', 'UUG'],
        'Asn / N': ['AAU', 'AAC'],
        'Lys / K': ['AAA', 'AAG'],
        'Asp / D': ['GAU', 'GAC'],
        'Met / M': ['AUG'],
        'Phe / F': ['UUU', 'UUC'],
        'Cys / C': ['UGU', 'UGC'],
        'Pro / P': ['CCU', 'CCC', 'CCA', 'CCG'],
        'Gln / Q': ['CAA', 'CAG'],
        'Ser / S': ['UCU', 'UCC', 'UCA', 'UCG',  'AGU', 'AGC'],
        'Glu / E': ['GAA', 'GAG'],
        'Thr / T': ['ACU', 'ACC', 'ACA', 'ACG'],
        'Trp / W': ['UGG'],
        'Gly / G': ['GGU', 'GGC', 'GGA', 'GGG'],
        'Tyr / Y': ['UAU', 'UAC'],
        'His / H': ['CAU', 'CAC'],
        'Val / V': ['GUU', 'GUC', 'GUA', 'GUG'],
        'STOP / *': ['UAA', 'UGA', 'UAG'],
        }
    return table

def amino_weight():
    table = {
        'Ala / A': 89.09,
        'Ile / I': 131.18,
        'Arg / R': 174.20,
        'Leu / L': 131.18,
        'Asn / N': 132.12,
        'Lys / K': 146.19,
        'Asp / D': 133.10,
        'Met / M': 149.21,
        'Phe / F': 165.19,
        'Cys / C': 121.16,
        'Pro / P': 115.13,
        'Gln / Q': 146.15,
        'Ser / S': 105.09,
        'Glu / E': 147.13,
        'Thr / T': 119.12,
        'Trp / W': 204.23,
        'Gly / G': 75.07,
        'Tyr / Y': 181.19,
        'His / H': 155.16,
        'Val / V': 117.15,
        'STOP / *': [],
        }
    return table

def pKa():
    table = {
        'alpha_amino': {'G': 9.60, 'A': 9.69, 'V': 9.62, 'L': 9.60, 'I': 9.68, 'M': 9.21, 'F': 9.13, 'W': 9.39, 'P': 10.60, 'S': 9.15,
                       'T': 9.10, 'C': 10.78, 'Y': 9.11, 'N': 8.84, 'Q': 9.13, 'D': 9.82, 'E': 9.67, 'K': 8.95, 'R': 9.04, 'H': 9.17},
        'alpha_carboxy': {'G': 2.34, 'A': 2.34, 'V': 2.32, 'L': 2.36, 'I': 2.36, 'M': 2.28, 'F': 1.83, 'W': 2.38, 'P': 1.99, 'S': 2.21,
                          'T': 2.63, 'C': 1.71, 'Y': 2.2, 'N': 2.02, 'Q': 2.17, 'D': 2.09, 'E': 2.19, 'K': 2.18, 'R': 2.17, 'H': 1.82},
        'sidechain_positive': {'K': 10.79, 'R': 12.48, 'H': 6.04},
        'sidechain_negative': {'D': 3.86, 'E': 4.25, 'C': 8.33, 'Y': 10.07},
        }
    return table

# Host: Mammalian | Yeast | E.Coli
# Unit: Minutes
def halflife():
    table = {
        'Ala / A': [264, 1200, 600],
        'Ile / I': [1200, 30, 600],
        'Arg / R': [60, 2, 2],
        'Leu / L': [330, 3, 2],
        'Asn / N': [84, 3, 600],
        'Lys / K': [78, 3, 2],
        'Asp / D': [66, 3, 600],
        'Met / M': [1800, 1200, 600],
        'Phe / F': [66, 3, 2],
        'Cys / C': [72, 1200, 600],
        'Pro / P': [1200, 1200, 600],
        'Gln / Q': [48, 10, 600],
        'Ser / S': [114, 1200, 600],
        'Glu / E': [60, 30, 600],
        'Thr / T': [432, 1200, 600],
        'Trp / W': [168, 3, 2],
        'Gly / G': [1800, 1200, 600],
        'Tyr / Y': [168, 10, 2],
        'His / H': [210, 10, 600],
        'Val / V': [6000, 1200, 600],
        'STOP / *': [],
        }
    return table

def hydropathy():
    table = {
        'Ala / A': 1.8,
        'Ile / I': 4.5,
        'Arg / R': -4.5,
        'Leu / L': 3.8,
        'Asn / N': -3.5,
        'Lys / K': -3.9,
        'Asp / D': -3.5,
        'Met / M': 1.9,
        'Phe / F': 2.8,
        'Cys / C': 2.5,
        'Pro / P': -1.6,
        'Gln / Q': -3.5,
        'Ser / S': -0.8,
        'Glu / E': -3.5,
        'Thr / T': -0.7,
        'Trp / W': -0.9,
        'Gly / G': -0.4,
        'Tyr / Y': -1.3,
        'His / H': -3.2,
        'Val / V': 4.2,
        'STOP / *': [],
        }
    return table

# C = Carbon | H = Hydrogen | N = Nitrogen | O = Oxygen | S = Sulfur
def atomic():
    table = {
        'Ala / A': (3, 7, 1, 2, 0), # C3H7NO2
        'Ile / I': [6, 13, 1, 2, 0], # C6H13NO2
        'Arg / R': [6, 14, 4, 2, 0], # C6H14N4O2
        'Leu / L': [6, 13, 1, 2, 0], # C6H13NO2
        'Asn / N': [4, 8, 2, 3, 0], # C4H8N2O3
        'Lys / K': [6, 14, 2, 2, 0], # C6H14N2O2
        'Asp / D': [4, 7, 1, 4, 0], # C4H7NO4
        'Met / M': [5, 11, 1, 2, 1], # C5H11NO2S
        'Phe / F': [9, 11, 1, 2, 0], # C9H11NO2
        'Cys / C': [3, 7, 1, 2, 1], # C3H7NO2S
        'Pro / P': [5, 9, 1, 2, 0], # C5H9NO2
        'Gln / Q': [5, 10, 2, 3, 0], # C5H10N2O3
        'Ser / S': [3, 7, 1, 3, 0], # C3H7NO3
        'Glu / E': [5, 9, 1, 4, 0], # C5H9NO4
        'Thr / T': [4, 9, 1, 3, 0], # C4H9NO3
        'Trp / W': [11, 12, 2, 2, 0], # C11H12N2O2
        'Gly / G': [2, 5, 1, 2, 0], # C2H5NO2
        'Tyr / Y': [9, 11, 1, 3, 0], # C9H11NO3
        'His / H': [6, 9, 3, 2, 0], # C6H9N3O2
        'Val / V': [5, 11, 1, 2, 0], # C5H11NO2
        'STOP / *': [],
        }
    return table

def DIWV():
    table = {
        'W': {'W':    1.0, 'C':   1.0, 'M': 24.68, 'H': 24.68, 'Y':   1.0, 'F':    1.0, 'Q':   1.0, 'N':  13.34, 'I':   1.0, 'R':    1.0, 'D':    1.0, 'P':   1.0, 'T': -14.03, 'K':    1.0, 'E':   1.0, 'V': -7.49, 'S':   1.0, 'G':  -9.37, 'A': -14.03, 'L': 13.34},
        'C': {'W':  24.68, 'C':   1.0, 'M':  33.6, 'H':  33.6, 'Y':   1.0, 'F':    1.0, 'Q': -6.54, 'N':    1.0, 'I':   1.0, 'R':    1.0, 'D':  20.26, 'P': 20.26, 'T':   33.6, 'K':    1.0, 'E':   1.0, 'V': -6.54, 'S':   1.0, 'G':    1.0, 'A':    1.0, 'L': 20.26},
        'M': {'W':    1.0, 'C':   1.0, 'M': -1.88, 'H': 58.28, 'Y': 24.68, 'F':    1.0, 'Q': -6.54, 'N':    1.0, 'I':   1.0, 'R':  -6.54, 'D':    1.0, 'P': 44.94, 'T':  -1.88, 'K':    1.0, 'E':   1.0, 'V':   1.0, 'S': 44.94, 'G':    1.0, 'A':  13.34, 'L':   1.0},
        'H': {'W':  -1.88, 'C':   1.0, 'M':   1.0, 'H':   1.0, 'Y': 44.94, 'F':  -9.37, 'Q':   1.0, 'N':  24.68, 'I': 44.94, 'R':    1.0, 'D':    1.0, 'P': -1.88, 'T':  -6.54, 'K':  24.68, 'E':   1.0, 'V':   1.0, 'S':   1.0, 'G':  -9.37, 'A':    1.0, 'L':   1.0},
        'Y': {'W':  -9.37, 'C':   1.0, 'M': 44.94, 'H': 13.34, 'Y': 13.34, 'F':    1.0, 'Q':   1.0, 'N':    1.0, 'I':   1.0, 'R': -15.91, 'D':  24.68, 'P': 13.34, 'T':  -7.49, 'K':    1.0, 'E': -6.54, 'V':   1.0, 'S':   1.0, 'G':  -7.49, 'A':  24.68, 'L':   1.0},
        'F': {'W':    1.0, 'C':   1.0, 'M':   1.0, 'H':   1.0, 'Y':  33.6, 'F':    1.0, 'Q':   1.0, 'N':    1.0, 'I':   1.0, 'R':    1.0, 'D':  13.34, 'P': 20.26, 'T':    1.0, 'K': -14.03, 'E':   1.0, 'V':   1.0, 'S':   1.0, 'G':    1.0, 'A':    1.0, 'L':   1.0},
        'Q': {'W':    1.0, 'C': -6.54, 'M':   1.0, 'H':   1.0, 'Y': -6.54, 'F':  -6.54, 'Q': 20.26, 'N':    1.0, 'I':   1.0, 'R':    1.0, 'D':  20.26, 'P': 20.26, 'T':    1.0, 'K':    1.0, 'E': 20.26, 'V': -6.54, 'S': 44.94, 'G':    1.0, 'A':    1.0, 'L':   1.0},
        'N': {'W':  -9.37, 'C': -1.88, 'M':   1.0, 'H':   1.0, 'Y':   1.0, 'F': -14.03, 'Q': -6.54, 'N':    1.0, 'I': 44.94, 'R':    1.0, 'D':    1.0, 'P': -1.88, 'T':  -7.49, 'K':  24.68, 'E':   1.0, 'V':   1.0, 'S':   1.0, 'G': -14.03, 'A':    1.0, 'L':   1.0},
        'I': {'W':    1.0, 'C':   1.0, 'M':   1.0, 'H': 13.34, 'Y':   1.0, 'F':    1.0, 'Q':   1.0, 'N':    1.0, 'I':   1.0, 'R':    1.0, 'D':    1.0, 'P': -1.88, 'T':    1.0, 'K':  -7.49, 'E': 44.94, 'V': -7.49, 'S':   1.0, 'G':    1.0, 'A':    1.0, 'L': 20.26},
        'R': {'W':  58.28, 'C':   1.0, 'M':   1.0, 'H': 20.26, 'Y': -6.54, 'F':    1.0, 'Q': 20.26, 'N':  13.34, 'I':   1.0, 'R':  58.28, 'D':    1.0, 'P': 20.26, 'T':    1.0, 'K':    1.0, 'E':   1.0, 'V':   1.0, 'S': 44.94, 'G':  -7.49, 'A':    1.0, 'L':   1.0},
        'D': {'W':    1.0, 'C':   1.0, 'M':   1.0, 'H':   1.0, 'Y':   1.0, 'F':  -6.54, 'Q':   1.0, 'N':    1.0, 'I':   1.0, 'R':  -6.54, 'D':    1.0, 'P':   1.0, 'T': -14.03, 'K':  -7.49, 'E':   1.0, 'V':   1.0, 'S': 20.26, 'G':    1.0, 'A':    1.0, 'L':   1.0},
        'P': {'W':  -1.88, 'C': -6.54, 'M': -6.54, 'H':   1.0, 'Y':   1.0, 'F':  20.26, 'Q': 20.26, 'N':    1.0, 'I':   1.0, 'R':  -6.54, 'D':  -6.54, 'P': 20.26, 'T':    1.0, 'K':    1.0, 'E': 18.38, 'V': 20.26, 'S': 20.26, 'G':    1.0, 'A':  20.26, 'L':   1.0},
        'T': {'W': -14.03, 'C':   1.0, 'M':   1.0, 'H':   1.0, 'Y':   1.0, 'F':  13.34, 'Q': -6.54, 'N': -14.03, 'I':   1.0, 'R':    1.0, 'D':    1.0, 'P':   1.0, 'T':    1.0, 'K':    1.0, 'E': 20.26, 'V':   1.0, 'S':   1.0, 'G':  -7.49, 'A':    1.0, 'L':   1.0},
        'K': {'W':    1.0, 'C':   1.0, 'M':  33.6, 'H':   1.0, 'Y':   1.0, 'F':    1.0, 'Q': 24.68, 'N':    1.0, 'I': -7.49, 'R':   33.6, 'D':    1.0, 'P': -6.54, 'T':    1.0, 'K':    1.0, 'E':   1.0, 'V': -7.49, 'S':   1.0, 'G':  -7.49, 'A':    1.0, 'L': -7.49},
        'E': {'W': -14.03, 'C': 44.94, 'M':   1.0, 'H': -6.54, 'Y':   1.0, 'F':    1.0, 'Q': 20.26, 'N':    1.0, 'I': 20.26, 'R':    1.0, 'D':  20.26, 'P': 20.26, 'T':    1.0, 'K':    1.0, 'E':  33.6, 'V':   1.0, 'S': 20.26, 'G':    1.0, 'A':    1.0, 'L':   1.0},
        'V': {'W':    1.0, 'C':   1.0, 'M':   1.0, 'H':   1.0, 'Y': -6.54, 'F':    1.0, 'Q':   1.0, 'N':    1.0, 'I':   1.0, 'R':    1.0, 'D': -14.03, 'P': 20.26, 'T':  -7.49, 'K':  -1.88, 'E':   1.0, 'V':   1.0, 'S':   1.0, 'G':  -7.49, 'A':    1.0, 'L':   1.0},
        'S': {'W':    1.0, 'C':  33.6, 'M':   1.0, 'H':   1.0, 'Y':   1.0, 'F':    1.0, 'Q': 20.26, 'N':    1.0, 'I':   1.0, 'R':  20.26, 'D':    1.0, 'P': 44.94, 'T':    1.0, 'K':    1.0, 'E': 20.26, 'V':   1.0, 'S': 20.26, 'G':    1.0, 'A':    1.0, 'L':   1.0},
        'G': {'W':  13.34, 'C':   1.0, 'M':   1.0, 'H':   1.0, 'Y': -7.49, 'F':    1.0, 'Q':   1.0, 'N':  -7.49, 'I': -7.49, 'R':    1.0, 'D':    1.0, 'P':   1.0, 'T':  -7.49, 'K':  -7.49, 'E': -6.54, 'V':   1.0, 'S':   1.0, 'G':  13.34, 'A':  -7.49, 'L':   1.0},
        'A': {'W':    1.0, 'C': 44.94, 'M':   1.0, 'H': -7.49, 'Y':   1.0, 'F':    1.0, 'Q':   1.0, 'N':    1.0, 'I':   1.0, 'R':    1.0, 'D':  -7.49, 'P': 20.26, 'T':    1.0, 'K':    1.0, 'E':   1.0, 'V':   1.0, 'S':   1.0, 'G':    1.0, 'A':    1.0, 'L':   1.0},
        'L': {'W':  24.68, 'C':   1.0, 'M':   1.0, 'H':   1.0, 'Y':   1.0, 'F':    1.0, 'Q':  33.6, 'N':    1.0, 'I':   1.0, 'R':  20.26, 'D':    1.0, 'P': 20.26, 'T':    1.0, 'K':  -7.49, 'E':   1.0, 'V':   1.0, 'S':   1.0, 'G':    1.0, 'A':    1.0, 'L':   1.0}
      }
    return table