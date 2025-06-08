from dataclasses import dataclass
from typing import List
from .. import formulas


@dataclass
class JobOffer:
    label: str
    compensation: float
    equity_value: float = 0.0
    bonus: float = 0.0
    probability: float = 1.0


@dataclass
class JobOfferComparisonInput:
    offers: List[JobOffer]
    criteria_weights: List[float]
    criteria_scores: List[List[float]]  # matrix: offer x criterion


@dataclass
class JobOfferComparisonResult:
    weighted_scores: List[float]
    best_offer: str


def compare_job_offers(params: JobOfferComparisonInput) -> JobOfferComparisonResult:
    scores = []
    for offer_scores in params.criteria_scores:
        scores.append(formulas.weighted_score(offer_scores, params.criteria_weights))
    best_index = max(range(len(scores)), key=lambda i: scores[i])
    best_label = params.offers[best_index].label
    return JobOfferComparisonResult(weighted_scores=scores, best_offer=best_label)
