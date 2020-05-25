class Rectangular():
    def __init__(self):
        print('直方体の3辺の長さ(m)を入力してください。')
        self.x = int(input('x: '))
        self.y = int(input('y: '))
        self.z = int(input('z: '))

    def volume(self):
        print(f'volume: {self.x * self.y * self.z} m^3')

    def surface_area(self):
        xy = self.x * self.y
        xz = self.x * self.z
        yz = self.y * self.z
        print(f'surface_area: {(xy + xz + yz) * 2} m^2')

r = Rectangular()
r.volume()
r.surface_area()