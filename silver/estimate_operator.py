from qiskit.quantum_info.operators import Operator
from qiskit.circuit.library import CPhaseGate
from math import pi
import numpy as np

#uU = Operator([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, -0.4762382+0.87931631j]])
phase = 0.329
U=Operator(CPhaseGate(2*pi*phase))
