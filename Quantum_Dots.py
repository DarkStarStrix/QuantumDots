# Import QuTiP library
from qutip import *
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio


def calculate_probabilities(N, tlist):
    """Calculate the probabilities of the energy levels of a quantum dot system."""
    # Check if N is a positive integer
    if not isinstance (N, int) or N <= 0:
        raise ValueError ("N must be a positive integer")

    # Define the Hamiltonian of the quantum dot
    H = 0.5 * 2 * np.pi * qeye (N)  # Identity operator in N-dimensional Hilbert space

    # Define the initial state of the quantum dot
    psi0 = basis (N, 0)

    # Solve the Schrödinger equation
    result = sesolve (H, psi0, tlist)

    # Create a 3D array to store the probabilities at each time step
    probabilities = np.zeros ((len (tlist), N, N))

    # Calculate the probabilities at each time step
    for i, state in enumerate (result.states):
        probabilities [i] = np.abs (state.full ()) ** 2

    return probabilities


def create_plot(probabilities):
    """Create a 3D surface plot of the probabilities."""
    fig = go.Figure(data=[go.Surface(z=probabilities[0], name='Probabilities')])

    fig.update_traces(showscale=True)  # Shows color scale

    fig.update_layout(
        title="Quantum Dot",
        scene=dict(
            xaxis_title="Energy Level",
            yaxis_title="Energy Level",
            zaxis_title="Probability",
        ),
        autosize=False,
        width=800,
        height=800,
        margin=dict(l=65, r=50, b=65, t=90),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )
    fig.show()


# Define the number of energy levels
N = 5

# Define the time range and steps
tlist = np.linspace(0, 20, 200)  # time range extended to 20

# Calculate the probabilities
probabilities = calculate_probabilities(N, tlist)

# Create the plot
create_plot(probabilities)
