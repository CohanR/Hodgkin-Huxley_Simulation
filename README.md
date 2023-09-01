# Hodgkin-Huxley_Simulation
I wrote this script to demonstrate and simulate The Hodgkin-Huxley model for a group of students.You can use any IDE to run the code, but I recommend Jupyter Lab. Make sure you install the dependencies. Remy Cohan, July 2023.

# Hodgkin-Huxley Model - Action Potential Simulation

The Hodgkin-Huxley model describes how action potentials in neurons are initiated and propagated. It is a mathematical model that forms the basis for understanding many aspects of neurobiology, including the transmission of signals in the nervous system.

This Python script provides an implementation of the model, allowing for visual simulations of the neuron's action potential over time. Here are the main features and components:

# 1. Constants and Parameters:
    - Membrane parameters like `Cm`, `g_Na`, `g_K`, and `g_L` are specified.
    - Reversal potentials for sodium (`E_Na`), potassium (`E_K`), and the leak channels (`E_L`) are provided.
  
# 2. Gating Variable Functions:
    - The gating mechanisms of the ion channels are described by rate equations (alpha and beta functions) which govern the opening and closing of the channels based on the membrane potential.

# 3. Injected Current Function:
    - `I_inj(t)` provides an external stimulus to the neuron, mimicking the kind of short bursts of current that might be provided in experimental settings.

# 4. Hodgkin-Huxley Equations:
    - This function `hodgkin_huxley(y, t)` implements the system of differential equations forming the Hodgkin-Huxley model, which depicts how the neuron's membrane potential changes over time due to the flow of ions through voltage-gated channels.

# 5. Initial Conditions & Time Vector:
    - Initial conditions for the simulation, including the initial membrane potential (`V0`) and the initial values of gating variables (`n0`, `m0`, `h0`), are calculated and provided.
    - A time vector `t` is created to span the simulation duration.

# 6. Solving the Differential Equations:
    - The `odeint` function from the `scipy.integrate` module is utilized to solve the system of differential equations numerically.

# 7. Visualization and Animation:
    - A graphical representation of the action potential is dynamically visualized over time.
    - Annotations, such as the resting membrane potential and injected current indications, are added to the plot to provide contextual insights.
    - The animation is saved as a high-quality GIF for easy sharing and display.

