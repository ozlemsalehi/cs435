from qiskit.circuit.library import PhaseGate
from math import pi
import numpy as np

#Unitary matrix U with eigenvector |11> and eigenvalue e^{2 pi i phase}
#U = diag(1, 1, 1, -0.4762382+0.87931631j)
phase = 0.329
U = PhaseGate(2*pi*phase).control().to_matrix()