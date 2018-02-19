from qiskit import QuantumProgram

#why?
if __name__ == '__main__':

	qp = QuantumProgram();
	qr = qp.create_quantum_register('qr',1)
	cr = qp.create_classical_register('cr',1)
	qc = qp.create_circuit('cir1', [qr],[cr])

	qc.x(qr[0])

	qc.measure(qr[0],cr[0])

	# print result count
	qobj = qp.compile(['cir1'],'local_qasm_simulator')
	result = qp.run(qobj,wait = 5, timeout = 2400)
	print(result.get_counts('cir1'))