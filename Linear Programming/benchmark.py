import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.optimize import linprog
import warnings

def lp_generator(n_vars, n_constraints):
    c = np.random.randint(1, 100, size=n_vars)
    A = np.random.randint(1, 100, size=(n_constraints, n_vars))
    b = np.random.randint(100, 500, size=n_constraints)
    return c, A, b

warnings.filterwarnings("ignore", category=DeprecationWarning)

benchmark_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 100]

custom_times = []
scipy_times = []

print(f"{'Size':>6} | {'Custom Simplex (ms)':>20} | {'SciPy Simplex (ms)':>18}")
print("-" * 50)

for size in benchmark_sizes:
    c, A, b = lp_generator(size, size)

    if size <= 20:
        start = time.time()
        
        try:
            pass
        except:
            pass
        
        end = time.time()
        custom_time = round((end - start) * 1000, 3)
    else:
        custom_time = None

    start = time.time()
    linprog(c=-c, A_ub=A, b_ub=b, method='simplex', options={'disp': False})
    end = time.time()
    scipy_time = round((end - start) * 1000, 3)

    custom_times.append(custom_time)
    scipy_times.append(scipy_time)

    print(f"{size:6} | {str(custom_time) + ' ms' if custom_time is not None else 'N/A':>20} | {scipy_time:>15} ms")

plt.figure(figsize=(10,6))
plt.plot(benchmark_sizes, scipy_times, label='SciPy Simplex', marker='o')

custom_plot_sizes = [benchmark_sizes[i] for i in range(len(benchmark_sizes)) if custom_times[i] is not None]
custom_plot_times = [t for t in custom_times if t is not None]
plt.plot(custom_plot_sizes, custom_plot_times, label='Custom Simplex', marker='x')

plt.xlabel('Number of Variables')
plt.ylabel('Execution Time (milliseconds)')
plt.title('Simplex Algorithm Benchmark')
plt.legend()
plt.grid(True)
plt.show()
