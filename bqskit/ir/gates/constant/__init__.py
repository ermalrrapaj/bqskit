"""This package defines constant gates."""
from __future__ import annotations

from bqskit.ir.gates.constant.cx import  CNOTGate, CXGate, CCXGate, ToffoliGate 
from bqskit.ir.gates.constant.ch import CHGate
from bqskit.ir.gates.constant.clock import ClockGate
from bqskit.ir.gates.constant.cclock import CClockGate
from bqskit.ir.gates.constant.cpd import CPDGate
from bqskit.ir.gates.constant.cpi import CPIGate
from bqskit.ir.gates.constant.cshift import CShiftGate
from bqskit.ir.gates.constant.csum import CSUMGate
#from bqskit.ir.gates.constant.csumd import CSUMDGate
from bqskit.ir.gates.constant.ct import CTGate
from bqskit.ir.gates.constant.cy import CYGate
from bqskit.ir.gates.constant.cz import CZGate
from bqskit.ir.gates.constant.h import HGate
from bqskit.ir.gates.constant.identity import IdentityGate
from bqskit.ir.gates.constant.iswap import ISwapGate
from bqskit.ir.gates.constant.itoffoli import IToffoliGate
from bqskit.ir.gates.constant.pd import PDGate
from bqskit.ir.gates.constant.permutation import PermutationGate
from bqskit.ir.gates.constant.s import SGate
from bqskit.ir.gates.constant.sdg import SdgGate
from bqskit.ir.gates.constant.shift import ShiftGate
from bqskit.ir.gates.constant.sqrtcnot import SqrtCNOTGate
from bqskit.ir.gates.constant.sqrtiswap import SqrtISwapGate
from bqskit.ir.gates.constant.subswap import SubSwapGate
from bqskit.ir.gates.constant.swap import SwapGate
from bqskit.ir.gates.constant.sx import SqrtXGate, SXGate
from bqskit.ir.gates.constant.sycamore import SycamoreGate
from bqskit.ir.gates.constant.t import TGate
from bqskit.ir.gates.constant.tdg import TdgGate
from bqskit.ir.gates.constant.unitary import ConstantUnitaryGate
from bqskit.ir.gates.constant.x import XGate
from bqskit.ir.gates.constant.xx import XXGate
from bqskit.ir.gates.constant.y import YGate
from bqskit.ir.gates.constant.yy import YYGate
from bqskit.ir.gates.constant.z import ZGate
from bqskit.ir.gates.constant.zz import ZZGate
from bqskit.ir.gates.constant.cs import CSGate

__all__ = [
    'CNOTGate',
    'CXGate',
    'CCXGate',
    'ToffoliGate',
    'CHGate',
    'ClockGate',
    'CClockGate',
    'CPDGate',
    'CPIGate',
    'CSGate',
    'CShiftGate',
    'CSUMGate',
    'CTGate',
    'CYGate',
    'CZGate',
    'HGate',
    'IdentityGate',
    'ISwapGate',
    'IToffoliGate',
    'PDGate',
    'PermutationGate',
    'SGate',
    'SdgGate',
    'ShiftGate',
    'SqrtCNOTGate',
    'SqrtISwapGate',
    'SubSwapGate',
    'SwapGate',
    'SqrtXGate',
    'SXGate',
    'SycamoreGate',
    'TGate',
    'TdgGate',
    'ConstantUnitaryGate',
    'XGate',
    'XXGate',
    'YGate',
    'YYGate',
    'ZGate',
    'ZZGate',
]
