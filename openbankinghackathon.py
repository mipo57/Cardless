import json
import pandas as pd
from pandas.io.json import json_normalize


def decoding_get_transactions():
    pd.set_option('display.max_columns', 500)

    with open("json_example", "r") as read_file:
        dict = json.load(read_file)
        transactions = dict['transactions']
        print(transactions)
        df = pd.DataFrame(transactions)
        df = pd.concat([df.drop(['auxData'], axis=1), df['auxData'].apply(pd.Series).add_suffix('_auxData')], axis=1)
        df = pd.concat([df.drop(['transactionStatus'], axis=1), df['transactionStatus'].apply(pd.Series).add_suffix('_transactionStatus')], axis=1)
        df = pd.concat([df.drop(['initiator'], axis=1), df['initiator'].apply(pd.Series).add_suffix('_initiator')], axis=1)
        df = pd.concat([df.drop(['sender'], axis=1), df['sender'].apply(pd.Series).add_suffix('_sender')], axis=1)
        df = pd.concat([df.drop(['recipient'], axis=1), df['recipient'].apply(pd.Series).add_suffix('_recipient')], axis=1)
        df = pd.concat([df.drop(['bank_sender'], axis=1), df['bank_sender'].apply(pd.Series).add_suffix('_bank_sender')], axis=1)
        print(df.iloc[0])


def mcc_intervals2(mcc: str):
    mcc = int(mcc)
    category = 'unknown'
    with open("json_mcc_grouping", "r") as read_file:
        dict = json.load(read_file)
        df = pd.io.json.json_normalize(dict)
        df['from'] = df['from'].astype(int)
        df['to'] = df['to'].astype(int)

        print(df.dtypes)
        for idx, row in df.iterrows():
            if row['from'] < mcc < row['to']:
                category = row['name']
        return category


print(mcc_intervals2('1000'))