import argparse
from decision_engine.services.financial import (
    InvestmentVsPrepaymentInput,
    compute_investment_vs_prepayment,
    RetirementCorpusInput,
    retirement_corpus_calculator,
)
from decision_engine.services.career import (
    JobOffer,
    JobOfferComparisonInput,
    compare_job_offers,
)


def main():
    parser = argparse.ArgumentParser(description="Decision Support Platform CLI")
    subparsers = parser.add_subparsers(dest="command")

    invest_parser = subparsers.add_parser("invest_vs_prepay")
    invest_parser.add_argument("debt_amount", type=float)
    invest_parser.add_argument("debt_interest_rate", type=float)
    invest_parser.add_argument("investment_amount", type=float)
    invest_parser.add_argument("expected_return_rate", type=float)
    invest_parser.add_argument("time_horizon_years", type=int)

    retire_parser = subparsers.add_parser("retirement")
    retire_parser.add_argument("current_age", type=int)
    retire_parser.add_argument("retirement_age", type=int)
    retire_parser.add_argument("current_corpus", type=float)
    retire_parser.add_argument("target_monthly_expense", type=float)
    retire_parser.add_argument("inflation_rate", type=float)
    retire_parser.add_argument("pre_retirement_return", type=float)
    retire_parser.add_argument("post_retirement_return", type=float)

    job_parser = subparsers.add_parser("job_compare")
    job_parser.add_argument("json_file", help="Path to JSON file with offers and scores")

    args = parser.parse_args()

    if args.command == "invest_vs_prepay":
        inp = InvestmentVsPrepaymentInput(
            debt_amount=args.debt_amount,
            debt_interest_rate=args.debt_interest_rate,
            investment_amount=args.investment_amount,
            expected_return_rate=args.expected_return_rate,
            time_horizon_years=args.time_horizon_years,
        )
        res = compute_investment_vs_prepayment(inp)
        print(res)
    elif args.command == "retirement":
        inp = RetirementCorpusInput(
            current_age=args.current_age,
            retirement_age=args.retirement_age,
            current_corpus=args.current_corpus,
            target_monthly_expense=args.target_monthly_expense,
            inflation_rate=args.inflation_rate,
            pre_retirement_return=args.pre_retirement_return,
            post_retirement_return=args.post_retirement_return,
        )
        res = retirement_corpus_calculator(inp)
        print(res)
    elif args.command == "job_compare":
        import json

        with open(args.json_file) as f:
            data = json.load(f)
        offers = [JobOffer(**o) for o in data["offers"]]
        inp = JobOfferComparisonInput(
            offers=offers,
            criteria_weights=data["criteria_weights"],
            criteria_scores=data["criteria_scores"],
        )
        res = compare_job_offers(inp)
        print(res)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
