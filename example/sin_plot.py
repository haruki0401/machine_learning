import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,100)
y = np.sin(x)
plt.plot(x,y)
plt.savefig('sin_curve.png')
