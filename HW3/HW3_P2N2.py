import numpy as np
import math

def activation(x):
        return 1/(1+math.e**(-x))


if __name__ == '__main__':
    input = np.array([[-1, -1], [-1, 1], [-1, 1], [1, 1]])
    Yd = np.array([0, 1, 1, 0])
    lr = 0.1
    InitialWeights = np.array([0.2, -0.4, 0.2, -0.2, 0.4])
    InitialBias = np.array([0.8, 0.3])
    MaxEpoch = 10000
    for i in range(MaxEpoch):
        eperror = 0
        epout = []
        for j in range(4):
            n3 = np.dot(input[j][:], InitialWeights[:2]) - InitialBias[0]
            n4 = np.dot(input[j][:], InitialWeights[2:4]) + np.dot(activation(n3), InitialWeights[4])- InitialBias[1]

            out = activation(n4)
            epout.append(out)
            error = Yd[j] - out
            eperror += abs(error)
            epsilon4 = -2 * error * out * (1-out)

            epsilon3 = activation(n3) * (1-activation(n3)) * epsilon4 * InitialWeights[4]


            InitialWeights[0] -= lr*epsilon3*input[j][0]
            InitialWeights[1] -= lr*epsilon3*input[j][1]
            InitialWeights[2] -= lr*epsilon4*input[j][0]
            InitialWeights[3] -= lr*epsilon4*input[j][1]
            InitialWeights[4] -= lr*epsilon4*activation(n3)

            InitialBias[0] += lr*epsilon3*1
            InitialBias[1] += lr*epsilon4*1
        print("Y")
        print(epout)
        print("eperror")
        print(eperror)