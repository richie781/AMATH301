# Problem 2
#

import numpy as np

ans1 = np.array([np.cos(0), np.sin(np.pi), np.sin(np.pi / 3), np.cos(np.pi / 3)])
print(ans1)

# Problem 2a
#

ans2 = (np.pi / 2) * ans1
print(ans2)

# Problem 2b
#

ans3 = np.sin(ans1)
print(ans3)

# Problem 2c
#

ans4 = ans2 * ans3
print(ans4)

# Problem 2d
#


ans5 = ans3[:2]
print(ans5)

ans6 = ans4[-2:]
print(ans6)

ans7 = ans5 - ans6
print(ans7)
