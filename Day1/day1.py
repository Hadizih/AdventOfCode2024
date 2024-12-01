## transform input into lists of integers
def get_lists():
    list1 = []
    list2 = []

    with open('input1-1.txt') as f:
        lines = f.readlines()

    for line in lines:
            left, right = line.split('   ')
            list1.append(int(left))
            list2.append(int(right))

    return sorted(list1), sorted(list2)

## calculate the distance between the two lists
def calculate_distance(list1, list2):
    distance = 0

    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])
       

    print(f"Total distance: {distance}")

def calculate_similarity(list1, list2):
    from collections import Counter
    # count the number of times each number appears in list2
    list2_counts = Counter(list2)

    # calculate the similarity score
    similarity_score = sum(number * list2_counts[number] for number in list1)
    
    print(f"Similarity score: {similarity_score}")

def main():
    list1, list2 = get_lists()
    # part1
    calculate_distance(list1, list2)

    # part2
    calculate_similarity(list1, list2)

if __name__ == '__main__':
    main()