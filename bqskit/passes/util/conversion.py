"""This module implements the BlockConversionPass."""
from __future__ import annotations

import logging
from typing import Any
from typing import Callable
from typing import Sequence

from bqskit.compiler.basepass import BasePass
from bqskit.ir.circuit import Circuit
from bqskit.ir.gate import Gate
from bqskit.ir.gates import CircuitGate
from bqskit.ir.gates import ConstantUnitaryGate
from bqskit.ir.gates import VariableUnitaryGate
from bqskit.ir.operation import Operation
from bqskit.ir.point import CircuitPoint
from bqskit.qis.unitary.unitary import RealVector

_logger = logging.getLogger(__name__)


class BlockConversionPass(BasePass):
    """
    Converts blocks of one type to another type.

    Blocks are either described by a constant or variable unitary gate or as a
    circuit gate. Often during the flow of compilatin we will need to convert
    them from one form to another for a future pass.
    """

    def __init__(
        self,
        convert_target: str,
        convert_variable: bool = True,
        convert_constant: bool = True,
        convert_circuitgates: bool = True,
    ):
        """
        Construct a BlockConversionPass.

        Args:
            convert_target (str): Either `variable` or `constant`.
                Blocks will be converted to the form described here. If
                this is `variable` all gates will be converted to
                `VariableUnitaryGate` s. If this is `constant` blocks
                will be converted to `ConstantUnitaryGate` s. Blocks
                cannot be converted to circuit gates, that can be caried
                out by synthesis.

            convert_variable (bool): If this is true, this will replace
                VariableUnitaryGate's in the circuit with one's specified
                in convert_target.

            convert_constant (bool): If this is true, this will replace
                ConstantUnitaryGate's in the circuit with one's specified
                in convert_target.

            convert_circuitgates (bool): If this is true, this will replace
                CircuitGate's in the circuit with one's specified
                in convert_target. The subcircuit information captured
                in the circuit gate will be lost.
        """

        self.convert_origin_class_list: Sequence[type[Gate]] = []
        self.convert_target_class: type[
            VariableUnitaryGate | ConstantUnitaryGate
        ]
        self.conversion_operation: Callable[
            [
                Operation,
            ], tuple[VariableUnitaryGate | ConstantUnitaryGate, RealVector],
        ]

        if convert_target == 'variable':
            self.convert_target_class = VariableUnitaryGate
            self.conversion_operation = self.convert_op_to_variable
            if convert_constant:
                self.convert_origin_class_list.append(ConstantUnitaryGate)

        elif convert_target == 'constant':
            self.convert_target_class = ConstantUnitaryGate
            self.conversion_operation = self.convert_op_to_constant
            if convert_variable:
                self.convert_origin_class_list.append(VariableUnitaryGate)
        else:
            raise ValueError('Unexpected input for conversion target.')

        if convert_circuitgates:
            self.convert_origin_class_list.append(CircuitGate)

    async def run(self, circuit: Circuit, data: dict[str, Any] = {}) -> None:
        """Perform the pass's operation, see :class:`BasePass` for more."""

        _logger.debug(
            f'Converting {[o.__name__ for o in self.convert_origin_class_list]}\
              to {self.convert_target_class.__name__}',
        )

        for cycle, op in circuit.operations_with_cycles():
            if isinstance(op.gate, tuple(self.convert_origin_class_list)):
                new_gate, params = self.conversion_operation(op)
                point = CircuitPoint(cycle, op.location[0])
                circuit.replace_gate(point, new_gate, op.location, params)

    @staticmethod
    def convert_op_to_constant(
            op: Operation,
    ) -> tuple[ConstantUnitaryGate, RealVector]:

        return ConstantUnitaryGate(op.get_unitary(), op.radixes), []

    @staticmethod
    def convert_op_to_variable(
            op: Operation,
    ) -> tuple[VariableUnitaryGate, RealVector]:

        params = VariableUnitaryGate.get_params(op.get_unitary())
        vgate = VariableUnitaryGate(op.num_qudits, op.radixes)

        return vgate, params
