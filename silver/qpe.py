from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit.library import UnitaryGate
import numpy as np

def qpe(t, control, target, circuit, U):
    # U is the unitary matrix (numpy array) whose eigenvalue we would like to estimate.
    # Qiskit ordering: control[0] is the least significant qubit of the control register.
    # control[j] controls U^(2^j), so after iqft the control register holds phase*2^t,
    # which can be read directly as an integer from the measurement result.

    #Apply Hadamard to control qubits
    for qb in control:
        circuit.h(qb)

    for j in range(t):
        #Create the gate CU^(2^j) where control[j] is the control qubit
        CU = UnitaryGate(np.linalg.matrix_power(U, 2**j)).control()
        circuit.append(CU, [control[j]] + list(target))

    #Apply inverse QFT
    iqft(t,control,circuit)
