
if __name__ == "__main__":
    permutations = 0
    ascending = 0

    for d4 in range(1, 5):
        for d6 in range(1, 7):
            for d8 in range(1, 9):
                permutations += 1
                if d4 < d6 < d8:
                    ascending += 1
    
    print(f"Probability of ascending: {ascending / permutations}")
