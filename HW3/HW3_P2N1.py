import numpy as np
import math




def activation(x):
        return 1/(1+math.e**(-x))



if __name__ == '__main__':
    input = np.array([[-1, -1], [-1, 1], [-1, 1], [1, 1]])
    Yd = np.array([0, 1, 1, 0])
    lr = 0.1
    InitialWeights = np.array([0.2, -0.4, 0.2, -0.2, 0.1, -0.4])
    InitialBias = np.array([0.8, -0.1, 0.3])
    MaxEpoch = 300000
    for i in range(MaxEpoch):
        eperror = 0
        epout = []
        for j in range(4):
            n3 = np.dot(input[j][:], InitialWeights[:2]) - InitialBias[0]
            n4 = np.dot(input[j][:], InitialWeights[2:4]) - InitialBias[1]
            n5 = np.dot( [activation(n3), activation(n4)], InitialWeights[4:6]) - InitialBias[2]
            out = activation(n5)
            epout.append(out)
            error = Yd[j] - out
            eperror += abs(error)
            epsilon5 = -2 * error * out * (1-out)

            epsilon3 = activation(n3) * (1-activation(n3)) * epsilon5 * InitialWeights[4]

            epsilon4 = activation(n4) * (1-activation(n4)) * epsilon5 * InitialWeights[5]


            InitialWeights[0] = InitialWeights[0] - lr*epsilon3*input[j][0]
            InitialWeights[1] -= lr*epsilon3*input[j][1]
            InitialWeights[2] -= lr*epsilon4*input[j][0]
            InitialWeights[3] -= lr*epsilon4*input[j][1]
            InitialWeights[4] -= lr*epsilon5*activation(n3)
            InitialWeights[5] -= lr*epsilon5*activation(n4)

            InitialBias[0] += lr*epsilon3*1
            InitialBias[1] += lr*epsilon4*1
            InitialBias[2] += lr*epsilon5*1
        print("Y")
        print(epout)
        print("eperror")
        print(eperror)