str = """Hello, my name is {}. I am {} years old. I live in {}.
My favourite hobby is {} & my ambition is to be {}.
My favourite sport is {}. My dream destination is {}"""

print(str.replace('{}', '_____'))

inputs = []

for i in range(str.count('{}')):
	inputs.append(input())

print(str.format(inputs[0],inputs[1],inputs[2],inputs[3],inputs[4],inputs[5],inputs[6]))
