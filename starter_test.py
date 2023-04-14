# test_friend.py

# assert expression
## if true nothing happens
## if false raises AssertionError

# create virtual environment and activate
# pip install pytest
# pip install pytest-cov

# run tests with python -m pytest -s
# compare -s and -v when running the tests
# run coverage tests with python -m pytest --cov

import pytest
from oop_loan_pmt import *


# Unit Tests
def test_loan_discount_factor():
    """
    GIVEN a user enters their loan details
    WHEN the loan object's calculateDiscountFactor method is called
    THEN the discount factor is accurately calculated
    """
    loan = Loan(loanAmount=100000, numberYears=30, annualRate=0.06)
    loan.calculateDiscountFactor()
    print("\r")
    print(" -- calculateDiscountFactor method unit test")
    assert loan.getDiscountFactor() == pytest.approx(
        166.79, rel=1e-3
    )  # approx two decimal places


def test_loan_payment():
    """
    GIVEN a user enters their loan details
    WHEN the loan object's calculateLoanPmt method is called
    THEN the loan payment is accurately calculated
    """
    loan = Loan(loanAmount=100000, numberYears=30, annualRate=0.06)
    loan.calculateLoanPmt()
    print("\r")
    print(" -- calculateLoanPmt method unit test")
    assert loan.getLoanPmt() == pytest.approx(
        599.55, rel=1e-3
    )  # approx two decimal places
    
# Functional Tests
def test_loan_payment_calculation():
    # GIVEN
    loan_amount = 100000
    number_years = 30
    annual_rate = 0.06
    expected_loan_payment = 599.55

    # WHEN
    loan = Loan(loanAmount=loan_amount, numberYears=number_years, annualRate=annual_rate)
    loan.calculateLoanPmt()
    actual_loan_payment = loan.getLoanPmt()
    print("\r")
    print(" -- calculate loan functional test")
    # THEN
    assert actual_loan_payment == pytest.approx(expected_loan_payment, rel=1e-3)
   