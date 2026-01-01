from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import AerSimulator
from math import pi

def iqft(n, qubits, circuit):
    #Swap the qubits
    for i in range(n//2):
        circuit.swap(qubits[i],qubits[n-i-1])     

    #For each qubit
    for i in range(n-1,-1,-1):
        #Apply CR_k gates where j is the control and i is the target
        k=n-i #We start with k=n-i
        for j in range(n-1,i,-1):
            #Apply CR_k gate  
            circuit.cp(-pi*2/2**(k), qubits[j],qubits[i])
            k=k-1 #Decrement k at each step

        #Apply Hadamard to the qubit
        circuit.h(qubits[i])
