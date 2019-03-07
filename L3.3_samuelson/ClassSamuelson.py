#!/usr/bin/env python3  
# -*- coding:utf-8 _*-  
# Author: Wengs
# Time  : 3/6/2019 10:58 PM 
# File  : ClassSamuelson.py 
# IDE   : PyCharm

import numpy as np
import matplotlib.pyplot as plt


class Samuelson:

    r"""This class represents the Samuelson model, otherwise known as the
    multiple-accelerator model. The model combines the Keynesian multiplier
    with the accelerator theory of investment.

    The path of output is governed by a linear second-order difference equation

    .. math::

        Y_t =  + \alpha (1 + \beta) Y_{t-1} - \alpha \beta Y_{t-2}

    Parameters
    ----------
    y_0 : scalar
        Initial condition for Y_0
    y_1 : scalar
        Initial condition for Y_1
    α : scalar
        Marginal propensity to consume
    β : scalar
        Accelerator coefficient
    n : int
        Number of iterations
    σ : scalar
        Volatility parameter. Must be greater than or equal to 0. Set
        equal to 0 for non-stochastic model.
    g : scalar
        Government spending shock
    g_t : int
        Time at which government spending shock occurs. Must be specified
        when duration != None.
    duration : {None, 'permanent', 'one-off'}
        Specifies type of government spending shock. If none, government
        spending equal to g for all t.

    """

    def __init__(self,
                 y_0=100,
                 y_1=50,
                 α=1.3,
                 β=0.2,
                 γ=10,
                 n=100,
                 σ=0,
                 g=0,
                 g_t=0,
                 duration=None):

        self.y_0, self.y_1, self.α, self.β = y_0, y_1, α, β
        self.n, self.g, self.g_t, self.duration = n, g, g_t, duration
        self.γ, self.σ = γ, σ
        self.ρ1 = α + β
        self.ρ2 = -β
        self.roots = np.roots([1, -self.ρ1, -self.ρ2])

    def root_type(self):
        if all(isinstance(root, complex) for root in self.roots):
            return 'Complex conjugate'
        elif len(self.roots) > 1:
            return 'Double real'
        else:
            return 'Single real'

    def root_less_than_one(self):
        if all(abs(root) < 1 for root in self.roots):
            return True

    def solution_type(self):
        ρ1, ρ2 = self.ρ1, self.ρ2
        discriminant = ρ1 ** 2 + 4 * ρ2
        if ρ2 >= 1 + ρ1 or ρ2 <= -1:
            return 'Explosive oscillations'
        elif ρ1 + ρ2 >= 1:
            return 'Explosive growth'
        elif discriminant < 0:
            return 'Damped oscillations'
        else:
            return 'Steady state'

    def _transition(self, x, t, g):

        # Non-stochastic - separated to avoid generating random series when not needed
        if self.σ == 0:
            return self.ρ1 * x[t - 1] + self.ρ2 * x[t - 2] + self.γ + g

        # Stochastic
        else:
            ϵ = np.random.normal(0, 1, self.n)
            return self.ρ1 * x[t - 1] + self.ρ2 * x[t - 2] + self.γ + g + self.σ * ϵ[t]

    def generate_series(self):

        # Create list and set initial conditions
        y_t = [self.y_0, self.y_1]

        # Generate y_t series
        for t in range(2, self.n):

            # No government spending
            if self.g == 0:
                y_t.append(self._transition(y_t, t))

            # Government spending (no shock)
            elif self.g != 0 and self.duration == None:
                y_t.append(self._transition(y_t, t))

            # Permanent government spending shock
            elif self.duration == 'permanent':
                if t < self.g_t:
                    y_t.append(self._transition(y_t, t, g=0))
                else:
                    y_t.append(self._transition(y_t, t, g=self.g))

            # One-off government spending shock
            elif self.duration == 'one-off':
                if t == self.g_t:
                    y_t.append(self._transition(y_t, t, g=self.g))
                else:
                    y_t.append(self._transition(y_t, t, g=0))
        return y_t

    def summary(self):
        print('Summary\n' + '-' * 50)
        print(f'Root type: {self.root_type()}')
        print(f'Solution type: {self.solution_type()}')
        print(f'Roots: {str(self.roots)}')

        if self.root_less_than_one() == True:
            print('Absolute value of roots is less than one')
        else:
            print('Absolute value of roots is not less than one')

        if self.σ > 0:
            print('Stochastic series with σ = ' + str(self.σ))
        else:
            print('Non-stochastic series')

        if self.g != 0:
            print('Government spending equal to ' + str(self.g))

        if self.duration != None:
            print(self.duration.capitalize() +
                  ' government spending shock at t = ' + str(self.g_t))

    def plot(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(self.generate_series())
        ax.set(xlabel='Iteration', xlim=(0, self.n))
        ax.set_ylabel('$Y_t$', rotation=0)
        ax.grid()

        # Add parameter values to plot
        paramstr = f'$\\alpha={self.α:.2f}$ \n $\\beta={self.β:.2f}$ \n $\\gamma={self.γ:.2f}$ \n \
$\\sigma={self.σ:.2f}$ \n $\\rho_1={self.ρ1:.2f}$ \n $\\rho_2={self.ρ2:.2f}$'
        props = dict(fc='white', pad=10, alpha=0.5)
        ax.text(0.87, 0.05, paramstr, transform=ax.transAxes,
                fontsize=12, bbox=props, va='bottom')

        return fig
    """
    # This is the version of param_plot in ClassSamuelson, but it cannot work in here.
    # So, I use the earlier version of this function and it works very well.
    def param_plot(self):

        # Uses the param_plot() function defined earlier (it is then able
        # to be used standalone or as part of the model)

        fig = param_plot()
        ax = fig.gca()

        # Add λ values to legend
        for i, root in enumerate(self.roots):
            if isinstance(root, complex):
                operator = ['+', '']  # Need to fill operator for positive as string is split apart
                label = rf'$\lambda_{i+1} = {sam.roots[i].real:.2f} {operator[i]} {sam.roots[i].imag:.2f}i$'
            else:
                label = rf'$\lambda_{i+1} = {sam.roots[i].real:.2f}$'
            ax.scatter(0, 0, 0, label=label) # dummy to add to legend

        # Add ρ pair to plot
        ax.scatter(self.ρ1, self.ρ2, 100, 'red', '+', label=r'$(\ \rho_1, \ \rho_2 \ )$', zorder=5)

        plt.legend(fontsize=12, loc=3)

        return fig
    """
    # Earlier version of this function
    def param_plot(self):

        """this function creates the graph on page 189 of Sargent Macroeconomic Theory, second edition, 1987"""

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_aspect('equal')

        # Set axis
        xmin, ymin = -3, -2
        xmax, ymax = -xmin, -ymin
        plt.axis([xmin, xmax, ymin, ymax])

        # Set axis labels
        ax.set(xticks=[], yticks=[])
        ax.set_xlabel(r'$\rho_2$', fontsize=16)
        ax.xaxis.set_label_position('top')
        ax.set_ylabel(r'$\rho_1$', rotation=0, fontsize=16)
        ax.yaxis.set_label_position('right')

        # Draw (t1, t2) points
        ρ1 = np.linspace(-2, 2, 100)
        ax.plot(ρ1, -abs(ρ1) + 1, c='black')
        ax.plot(ρ1, np.ones_like(ρ1) * -1, c='black')
        ax.plot(ρ1, -(ρ1 ** 2 / 4), c='black')

        # Turn normal axes off
        for spine in ['left', 'bottom', 'top', 'right']:
            ax.spines[spine].set_visible(False)

        # Add arrows to represent axes
        axes_arrows = {'arrowstyle': '<|-|>', 'lw': 1.3}
        ax.annotate('', xy=(xmin, 0), xytext=(xmax, 0), arrowprops=axes_arrows)
        ax.annotate('', xy=(0, ymin), xytext=(0, ymax), arrowprops=axes_arrows)

        # Annotate the plot with equations
        plot_arrowsl = {'arrowstyle': '-|>', 'connectionstyle': "arc3, rad=-0.2"}
        plot_arrowsr = {'arrowstyle': '-|>', 'connectionstyle': "arc3, rad=0.2"}
        ax.annotate(r'$\rho_1 + \rho_2 < 1$', xy=(0.5, 0.3), xytext=(0.8, 0.6),
                    arrowprops=plot_arrowsr, fontsize='12')
        ax.annotate(r'$\rho_1 + \rho_2 = 1$', xy=(0.38, 0.6), xytext=(0.6, 0.8),
                    arrowprops=plot_arrowsr, fontsize='12')
        ax.annotate(r'$\rho_2 < 1 + \rho_1$', xy=(-0.5, 0.3), xytext=(-1.3, 0.6),
                    arrowprops=plot_arrowsl, fontsize='12')
        ax.annotate(r'$\rho_2 = 1 + \rho_1$', xy=(-0.38, 0.6), xytext=(-1, 0.8),
                    arrowprops=plot_arrowsl, fontsize='12')
        ax.annotate(r'$\rho_2 = -1$', xy=(1.5, -1), xytext=(1.8, -1.3),
                    arrowprops=plot_arrowsl, fontsize='12')
        ax.annotate(r'${\rho_1}^2 + 4\rho_2 = 0$', xy=(1.15, -0.35),
                    xytext=(1.5, -0.3), arrowprops=plot_arrowsr, fontsize='12')
        ax.annotate(r'${\rho_1}^2 + 4\rho_2 < 0$', xy=(1.4, -0.7),
                    xytext=(1.8, -0.6), arrowprops=plot_arrowsr, fontsize='12')

        # Label categories of solutions
        ax.text(1.5, 1, 'Explosive\n growth', ha='center', fontsize=16)
        ax.text(-1.5, 1, 'Explosive\n oscillations', ha='center', fontsize=16)
        ax.text(0.05, -1.5, 'Explosive oscillations', ha='center', fontsize=16)
        ax.text(0.09, -0.5, 'Damped oscillations', ha='center', fontsize=16)

        # Add small marker to y-axis
        ax.axhline(y=1.005, xmin=0.495, xmax=0.505, c='black')
        ax.text(-0.12, -1.12, '-1', fontsize=10)
        ax.text(-0.12, 0.98, '1', fontsize=10)

        return fig


# Use the method "summary" for example
sam = Samuelson(α=0.8, β=0.5, σ=2, g=10, g_t=20, duration='permanent')
sam.summary()
# Plot it
sam.plot()
plt.show()
# Draw a graph from page 189 of [Sar87]
sam.param_plot()
plt.show()
