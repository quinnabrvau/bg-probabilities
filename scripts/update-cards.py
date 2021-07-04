#!/usr/bin/env python3


import pandas as pd

def parse_xlsx(filename='story-book-cards.xlsx'):
    sheets = pd.read_excel(filename, sheet_name=None)
    for key in sheets:
        sheets[key].dropna(axis=1, how='all', inplace=True)
    return sheets

def parse_minions(df):
    keywords = [
        'Flying',
        'Support',
        'Slay',
        'Quest',
        'Last Breath',
        'Ranged',
    ]
    def get_keywords(text):
        out = []
        for keyword in keywords:
            if keyword in text:
                out.append(keyword)
        return ', '.join(out)

    df['Text'].fillna('', inplace=True)
    df['Gold Text'].fillna('', inplace=True)
    df['Keywords'] = df['Text'].apply(get_keywords)
    df['Alignment'].replace('Neutral','',inplace=True)
    df['Combined'] = df[['Alignment','Type','Keywords']].agg(', '.join, axis=1)
    df['Combined'] = df['Combined'].apply(lambda x : x[2:] if x.startswith(', ') else x) ## remove leading  ', '
    df['Combined'] = df['Combined'].apply(lambda x : x[:-2] if x.endswith(', ') else x)  ## remove trailing ', '
    df.rename(columns={'Cost':'Tier'}, inplace=True)
    return df

if __name__ == '__main__':
    sheets = parse_xlsx()
    # print(sheets)

    minions = sheets['Characters']
    minions = parse_minions(minions)
    print(minions)

    # for index, row in minions.iterrows():
    #     print(f"|{row['Combined']}|")

    minions.to_json('minions-sbb.json', orient='records', indent=2)