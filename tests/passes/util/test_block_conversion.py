from __future__ import annotations

from typing import Any

from bqskit.ir.circuit import Circuit
from bqskit.ir.gates import CircuitGate
from bqskit.ir.gates import ConstantUnitaryGate
from bqskit.ir.gates import VariableUnitaryGate
from bqskit.passes.util.conversion import BlockConversionPass


def test_circuit_gate_to_variable_gate(r3_qubit_circuit: Any) -> None:
    in_utry = r3_qubit_circuit.get_unitary()
    cg = CircuitGate(r3_qubit_circuit)
    cir = Circuit(3)
    cir.append_gate(cg, [0, 1, 2])

    cir.perform(BlockConversionPass('variable'))

    out_untry = cir.get_unitary()

    assert in_utry == out_untry  # This is failing and I don't know why
    assert all(isinstance(op.gate, VariableUnitaryGate) for op in cir)


def test_circuit_gate_to_constant_gate(r3_qubit_circuit: Any) -> None:
    in_utry = r3_qubit_circuit.get_unitary()
    cg = CircuitGate(r3_qubit_circuit)
    cir = Circuit(3)
    cir.append_gate(cg, [0, 1, 2])

    cir.perform(BlockConversionPass('constant'))

    out_untry = cir.get_unitary()

    assert in_utry == out_untry  # This is failing and I don't know why
    assert all(isinstance(op.gate, ConstantUnitaryGate) for op in cir)
