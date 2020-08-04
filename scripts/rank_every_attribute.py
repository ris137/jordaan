import pandas as pd
import json


def rank_every_attribute(**kwargs):
    if 'data' not in kwargs.keys():
        pl_data = pd.read_csv(kwargs['data_path'])
    else:
        pl_data = kwargs['data']

    abbvs = json.load(open(r'C:\Users\risha\PycharmProjects\jordaan\data\abbreviations.json'))
    abbvs = {value: key for key, value in abbvs.items()}

    pl_data['Label'] = pl_data['Squad'].apply(lambda x: abbvs[x])
    # pl_data['%Prod'] = pl_data['Prog'] / pl_data['Cmp']
    if 'club_label' in kwargs.keys():
        club = kwargs['club_label']
        label_column = 'Label'
    else:
        club = kwargs['club_name']
        label_column = 'Squad'
    for a in pl_data.columns:
        pl_data['Rank'] = pl_data[a].rank(method='min',
                                          ascending=False)
        print('Rank {} in {} = {}'.format(pl_data.Rank[pl_data[label_column] == club][0],
                                          a,
                                          pl_data[a][pl_data[label_column] == club][0]))
