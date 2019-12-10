width = 25
height = 6
f = open("d8Input.txt", "r")
d8Input = f.read()
testinput = 123456789012
input = str(d8Input)
layers = []
length = len(input)
## CREATING LAYERS
for j in range(int(length/(height*width))):
    layer = []
    for i in range((j*width*height), ((j+1)*width*height),width):
        layer.append(input[i:i+width])
    layers.append(layer)
## END LAYER CREATION
#PART ONE
# lowest_count = 200
# lowest_layer = 101
# for i in range(len(layers)):
#     count = 0
#     for j in layers[i]:
#         count += str(j).count('0')
#     if count < lowest_count:
#         lowest_count = count
#         lowest_layer = i
# ones = 0
# twos = 0
# for i in layers[lowest_layer]:
#     ones += str(i).count('1')
#     twos += str(i).count('2')
# print(ones*twos)
#PART TWO
final = layers[0]

for layer in layers:
    for i in range(len(layer)):
        final[i] = list(final[i])
        for j in range(len(layer[i])):
            if final[i][j] == '1':
                final[i][j] = final[i][j]
            elif final[i][j] == '0':
                final[i][j] = '0'
            elif final[i][j] == '2':
                final[i][j] = layer[i][j]

for i in final:
    line = ''.join(i)
    print(" ")
    for j in line:
        if j == '0':
            print(' ', end=" "),
        else:
            print('X', end=" ")