# =========================================
# NEWTON-RAPHSON METHOD
# =========================================

# USER INPUTS
x = 0.0                 # Initial guess
tolerance = 1e-6        # Convergence tolerance
max_iterations = 100    # Maximum iterations


# DEFINE FUNCTIONS
def f(x):
    return ...          # Enter f(x) = 0


def df(x):
    return ...          # Enter derivative f'(x)


# NEWTON-RAPHSON METHOD
for i in range(1, max_iterations + 1):

    fx = f(x)
    dfx = df(x)

    # Check derivative
    if abs(dfx) < 1e-12:
        print("Error: Derivative is approximately zero.")
        break

    # Newton-Raphson equation
    x_new = x - fx / dfx

    # Display results
    print(f"Iteration {i}: x = {x_new:.8f}")

    # Check convergence
    if abs(x_new - x) < tolerance:
        print(f"\nConverged: x = {x_new:.8f}")
        break

    # Update solution
    x = x_new

    # Manual iteration
    input("Press Enter to continue...")

else:
    print("Maximum iterations reached without convergence.")