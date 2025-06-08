from dataclasses import dataclass
from typing import Sequence
import math


def future_value(present_value: float, rate: float, periods: int) -> float:
    """Compute future value given present value, rate per period, and number of periods."""
    return present_value * (1 + rate) ** periods


def present_value(future_value: float, rate: float, periods: int) -> float:
    """Compute present value of future value given discount rate and periods."""
    return future_value / ((1 + rate) ** periods)


def emi(principal: float, annual_rate: float, months: int) -> float:
    """Calculate the equal monthly installment for a loan."""
    monthly_rate = annual_rate / 12
    if monthly_rate == 0:
        return principal / months
    return principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)


def npv(cashflows: Sequence[float], rate: float) -> float:
    """Net present value of a series of cashflows."""
    return sum(cf / ((1 + rate) ** i) for i, cf in enumerate(cashflows, start=1))


def weighted_score(scores: Sequence[float], weights: Sequence[float]) -> float:
    """Compute weighted average score."""
    if len(scores) != len(weights):
        raise ValueError("scores and weights must have same length")
    total_weight = sum(weights)
    if total_weight == 0:
        return 0.0
    return sum(s * w for s, w in zip(scores, weights)) / total_weight


def expected_utility(values: Sequence[float], probabilities: Sequence[float], risk_aversion: float = 1.0) -> float:
    """Simple expected utility with optional risk aversion."""
    if len(values) != len(probabilities):
        raise ValueError("values and probabilities must have same length")
    return sum(p * (v ** risk_aversion) for v, p in zip(values, probabilities))
