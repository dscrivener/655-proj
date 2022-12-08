import os
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

sns.set(rc={'figure.figsize':(10, 10)})

COLS = ['img_name', 'img_size', 'start', 'stop', 'total', 'result']
FILENAME = "experiment_150_3_1000kbps.csv"
LINK_CAPACITY = 1000 # 1000 Kbps
#TODO: verify that the link capacity is correct
FOLDER = "plots/" + FILENAME.split(".")[0]

try:
    os.mkdir(FOLDER)
except:
    pass

df = pd.read_csv(FILENAME)

df["img_size"] = df["img_size"] * 8 # bits

df["throughput"] = df["img_size"] / df["total"] # bits / second
df["utilization"] = (df["throughput"] / LINK_CAPACITY) * 100

sns.set_theme(style="whitegrid")
ax = sns.boxplot(x="img_size", y="utilization", data=df)
ax.set(xlabel='Image Size (bits)', ylabel='Utilization (%)')
ax.set_title('Utilization vs Image Size')
labels = [str(eval(item.get_text()) // 100) + "Kb" for item in ax.get_xticklabels()]
ax.set_xticklabels(labels, rotation=45)
ax.figure.savefig('{}/utilization_vs_image_size.png'.format(FOLDER), dpi=800)
plt.clf()

ax = sns.boxplot(x="img_size", y="throughput", data=df)
ax.set(xlabel='Image Size (bits)', ylabel='Throughput (bytes/second)')
ax.set_title('Throughput vs Image Size')
labels = [str(eval(item.get_text()) // 100) + "Kb" for item in ax.get_xticklabels()]
ax.set_xticklabels(labels, rotation=45)
ax.figure.savefig('{}/throughput_vs_image_size.png'.format(FOLDER), dpi=800)
plt.clf()

ax = sns.boxplot(x="img_size", y="total", data=df)
ax.set(xlabel='Image Size (bits)', ylabel='Total Time (seconds)')
ax.set_title('Total Time vs Image Size')
labels = [str(eval(item.get_text()) // 100) + "Kb" for item in ax.get_xticklabels()]
ax.set_xticklabels(labels, rotation=45)
ax.figure.savefig('{}/total_time_vs_image_size.png'.format(FOLDER), dpi=800)
plt.clf()

ax = sns.pointplot(data=df, x="img_size", y="total")
ax.set(xlabel='Image Size (bits)', ylabel='Total Time (seconds)')
ax.set_title('Total Time vs Image Size')
labels = [str(eval(item.get_text()) // 100) + "Kb" for item in ax.get_xticklabels()]
ax.set_xticklabels(labels, rotation=45)
ax.figure.savefig('{}/total_time_vs_image_size_point.png'.format(FOLDER), dpi=800)
plt.clf()