from dataclasses import dataclass
from typing import Optional
from .. import formulas


@dataclass
class InvestmentVsPrepaymentInput:
    debt_amount: float
    debt_interest_rate: float
    investment_amount: float
    expected_return_rate: float
    time_horizon_years: int
    risk_tolerance: Optional[str] = None
    volatility: Optional[float] = None


@dataclass
class InvestmentVsPrepaymentResult:
    future_value_investment: float
    future_value_debt: float
    recommendation: str


def compute_investment_vs_prepayment(params: InvestmentVsPrepaymentInput) -> InvestmentVsPrepaymentResult:
    fv_invest = formulas.future_value(
        params.investment_amount, params.expected_return_rate, params.time_horizon_years
    )
    fv_debt = formulas.future_value(
        params.debt_amount, params.debt_interest_rate, params.time_horizon_years
    )

    if fv_invest > fv_debt:
        rec = "Invest"
    else:
        rec = "Prepay Debt"

    return InvestmentVsPrepaymentResult(
        future_value_investment=fv_invest,
        future_value_debt=fv_debt,
        recommendation=rec,
    )


@dataclass
class RetirementCorpusInput:
    current_age: int
    retirement_age: int
    current_corpus: float
    target_monthly_expense: float
    inflation_rate: float
    pre_retirement_return: float
    post_retirement_return: float


@dataclass
class RetirementCorpusResult:
    required_corpus: float
    monthly_sip: float


def retirement_corpus_calculator(params: RetirementCorpusInput) -> RetirementCorpusResult:
    years_to_retire = params.retirement_age - params.current_age
    fv_current = formulas.future_value(
        params.current_corpus, params.pre_retirement_return, years_to_retire
    )
    inflated_expense = formulas.future_value(
        params.target_monthly_expense, params.inflation_rate, years_to_retire
    )
    required_corpus = inflated_expense * 12 / params.post_retirement_return
    gap = max(required_corpus - fv_current, 0)

    # simple SIP formula ignoring monthly compounding for brevity
    if years_to_retire * 12 == 0:
        monthly_sip = gap
    else:
        monthly_rate = params.pre_retirement_return / 12
        months = years_to_retire * 12
        monthly_sip = gap * monthly_rate / ((1 + monthly_rate) ** months - 1)

    return RetirementCorpusResult(required_corpus=required_corpus, monthly_sip=monthly_sip)
