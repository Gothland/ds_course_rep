import numpy as np
def predict(number:int=1) -> int:
    """Multiline comment about what function does
    """
    try_count = 0
    while True:
        try_count += 1
        predicted_num = np.random.randint(1, 101)
        if predicted_num == number:
            break
    return try_count
# RUN
if __name__ == '__main__':
    print(f'Tryouts count: {predict(15)}')