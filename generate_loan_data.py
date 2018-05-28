import pandas as pd
import random
import zipcodes

def generate_data():
    zipcodes = [elem["zip_code"] for elem in zipcodes.list_all()]
    df = pd.DataFrame()
    for _ in range(1000):
        tmp = {}
        tmp["checking_balance"] = random.randint(1, 4)
        tmp["months_loan_duration"] = random.randint(1, 75)
        tmp["credit_history"] = random.randint(1, 5)
        tmp["purpose"] = random.randint(1, 5)
        tmp["amount"] = random.randint(1, 10000)
        tmp["savings_balance"] = random.randint(1, 5)
        tmp["employment_duration"] = random.randint(1, 5)
        tmp["percent_of_income"] = random.randint(1, 25)
        tmp["years_at_residence"] = random.randint(1, 25)
        tmp["age"] = random.randint(18, 85)
        tmp["other_credit"] = random.randint(1, 3)
        tmp["housing"] = random.randint(1, 3)
        tmp["job"] = random.randint(1, 4)
        tmp["existing_loans_count"] = random.randint(0, 3)
        tmp["dependents"] = random.randint(1, 3)
        tmp["phone"] = random.randint(1, 2)
        tmp["default"] = random.randint(1, 2)
        tmp["gender"] = random.randint(1, 2)
        tmp["status"] = random.randint(1, 3)
        tmp["zipcode"] = random.choice(zipcodes)
        tmp["race"] = random.randint(1, 4)
        df = df.append(tmp, ignore_index=True)
    return df

def map_data(df):
    map_checking_balance = {
        1: "< 0 USD",
        2:"1 - 200 USD",
        3: ">= 200 USD",
        4: "unknown"
    }
    map_credit_history = {
        1: "critical",
        2: "good",
        3: "bad",
        4: "excellent",
        5: "no credit"
    }
    map_purpose = {
        1: "business",
        2: "car",
        3: "furniture",
        4: "education",
        5: "other"
    }
    map_savings_balance = {
        1: "< 100 USD",
        2: ">1000 USD",
        3: "100 - 500 USD",
        4: "500 - 1000 USD",
        5: "unknown"
    }
    map_employment_duration = {
        1: "< 1 year",
        2: "> 7 years",
        3: "1 - 3 years",
        4: "3 - 5 years",
        5: "unknown"
    }
    map_other_credit = {
        1: "bank",
        2: "none",
        3: "stores"
    }
    map_housing = {
        1: "other",
        2: "own",
        3: "rent"
    }
    map_job = {
        1: "management",
        2: "skilled",
        3: "unskilled",
        4: "none"
    }
    map_phone = {
        1: "no",
        2: "yes"
    }
    map_default = {
        1: "no",
        2: "yes"
    }
    map_gender = {
        1: "F",
        2: "M"
    }
    map_status = {
        1: "married",
        2: "single",
        3: "divorced"
    }
    map_race = {
        1: "AA",
        2: "SA",
        3: "CA",
        4: "BA"
    }
    df["checking_balance"] = df["checking_balance"].map(map_checking_balance)
    df["credit_history"] = df["credit_history"].map(map_credit_history)
    df["purpose"] = df["purpose"].map(map_purpose)
    df["savings_balance"] = df["savings_balance"].map(map_savings_balance)
    df["employment_duration"] = df["employment_duration"].map(map_employment_duration)
    df["other_credit"] = df["other_credit"].map(map_other_credit)
    df["housing"] = df["housing"].map(map_housing)
    df["job"] = df["job"].map(map_job)
    df["phone"] = df["phone"].map(map_phone)
    df["default"] = df["default"].map(map_default)
    df["gender"] = df["gender"].map(map_gender)
    df["status"] = df["status"].map(map_status)
    df["race"] = df["race"].map(map_race)
    return df

if __name__ == '__main__':
    df = generate_data()
    df = map_data(df)
    df.to_csv("loans.csv")
