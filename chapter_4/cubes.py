for value in range(1, 11):
    print(value ** 3)

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

print("\nThe first three items in the list are:")
for cube in cubes[:3]:
    print(cube)

print("\nThree items frim the middle of the list are:")
for cube in cubes[4:7]:
    print(cube)

print("\nThe last three items in the list are:")
for cube in cubes[-3:]:
    print(cube)
