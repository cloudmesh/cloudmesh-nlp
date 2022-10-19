import numpy as np
from tabulate import tabulate
from cloudmesh.common.util import readfile
from cloudmesh.common.Shell import Shell
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

# aws cli
# aws api
# aws requests
#
# aws cli
# ibm cli
# google cli
# azure cli
# read all log files from results and put in df
# the df has the following columns
# ['node', 'user', 'text', 'time', 'provider', 'api']
# return me all the rows where ...
# aws cli example
# give me all the rows where the value of the column provider == 'aws'
# and all the rows where the api == 'cli'

list_of_dataframes = []
for filename in os.listdir('../results/'):
    # assert 'benchmarks' in os.getcwd()

    filepath = Shell.map_filename(f'../results/{filename}').path
    current_log = readfile(filepath)

    csv_lines = []
    for line in current_log.splitlines():
        if line.startswith("#"):
            csv_lines.append(line)
    csv_string = "\n".join(csv_lines)
    csv_string = csv_string.replace("# csv,", "")
    df = pd.DataFrame([x.split(',') for x in csv_string.split('\n')])
    headers = df.iloc[0].values
    df.columns = headers
    df.drop(index=0, axis=0, inplace=True)
    for column_name in ['Status', 'msg']:
        try:
            df.drop(column_name, axis=1, inplace=True)
        except KeyError:
            pass
    try:
        df.drop(list(df.filter(regex = 'None')), axis = 1, inplace = True)
    except KeyError:
        pass

    df["provider"] = np.nan
    count = 0
    for cell in df["timer"]:
        count += 1
        # looking for providers with dash in them like aws-cli
        if "-" not in cell:
            df.at[count, "provider"] = np.nan
            continue
        current_provider = cell.split("-")[0] + "-" + cell.split("-")[-1]
        df.at[count, "provider"] = current_provider
    df = df[df['provider'].notna()]
    print(tabulate(df, headers='keys', tablefmt='psql'))

    #print(df.to_string())
    #df.columns = ['time', 'provider', 'content', 'api']
    #print(df.to_string())
    #list_of_dataframes.append(df)


# sns.scatterplot(x="provider", y="time",
#                 data=df)
print(df.describe())

stats_df = pd.DataFrame
list_of_providers = list(df['provider'].unique())
count = 0
for iterated_provider in list_of_providers:
    count += 1
    df_new = pd.DataFrame
    df_new = df.loc[df['provider'] == iterated_provider]
    to_drop = ['sum', 'start', 'tag', 'uname.node', 'user',
               'uname.system', 'platform.system', 'status',
               'platform.version', 'timer']
    for dropping_column in to_drop:
        df_new.drop(list(df_new.filter(regex=f'{dropping_column}')), axis=1, inplace=True)
    df_new_new = df_new.explode('time')
    df_new_new['time'] = df_new_new['time'].astype('float')
    df_new_new.rename(columns={'time': iterated_provider}, inplace=True)
    df_new_new.drop('provider', axis=1, inplace=True)
    df_to_add = df_new_new.describe(include='all')
    if count == 1:
        stats_df = df_to_add
    else:
        stats_df = pd.concat([stats_df, df_to_add],
                         axis=1)
stats_df = stats_df.sort_values(by='mean', axis=1)

print(stats_df)
print(stats_df.style.to_latex())
print(stats_df.to_markdown())
exploded = df.explode('time')
exploded['time'] = exploded['time'].astype('float')

ax = sns.violinplot(data=exploded, x="provider", y="time")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()

plt.savefig('helloworldbenchmark.png')
plt.savefig('helloworldbenchmark.pdf')

#os.system('open helloworldbenchmark.pdf')
Shell.browser('helloworldbenchmark.pdf')