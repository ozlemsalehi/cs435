from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from math import pi

def qft(n, qubits, circuit):
    # Qiskit ordering: qubits[n-1] is the most significant qubit (j_1 in the text)
    # and qubits[0] is the least significant qubit (j_n in the text).

    #For each qubit, starting from the most significant one
    for i in range(n-1,-1,-1):
        #Apply Hadamard to the qubit
        circuit.h(qubits[i])

        #Apply CR_k gates where j is the control and i is the target
        k=2 #We start with k=2
        for j in range(i-1,-1,-1):
            circuit.cp(2*pi/2**k, qubits[j],qubits[i])
            k=k+1 #Increment k at each step

    #Swap the qubits
    for i in range(n//2):
        circuit.swap(qubits[i],qubits[n-i-1])
