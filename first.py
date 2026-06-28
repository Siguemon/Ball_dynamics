import numpy as np

class ball:
    def __init__(self):
        self.x = 0 #m
        self.y = 0 #m
        self.vx = 0 #m/s
        self.vy = 0 #m/s

    def set_x(self, x): self.x = x
    def set_y(self, y): self.y = y
    def set_vx(self, vx): self.vx = vx
    def set_vy(self, vy): self.vy = vy

    def get_x(self): return self.x
    def get_y(self): return self.y
    def get_vx(self): return self.vx
    def get_vy(self): return self.vy
    def get_ax(self): return 0 #- self.vx #m/s2
    def get_ay(self): return -0 #- self.vy #m/s2

    def update_x(self, time): #self.x += self.vx * time
        if self.x < 0: self.x = abs(self.x) + self.vx * time
        elif self.x > 1: self.x = 1 - abs(self.x - 1) + self.vx * time
        else:          self.x += self.vx * time
    def update_y(self, time):
        if self.y < 0: self.y = abs(self.y) + self.vy * time
        elif self.y > 1: self.y = 1 - abs(self.y - 1) + self.vy * time
        else:          self.y += self.vy * time

    def update_vx(self, time): #self.vx += self.get_ax() * time
        if self.x < 0: self.vx = abs(self.vx) + self.get_ax() * time
        elif self.x > 1: self.vx = -self.vx + self.get_ax() * time
        else:          self.vx += self.get_ax() * time
    def update_vy(self, time):
        if self.y < 0: self.vy = abs(self.vy) + self.get_ay() * time
        elif self.y > 1: self.vy = -self.vy + self.get_ay() * time
        else:          self.vy += self.get_ay() * time

    def update(self, time):
        self.update_x(time)
        self.update_y(time)
        self.update_vx(time)
        self.update_vy(time)

    def __repr__(self):
        return f'x :\t{self.x} m\ny :\t{self.y} m\nvx :\t{self.vx} m/s\nvy :\t{self.vy} m/s\n'
    def __str(self): return self.__repr__()

####
a = ball()

a.set_x(.5) ; a.set_y(.75); a.set_vx(1) ; a.set_vy(-1)
print(f'Initial setup :\n{a}')

time = 1E-3
ndots = int(5E3)

x,y = np.array([]), np.array([])
for i in range(ndots):
    a.update(time)
    x = np.append(x, a.get_x())
    y = np.append(y, a.get_y())

if __name__=="__main__":
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    fig = plt.figure()
    ax = fig.add_subplot(aspect=1)

    line = ax.plot(x,y, 'ko', ms=2)[0]
    lin_kw = {'color':'k','lw':1} ; ax.hlines(0,0,1,**lin_kw) ; ax.hlines(1,0,1,**lin_kw) ; ax.vlines(0,0,1,**lin_kw) ; ax.vlines(1,0,1,**lin_kw)

    def update(frame):
        line.set_xdata([x[10*frame]])
        line.set_ydata([y[10*frame]])

        return line

    ani = animation.FuncAnimation(fig=fig, func=update, frames=ndots//10, interval=10)

    plt.show()
