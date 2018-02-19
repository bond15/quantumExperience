import sys
if sys.version_info < (3,5):
	raise Exception('Python 3.5')

from qiskit import QuantumProgram

qp = QuantumProgram();

def makeSuperpositionState(numberQubits):

	#create registers
	qr = qp.create_quantum_register('qr2',numberQubits);
	cr = qp.create_classical_register('cr2',numberQubits);
	#create circuite
	qc = qp.create_circuit('circuitB',[qr],[cr])

	for n in range(0,numberQubits):
		qc.h(qr[n])
		qc.measure(qr[n],cr[n])


def makeEntangledState():
	#allocate registers
	qr = qp.create_quantum_register('qr1',2);
	cr = qp.create_classical_register('cr1',2);
	#create a circuit
	qc = qp.create_circuit('circuitA',[qr],[cr])

	# program circuit
	qc.h(qr[0])
	qc.cx(qr[0],qr[1])

	#measure
	qc.measure(qr[0],cr[0])
	qc.measure(qr[1],cr[1])


def runAndDisplay(circuits):

	backend = 'local_qasm_simulator'

	for circuit in circuits:
		print(circuit)
		qobj = qp.compile(circuits, backend);
		result = qp.run(qobj,wait = 5, timeout = 2400)
		print(result.get_counts(circuit))


if __name__ == '__main__':
#def main():

	makeEntangledState();
	runAndDisplay(['circuitA'])

	makeSuperpositionState(5)
	runAndDisplay(['circuitB'])
	#minimal



	#qr = qp.create_quantum_register('qr', 2)
	#cr = qp.create_classical_register('cr',2)

	#quantum programs have many circuits
	#qc = qp.create_circuit('circuitA', [qr],[cr])


	#circuit = qp.get_circuit('circuitA')

	#quantum_r = qp.get_quantum_register('qr')
	#classical_r = qp.get_classical_register('cr')

	#circuit.h(quantum_r[0])
	#circuit.h(quantum_r[1])
	#circuit.cx(quantum_r[0], quantum_r[1])
	#circuit.measure(quantum_r[0], classical_r[0])
	#circuit.measure(quantum_r[1], classical_r[1])


	#print the qasm
	#qasm = qp.get_qasm('circuitA');
	#print(qasm);

	#compile and simulate