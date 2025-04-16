
import matplotlib.pyplot as plt
import numpy as np

def brownian_motion(NbScenarios, k):
    np.random.seed(10)
    M = np.zeros((k + 1, NbScenarios + 1))
    for omega in range(1, NbScenarios + 1):
        M[0][omega] = 0
        for j in range(1, k + 1):
            U = np.random.uniform()
            X = -1 if U < 1/2 else 1
            M[j][omega] = M[j - 1][omega] + np.random.normal()
    return M


scenarios_and_times = [
    (50, 50),
    (50, 100),
    (5000, 50),
    (5000,100)
]


for scenario_data in scenarios_and_times:
    if len(scenario_data) == 2:
      NbScenarios, k = scenario_data
      M = brownian_motion(NbScenarios,k)
      Mk = M[k, :]
      plt.hist(Mk, bins=15)
      plt.title(f'Histogram of Mk for {NbScenarios} scenarios and k={k}')
      plt.show()
      print('mean Mk', np.mean(Mk),'for k=',k)
      print('var Mk',  np.var(Mk),'for k=', k)

      # Brownian motion
      n = 2
      Wn = np.sqrt(1/n) * M
      t = 5
      if t <= k:
          Wn_at_t = Wn[t, :]  # Extract values at time t
          plt.hist(Wn_at_t, bins=15)  # Create histogram
          plt.title(f'Brownian Motion at t={t} for {NbScenarios} scenarios and k={k}')  # Add title
          plt.show()
      else:
          print(f"Time t={t} exceeds the simulation time k={k}.")
    else:
        print("Invalid input")

