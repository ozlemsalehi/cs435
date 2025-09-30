from qiskit.quantum_info.operators import Operator
from qiskit.circuit.library import CPhaseGate
from math import pi
import numpy as np

def Ux(x,N):

    # Number of qubits [ceil(log_2(N))]
    k=1
    while(N>2**k):
        k=k+1

    # Matrix representation of U
    u = np.zeros([2**k, 2**k], dtype = int) 

    for i in range(N):
        u[x*i%N][i]=1
    for i in range(N,2**k):
        u[i][i]=1

    XU=Operator(u)
    
    return XU
