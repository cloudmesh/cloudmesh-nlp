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



df = pd.read_csv('helloworld.log')
df.columns = ['time', 'provider', 'content', 'api']
print(df.to_string())


# sns.scatterplot(x="provider", y="time",
#                 data=df)
print(df.describe())

sns.violinplot(data=df, x="provider", y="time")

plt.savefig('helloworldbenchmark.png')
plt.savefig('helloworldbenchmark.pdf')

os.system('open helloworldbenchmark.pdf')






