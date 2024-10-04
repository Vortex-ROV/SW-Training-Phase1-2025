import matplotlib.pyplot as plt
import numpy as np

userInput = input("If you want preset data press N, if you want to enter your data press Y: ").lower()

if (userInput == 'y'):
    x = []
    y = []
    z = []

    print("entering first row, please enter it as a whole")
    inputData = list(map(int, input().split()))
    x = inputData

    print("entering second row, please enter it as a whole")
    inputData = list(map(int, input().split()))
    y = inputData

    print("entering third row, please enter it as a whole")
    inputData = list(map(int, input().split()))
    z = inputData

    data = np.array([x, y, z]) 

elif(userInput == 'n'):
    data = np.array([
        [3, 3, 0, 0, 1, 1, 1, 3, 2, 0, 2, 3, 2, 0, 0],
        [4, 3, 8, 8, 13, 10, 8, 4, 3, 1, 2, 1, 0, 1, 2],
        [3, 2, 5, 6, 3, 2, 3, 2, 2, 3, 2, 1, 0, 1, 0]
    ])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
ax.plot_surface(X, Y, data, cmap='viridis')
ax.set_xlabel('Day')
ax.set_ylabel('Receiver')
ax.set_zlabel('Number of Sturgeon')
plt.title('Sturgeon Detections (3D)')
plt.show()

plt.figure(figsize=(12, 6))
for i in range(data.shape[0]):
    plt.plot(data[i], label=f"Receiver {i+1}")
    
plt.xlabel("Day")
plt.ylabel("Number of Sturgeon")
plt.title("Sturgeon Detections per Day")
plt.legend()
plt.show()
