from expense_tracker import calculate_monthly_summary


def test_multiple_categories_same_month():
    transactions = [
        {"amount": 10, "category": "Food", "date": "2026-05-01"},
        {"amount": 20, "category": "Transport", "date": "2026-05-03"},
        {"amount": 30, "category": "Entertainment", "date": "2026-05-10"},
    ]

    result = calculate_monthly_summary(transactions, "2026-05")

    assert result == {
        "Food": 10,
        "Transport": 20,
        "Entertainment": 30
    }


def test_same_category_gets_added_together():
    transactions = [
        {"amount": 10, "category": "Food", "date": "2026-05-01"},
        {"amount": 15, "category": "Food", "date": "2026-05-08"},
        {"amount": 25, "category": "Food", "date": "2026-05-20"},
    ]

    result = calculate_monthly_summary(transactions, "2026-05")

    assert result == {"Food": 50}


def test_no_matching_transactions_returns_empty_dict():
    transactions = [
        {"amount": 10, "category": "Food", "date": "2026-04-01"},
        {"amount": 20, "category": "Transport", "date": "2026-04-15"},
    ]

    result = calculate_monthly_summary(transactions, "2026-05")

    assert result == {}


def test_empty_transactions_list_returns_empty_dict():
    transactions = []

    result = calculate_monthly_summary(transactions, "2026-05")

    assert result == {}

def test_transaction_list_spanning_multiple_months_counts_requested_month():
    transactions = [
        {"amount": 10, "category": "Food", "date": "2026-04-01"},
        {"amount": 20, "category": "Transport", "date": "2026-05-15"},
        {"amount": 20, "category": "Transport", "date": "2027-05-19"},
    ]
    result = calculate_monthly_summary(transactions, "2026-05")

    assert result == {"Transport": 20}


