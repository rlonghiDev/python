from platform import platform,machine,processor,system,version

# print(platform())
# print(platform(1))
# print(platform(0, 1))

print(machine())

print(processor())

print(system())

print(version())


from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)