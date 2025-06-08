# Program Your Life

This repository contains an early prototype of the **Decision Support Platform** described in the project blueprint. It currently provides a minimal Python implementation with sample financial planning modules.

## Features

- Formula library with common financial calculations (future value, present value, EMI, NPV, weighted scores).
- Service functions for:
  - Investment vs. Prepayment decision
  - Retirement corpus calculator
  - Job offer comparison
- Command line interface for running the above modules.

## Usage

```
python cli.py invest_vs_prepay <debt_amount> <debt_interest_rate> <investment_amount> <expected_return_rate> <time_horizon_years>

python cli.py retirement <current_age> <retirement_age> <current_corpus> <target_monthly_expense> <inflation_rate> <pre_retirement_return> <post_retirement_return>

python cli.py job_compare offers.json
```

The JSON file should contain keys `offers`, `criteria_weights`, and `criteria_scores` as shown below:

```json
{
  "offers": [
    {"label": "OfferA", "compensation": 100000},
    {"label": "OfferB", "compensation": 120000}
  ],
  "criteria_weights": [0.5, 0.3, 0.2],
  "criteria_scores": [[8, 7, 9], [9, 6, 7]]
}
```

The CLI outputs dataclass objects with computed fields.

This is a starting point; further modules and a complete UI can be built following the blueprint.
