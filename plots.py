from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

sns.set(rc={'figure.figsize':(10, 10)})

COLS = ['img_name', 'img_size', 'start', 'stop', 'total', 'result']
FILENAME = "12072022153433.csv"
LINK_CAPACITY = 1000000000 # 1 Gbps
#TODO: verify that the link capacity is correct

df = pd.read_csv(FILENAME)

df["throughput"] = df["img_size"] / df["total"] # Bytes / second
df["utilization"] = (df["throughput"] / LINK_CAPACITY) * 100

sns.set_theme(style="whitegrid")
ax = sns.boxplot(x="img_size", y="utilization", data=df)
ax.set(xlabel='Image Size (bytes)', ylabel='Utilization (%)')
ax.set_title('Utilization vs Image Size')
labels = [str(eval(item.get_text()) // 100) + "K" for item in ax.get_xticklabels()]
ax.set_xticklabels(labels, rotation=45)
ax.figure.savefig('plots/utilization_vs_image_size.png', dpi=800)
plt.clf()

ax = sns.boxplot(x="img_size", y="throughput", data=df)
ax.set(xlabel='Image Size (bytes)', ylabel='Throughput (bytes/second)')
ax.set_title('Throughput vs Image Size')
labels = [str(eval(item.get_text()) // 100) + "K" for item in ax.get_xticklabels()]
ax.set_xticklabels(labels, rotation=45)
ax.figure.savefig('plots/throughput_vs_image_size.png', dpi=800)
plt.clf()

ax = sns.boxplot(x="img_size", y="total", data=df)
ax.set(xlabel='Image Size (bytes)', ylabel='Total Time (seconds)')
ax.set_title('Total Time vs Image Size')
labels = [str(eval(item.get_text()) // 100) + "K" for item in ax.get_xticklabels()]
ax.set_xticklabels(labels, rotation=45)
ax.figure.savefig('plots/total_time_vs_image_size.png', dpi=800)
plt.clf()

ax = sns.pointplot(data=df, x="img_size", y="total")
ax.set(xlabel='Image Size (bytes)', ylabel='Total Time (seconds)')
ax.set_title('Total Time vs Image Size')
labels = [str(eval(item.get_text()) // 100) + "K" for item in ax.get_xticklabels()]
ax.set_xticklabels(labels, rotation=45)
ax.figure.savefig('plots/total_time_vs_image_size_point.png', dpi=800)
plt.clf()