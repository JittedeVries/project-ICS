

import numpy as np
import matplotlib.pyplot as plt

# Parameters

import numpy as np
import matplotlib.pyplot as plt

# Parameters
h = 10000
inf_duration1 = 2
inf_duration2 = 2.5
imm_duration = 5
b = 2
maxtime = 1000

# Initial values of infected, susceptible and recovered:
I1 = 1000
I2 = 1000
R = 1000
S = 1000
total = I1+I2+R+S
step = 100
# Arrays with time points and simulation outcomes
I1_list = [I1/total]
I2_list = [I2/total]
R_list = [R/total]
S_list = [S/total]
T_list = [0]

for T in range(maxtime):
    # Add data to data arrays:
    I1 += (S*(8*b*I1)/(8*b*I1+h) - I1/inf_duration1)/step 
    I2 += (S*(8*b*I2)/(8*b*I2+h) - I2/inf_duration2)/step
    R += (I1/inf_duration1 + I2/inf_duration2 - R/imm_duration)/step
    S += (R/imm_duration - S*(8*b*I1)/(8*b*I1+h) - S*(8*b*I2)/(8*b*I2+h))/step  
    I1_list.append(I1/total)
    I2_list.append(I2/total)
    R_list.append(R/total)
    S_list.append(S/total)
    T_list.append(T)


# Plot
plt.plot(T_list, R_list, 'orange', label = 'Recovered')
plt.plot(T_list, S_list, 'green', label = 'Susceptible')
plt.plot(T_list, I1_list, 'red', label = 'Infected1 (normal pathogen)')
plt.plot(T_list, I2_list, 'grey', label = 'Infected2 (mutated pathogen)')
plt.legend()
plt.xlabel("Time")
plt.ylabel("State fraction")
plt.show()

