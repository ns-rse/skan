import numpy as np


tinycycle = np.array([[0, 1, 0],
                      [1, 0, 1],
                      [0, 1, 0]], dtype=bool)


skeleton1 = np.array([[0, 1, 1, 1, 1, 1, 0],
                      [1, 0, 0, 0, 0, 0, 1],
                      [0, 1, 1, 0, 1, 1, 0],
                      [1, 0, 0, 1, 0, 0, 0],
                      [1, 0, 0, 0, 1, 1, 1]], dtype=bool)


zeros1 = np.zeros_like(skeleton1)
skeleton2 = np.column_stack((skeleton1, zeros1))
skeleton2 = np.row_stack((skeleton2, skeleton2[:, ::-1]))