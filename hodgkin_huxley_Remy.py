import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint

# Constants
Cm = 1.0  # Membrane capacitance (uF/cm^2)
g_Na = 120.0  # Maximum sodium conductance (mS/cm^2)
g_K = 36.0  # Maximum potassium conductance (mS/cm^2)
g_L = 0.3  # Leak conductance (mS/cm^2)
E_Na = 50.0  # Sodium reversal potential (mV)
E_K = -77.0  # Potassium reversal potential (mV)
E_L = -54.387  # Leak reversal potential (mV)

# Gating variable functions
def alpha_n(V):
    return 0.01 * (V + 55) / (1 - np.exp(-0.1 * (V + 55)))

def beta_n(V):
    return 0.125 * np.exp(-0.0125 * (V + 65))

def alpha_m(V):
    return 0.1 * (V + 40) / (1 - np.exp(-0.1 * (V + 40)))

def beta_m(V):
    return 4 * np.exp(-0.0556 * (V + 65))

def alpha_h(V):
    return 0.07 * np.exp(-0.05 * (V + 65))

def beta_h(V):
    return 1 / (1 + np.exp(-0.1 * (V + 35)))

# Define the injected current function
def I_inj(t):
    return 10 if 5 <= t <= 45 else 0

# Hodgkin-Huxley model
def hodgkin_huxley(y, t):
    V, n, m, h = y
    dVdt = (I_inj(t) + g_Na * m**3 * h * (E_Na - V) + g_K * n**4 * (E_K - V) + g_L * (E_L - V)) / Cm
    dndt = alpha_n(V) * (1 - n) - beta_n(V) * n
    dmdt = alpha_m(V) * (1 - m) - beta_m(V) * m
    dhdt = alpha_h(V) * (1 - h) - beta_h(V) * h
    return [dVdt, dndt, dmdt, dhdt]

# Initial conditions
V0 = -65.0  # Initial membrane potential (mV)
n0 = alpha_n(V0) / (alpha_n(V0) + beta_n(V0))
m0 = alpha_m(V0) / (alpha_m(V0) + beta_m(V0))
h0 = alpha_h(V0) / (alpha_h(V0) + beta_h(V0))

y0 = [V0, n0, m0, h0]

# Time vector
t = np.linspace(0, 50, 1000)

# Solve the ODE
solution = odeint(hodgkin_huxley, y0, t)
V = solution[:, 0]

# Create the plot and set the y-axis limits
fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
ax.set_ylim(-100, 70)
ax.set_xlim(0, 50)
ax.set_xlabel('Time (ms)', fontsize=12)
ax.set_ylabel('Voltage (mV)', fontsize=12)
ax.set_title('Hodgkin-Huxley Model - Action Potential', fontsize=14)

# Add resting membrane potential line and 0 mV line
ax.axhline(y=V0, color='gray', linestyle='--', alpha=0.5, zorder=1)
ax.axhline(y=0, color='black', linestyle='-', alpha=0.5, zorder=0)

# Add injected current indication
ax.annotate('Injected current: 10 uA/cm$^2$', xy=(5, 50), xycoords='data', fontsize=10, ha='left', va='center', zorder=3)
ax.axvline(x=5, ymin=0.2, ymax=0.8, linestyle=':', color='red', alpha=0.5, zorder=3)
ax.axvline(x=45, ymin=0.2, ymax=0.8, linestyle=':', color='red', alpha=0.5, zorder=3)

# Add text as an annotation
ax.annotate("© Remy Cohan", (0.97, 0.03), xycoords='axes fraction', fontsize=10, ha='right', va='bottom', alpha=0.3, zorder=3)

# Initialize the action potential line
line, = ax.plot([], [], color='blue', linewidth=2, zorder=2)

# Animation update function
def update(frame):
    # Update the time vector to only include the frames we want to plot
    t_plot = t[:frame*10]
    V_plot = V[:frame*10]
    line.set_data(t_plot, V_plot)
    return line,

# Create the animation with a faster frame rate
animation = FuncAnimation(fig, update, frames=len(t)//10, interval=5, blit=True)

# Save the animation as a GIF with a higher DPI and faster speed
animation.save('hodgkin_huxley_Remy_Cohan.gif', writer='pillow', fps=60, dpi=200)

