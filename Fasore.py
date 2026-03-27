import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML, display

plt.close('all')

raggio = 1

fig = plt.figure(figsize=(8, 8))
ax = fig.add_axes([0.1, 0.4, 0.8, 0.55])
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-raggio - 1, raggio + 1)
ax.set_ylim(-raggio - 1, raggio + 1)
ax.grid(True)
ax.set_title('Punto sulla circonferenza e proiezioni su assi X e Y')

circle = plt.Circle((0, 0), raggio, color='blue', fill=False)
ax.add_patch(circle)

point, = ax.plot([], [], 'o', color='red', markersize=8, label='Punto sulla circonferenza')
proj_x_line, = ax.plot([], [], '--', color='orange', alpha=0.7, label='Proiezione X')
proj_y_line, = ax.plot([], [], '--', color='green', alpha=0.7, label='Proiezione Y')
proj_x_point, = ax.plot([], [], 'o', color='orange', markersize=6)
proj_y_point, = ax.plot([], [], 'o', color='green', markersize=6)

ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

t_vals_full = np.linspace(0, 2 * np.pi, 200)
ax_sin_cos = fig.add_axes([0.1, 0.05, 0.8, 0.2])
ax_sin_cos.set_xlim(0, 2 * np.pi)
ax_sin_cos.set_ylim(-1.1, 1.1)
ax_sin_cos.grid(True)
ax_sin_cos.set_title('sin(theta) e cos(theta)')

line_cos, = ax_sin_cos.plot([], [], label='cos(theta)', color='orange')
line_sin, = ax_sin_cos.plot([], [], label='sin(theta)', color='green')

ax.legend()

def init():
    point.set_data([], [])
    proj_x_line.set_data([], [])
    proj_y_line.set_data([], [])
    proj_x_point.set_data([], [])
    proj_y_point.set_data([], [])
    line_cos.set_data([], [])
    line_sin.set_data([], [])
    return point, proj_x_line, proj_y_line, proj_x_point, proj_y_point, line_cos, line_sin

def update(frame):
    theta = 2 * np.pi * frame / 100
    x = raggio * np.cos(theta)
    y = raggio * np.sin(theta)
    point.set_data([x], [y])
    proj_x_line.set_data([x, x], [0, y])
    proj_x_point.set_data([x], [0])
    proj_y_line.set_data([0, x], [y, y])
    proj_y_point.set_data([0], [y])
    t_vals = np.linspace(0, theta, 50)
    line_cos.set_data(t_vals, np.cos(t_vals))
    line_sin.set_data(t_vals, np.sin(t_vals))
    return point, proj_x_line, proj_y_line, proj_x_point, proj_y_point, line_cos, line_sin

ani = animation.FuncAnimation(fig, update, frames=range(100), init_func=init,
                              blit=True, interval=50, repeat=False)

animation_html = ani.to_jshtml()
plt.close(fig)
display(HTML(animation_html))
