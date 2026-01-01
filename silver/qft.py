
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import StatevectorSimulator
from math import pi

def qft(n, qubits, circuit):
    #For each qubit
    for i in range(n):
        #Apply Hadamard to the qubit
        circuit.h(qubits[i])

        #Apply CR_k gates where j is the control and i is the target
        k=2 #We start with k=2
        for j in range(i+1,n):
            #Apply CR_k gate  
            circuit.cp(pi*2/2**(k), qubits[j],qubits[i])
            k=k+1 #Increment k at each step

    for i in range(n//2):
        circuit.swap(qubits[i],qubits[n-i-1])     

