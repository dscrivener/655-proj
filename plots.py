import pandas as pd
import seaborn as sns

COLS = ['img_name', 'img_size', 'start', 'stop', 'total', 'result']
FILENAME = ""
LINK_CAPACITY = 1000000000 # 1 Gbps (verify it)
#TODO: verify that the link capacity is correct
#TODO: vefify what is the unit of the image size


df = pd.read_csv(FILENAME)

df["throughput"] = df["img_size"] / df["total"]
df["utilization"] = df["throughput"] / LINK_CAPACITY

sns.set_theme(style="whitegrid")
ax = sns.boxplot(x="img_size", y="utilization", data=df)
ax.set(xlabel='Image Size (bytes)', ylabel='Utilization')
ax.set_title('Utilization vs Image Size')
ax.figure.savefig('plots/utilization_vs_image_size.png')

ax = sns.boxplot(x="img_size", y="throughput", data=df)
ax.set(xlabel='Image Size (bytes)', ylabel='Throughput (bytes/second)')
ax.set_title('Throughput vs Image Size')
ax.figure.savefig('plots/throughput_vs_image_size.png')

ax = sns.boxplot(x="img_size", y="total", data=df)
ax.set(xlabel='Image Size (bytes)', ylabel='Total Time (seconds)')
ax.set_title('Total Time vs Image Size')
ax.figure.savefig('plots/total_time_vs_image_size.png')
