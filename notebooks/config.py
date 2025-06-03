
import pandas as pd
import os

def load_client_data(path, filename, dtypes):
    df = pd.read_csv(os.path.join(path, filename), dtype=dtypes)
    return df

dtypes_clientes = {
    'CLIENT_ID': 'object',
    'NON_COMPLIANT_CONTRACT': 'int64',
    'NAME_PRODUCT_TYPE': 'object',
    'GENDER': 'object',
    'TOTAL_INCOME': 'float64',
    'AMOUNT_PRODUCT': 'float64',
    'INSTALLMENT': 'float64',
    'EDUCATION': 'object',
    'MARITAL_STATUS': 'object',
    'HOME_SITUATION': 'object',
    'REGION_SCORE': 'float64',
    'AGE_IN_YEARS': 'float64',
    'JOB_SENIORITY': 'float64',
    'HOME_SENIORITY': 'float64',
    'LAST_UPDATE': 'float64',
    'OWN_INSURANCE_CAR': 'object',
    'CAR_AGE': 'float64',
    'FAMILY_SIZE': 'float64',
    'REACTIVE_SCORING': 'float64',
    'PROACTIVE_SCORING': 'float64',
    'BEHAVIORAL_SCORING': 'float64',
    'DAYS_LAST_INFO_CHANGE': 'float64',
    'NUMBER_OF_PRODUCTS': 'float64',
    'OCCUPATION': 'object',
    'DIGITAL_CLIENT': 'int64',
    'HOME_OWNER': 'object',
    'EMPLOYER_ORGANIZATION_TYPE': 'object',
    'CURRENCY': 'object',
    'NUM_PREVIOUS_LOAN_APP': 'float64',
    'LOAN_ANNUITY_PAYMENT_MAX': 'float64',
    'LOAN_ANNUITY_PAYMENT_MIN': 'float64',
    'LOAN_ANNUITY_PAYMENT_SUM': 'float64',
    'LOAN_APPLICATION_AMOUNT_MAX': 'float64',
    'LOAN_APPLICATION_AMOUNT_MIN': 'float64',
    'LOAN_APPLICATION_AMOUNT_SUM': 'float64',
    'LOAN_CREDIT_GRANTED_MAX': 'float64',
    'LOAN_CREDIT_GRANTED_MIN': 'float64',
    'LOAN_CREDIT_GRANTED_SUM': 'float64',
    'LOAN_VARIABLE_RATE_MAX': 'float64',
    'LOAN_VARIABLE_RATE_MIN': 'float64',
    'NUM_STATUS_ANNULLED': 'float64',
    'NUM_STATUS_AUTHORIZED': 'float64',
    'NUM_STATUS_DENIED': 'float64',
    'NUM_STATUS_NOT_USED': 'float64',
    'NUM_FLAG_INSURED': 'float64'
}

dtypes_comportamiento = {
    "CLIENT_ID": 'object',
    "CONTRACT_ID": 'object',
    "CURRENCY": 'object',
    "CREDIT_CARD_BALANCE": 'float64',
    "CREDIT_CARD_LIMIT": 'float64',
    "CREDIT_CARD_DRAWINGS_ATM": 'float64',
    "CREDIT_CARD_DRAWINGS_POS": 'float64',
    "CREDIT_CARD_DRAWINGS_OTHER": 'float64',
    "CREDIT_CARD_DRAWINGS": 'float64',
    "CREDIT_CARD_PAYMENT": 'float64',
    "NUMBER_DRAWINGS_ATM": 'int64',
    "NUMBER_DRAWINGS": 'int64',
    "NUMBER_INSTALMENTS": 'float64'
}