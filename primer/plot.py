import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

#Orkut
data = np.array([[48,40460.5,37782.28125],
[96,45612.875,41508.5],
[192,46895.25,41848.21875],
[384,56953.5,51466.23333],
[480,71815.66667,63733.57895]]);


#1mil random-er
# data = np.array([[24, 9640.952381, 8280.539683],
#                  [120, 8798.5, 6684.5],
#                  [240, 8843.5, 6615.809524],
#                  [360, 10101, 6725.451613],
#                  [480, 8215, 5736.560976]])

plot_lines = [data[:, 1] * 60, data[:, 2] * 60]
k = data[:, 0]
legend = ['Max Time', 'Avg Time']
plt.figure(figsize=(6,3))
styles = ['-o', '-o', '--o', '--o', '--o', '--o']
for ind, line in enumerate(plot_lines):
    plt.semilogy(k, line, styles[ind], label=legend[ind])
plt.legend(loc='best')
plt.xlabel('Total parallel units')
plt.ylabel('\n'.join(wrap('Time per iteration (log scale) ms',20)))
# plt.title('Scalability of Graph Scan Statistics Algorithms')
plt.tight_layout()

plt.rcParams.update({'font.size': 14})
plt.rcParams.update({'lines.linewidth': 2})
plt.rcParams.update({'legend.fontsize': 12})

plt.savefig('fig-orkut-timeperiteration.pdf')
