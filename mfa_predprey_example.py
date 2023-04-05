import numpy as np
import matplotlib.pyplot as plt

# Parameters
h = 100
inf_duration = 5
imm_duration = 5
b = 0.02
maxtime = 2000 # er worden 2000 generateis gesimuleerd
step = 50 # kleiner time steps leidt tot een grotere fps

# Initial values of infected, susceptible and recovered:
I = 333
R = 333
S = 333
# Arrays with time points and simulation outcomes
I_list = [I]
R_list = [R]
S_list = [S]
T_list = [0]

for T in range(1,maxtime):
    # Add data to data arrays:
    I += (S*(8*b*I)/(8*b*I+h) - I/inf_duration)/step # infection -recovery
    R += (I/inf_duration - R/imm_duration)/step # recovery - loss of immunity
    S += (R/imm_duration - S*(8*b*I)/(8*b*I+h))/step # loss of immunity - infection
    I_list.append(I)
    R_list.append(R)
    S_list.append(S)
    T_list.append(T)


# Plot
plt.plot(T_list, R_list, 'orange', lw = 2.0, label = 'Recovered')
plt.plot(T_list, S_list, 'green', lw = 2.0, label = 'Susceptible')
plt.plot(T_list, I_list, 'grey', label = 'Infected')
plt.legend()
plt.xlabel("Time")
plt.ylabel("State density (percentage of total)")
plt.show()

