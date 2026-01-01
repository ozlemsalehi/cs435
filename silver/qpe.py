from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.circuit.library import UnitaryGate

def qpe(t,control, target, circuit, U):

    #Apply Hadamard to control qubits
    for qb in control:
        circuit.h(qb)

    # raise U on the appropriate power
    for i in range(t):
        # Assemble list of control and target qubits
        qubits=[control[t-i-1]]
        for qq in target:
            qubits.append(qq)

        # Apply CU gates
        circuit.append(UnitaryGate(U).control(),qubits)

        # Increase the power of U for next iteration
        U=Operator(UnitaryGate(U.dot(U)))

    #Apply inverse QFT
    iqft(t,control,circuit)
