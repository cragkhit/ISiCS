from matplotlib import pyplot as plt
import numpy as np
import matplotlib

# Index time plot

methods = [22, 50, 178, 423, 1723, 6601, 28030, 111190, 442403, 1771183]
siamese = [4.13, 2.95, 4.62, 8.4, 11.94, 36.22, 172.90, 614.90, 2077.04, 9089]
scc = [(0.58 + 2.03), (0.88 + 0.68), (2.68 + 0.98), (3.81 + 1.37), (9.18 + 2.15), (28.40 + 4.96),
       (110.09 + 16.78), (432.52 + 60.96), (1694.23 + 219.8), (6786 + 870.08)]
# seconds
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(methods, siamese, c="b", marker="s", label="Siamese")
ax.plot(methods, scc, c="r", marker="x", label="SourcererCC")
plt.xscale('log', basex=2)
plt.xlabel("No. of methods")
plt.ylabel("Indexing time (s)")
plt.ylim(ymax=10000)
plt.legend(loc=2)
plt.show()

fig = ax.get_figure()
fig.savefig('index.pdf', bbox_inches='tight')

# minutes
siamese_m = [x / 60 for x in siamese]
scc_m = [x / 60 for x in scc]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(methods, siamese_m, c="b", marker="s", label="Siamese")
ax.plot(methods, scc_m, c="r", marker="x", label="SourcererCC")
plt.xscale('log', basex=10)
plt.xlabel("No. of methods")
plt.ylabel("Indexing time (m)")
plt.ylim(ymax=160)
plt.legend(loc=2)
plt.show()

fig = ax.get_figure()
fig.savefig('index_m.pdf', bbox_inches='tight')


# Query time plot

methods = [22, 50, 178, 423, 1723, 6601, 28030, 111190, 442403, 1771183]
siamese = [1.539, 1.5405, 1.5526, 1.5244, 1.5818, 1.6382, 1.71, 1.8626, 1.9711, 2.3409]
scc = [1.3006, 1.3773, 1.3937, 1.3412, 1.4536, 1.4913, 2.0718, 3.3621, 9.2613, 28.3169]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(methods, siamese, c="b", marker="s", label="Siamese")
ax.plot(methods, scc, c="r", marker="x", label="SourcererCC")
plt.xscale('log', basex=2)
plt.xlabel("No. of methods in the index")
plt.ylabel("Average query response time (s)")
plt.legend(loc=2)
plt.show()

fig = ax.get_figure()
fig.savefig('query.pdf', bbox_inches='tight')