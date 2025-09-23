import random
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def oracle():
    type = random.choice(["constant", "balanced"])
    result = QuantumCircuit(2)
    result.barrier()
    
    if type == "constant":
        # we ignore the input and randomly add a not gate
        if random.randrange(2) == 0:
            result.x(1)
    elif type == "balanced":
        # making sure the output is balanced
        result.cx(0, 1)
        # and randomly inverting it
        if random.randrange(2) == 0:
            result.x(1)
    
    result.barrier()
    return result

import random
from qiskit import QuantumCircuit

def oraclej(n):
    result = QuantumCircuit(n+1)
    result.barrier()
    
    type = random.choice(["constant", "balanced"])
    if type == "constant":
        # we ignore the input and randomly add a not gate
        if random.randrange(2) == 0:
            result.x(n)
    else:
        # we can add a single cnot to the circuit to have a balanced function
        # but we decide on the control qubit randomly
        control = random.randrange(n)
        result.cx(control, n)
        # randomly invert the result
        if random.randrange(2) == 0:
            result.x(n)
    
    result.barrier()
    return result

def bv_oracle():
    s="11010"
    n = len(s)
    s = s[::-1] # we revert the string since s_0 is at the left according to python 
    # and in the right according to qiskit
    
    circuit = QuantumCircuit(n+1)
    circuit.barrier()
    
    for i in range(n):
        if s[i] == '1':
            circuit.cx(i, n)
    
    circuit.barrier()
    return circuit

def f(x):
    if x=="000":
        return "001"
    elif x=="010":
        return "001"
    elif x=="011":
        return "000"
    elif x=="001":
        return "000"
    elif x=="100":
        return "101"
    elif x=="110":
        return "001"
    elif x=="111":
        return "100"
    elif x=="101":
        return "100"

def simon_oracle():
    qreg1 = QuantumRegister(3, "register_1")
    qreg2 = QuantumRegister(3, "register_2")
    creg = ClassicalRegister(3)

    simon_circuit = QuantumCircuit(qreg1, qreg2, creg)

    #map 000 and 010 to 000
    #Do nothing

    #map 111 to 100
    simon_circuit.mcx([0,1,2],5) 
    simon_circuit.barrier()

    #map 101 to 100
    simon_circuit.x(1)
    simon_circuit.mcx([0,1,2],5)
    simon_circuit.x(1)
    simon_circuit.barrier()

    #map 110 to 110
    simon_circuit.x(0)
    simon_circuit.mcx([0,1,2],4)
    simon_circuit.mcx([0,1,2],5)
    simon_circuit.x(0)
    simon_circuit.barrier()

    #map 100 to 110
    simon_circuit.x(0)
    simon_circuit.x(1)
    simon_circuit.mcx([0,1,2],4)
    simon_circuit.mcx([0,1,2],5)
    simon_circuit.x(0)
    simon_circuit.x(1)
    simon_circuit.barrier()    
    
    #map 001 to 010
    simon_circuit.x(1)
    simon_circuit.x(2)
    simon_circuit.mcx([0,1,2],4)
    simon_circuit.x(1)
    simon_circuit.x(2)
    simon_circuit.barrier()
    
    #map 011 to 010
    simon_circuit.x(2)
    simon_circuit.mcx([0,1,2],4)
    simon_circuit.x(2)
  

    return simon_circuit
    