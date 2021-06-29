is_on = False

class LightSwitch:
    is_on = False

    def flip(self):
        self.is_on = not self.is_on # field
        print(self.is_on)

    def flipMany(self, number : int):
        for i in range(number):
            self.flip()

def MultiplyByTwo(number: int):
    return number*2



living_room_light = LightSwitch()
bedroom_light = LightSwitch()

print('living_room_light:')
living_room_light.flipMany(13)

# print('bedroom_light:')
# bedroom_light.flip()

# result = MultiplyByTwo(2)
# print(result)

print(type(bedroom_light))
print(dir(bedroom_light))