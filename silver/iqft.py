from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from math import pi

def iqft(n, qubits, circuit):
    # Qiskit ordering: qubits[0] is the least significant qubit, qubits[n-1] the most significant.
    # The gates of qft() are applied in reverse order with negated angles.

    #Swap the qubits
    for i in range(n//2):
        circuit.swap(qubits[i],qubits[n-i-1])

    #For each qubit, starting from the least significant one
    for i in range(n):
        #Apply the inverse CR_k gates where j is the control and i is the target
        for j in range(i):
            k=i-j+1
            circuit.cp(-2*pi/2**k, qubits[j],qubits[i])

        #Apply Hadamard to the qubit
        circuit.h(qubits[i])
