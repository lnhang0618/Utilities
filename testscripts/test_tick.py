from sciplotlib import AcademicPlot
import numpy as np
import matplotlib.pyplot as plt

plt = AcademicPlot(figsize=(8,6),fontsize=20,show_minor_ticks=True)
plt.plot(np.random.randn(100),np.random.randn(100),marker='o')
plt.savefig("test.png")
