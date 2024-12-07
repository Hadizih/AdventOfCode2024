def parse_input():
    with open ("input7.txt", "r") as f:
        input  = f.read().splitlines()
        pretty_input = []
        for line in input:
            lines = line.split(":")
            pretty_input.append(lines)
        
        scoreDict = {}
        for line in pretty_input:
            scoreDict[line[0]] = line[1].strip().split(" ")
        
        for key in scoreDict:
            for number in scoreDict[key]:
                number = int(number)
            

    return scoreDict



def add(zahl: int, zahlen_array:list, score:int, truescores:list) -> list:
    
    zahlen_array = zahlen_array.copy()

    try:
        zahlen_array.pop(0)
    except IndexError:
        pass 

    if len(zahlen_array) == 0:
        if zahl == score and score not in truescores:
            truescores.append(score)
            return truescores
    else:
        new_zahl = zahl + int(zahlen_array[0])
        new_array = zahlen_array

        
        add(new_zahl, new_array, score, truescores)
        multiply(new_zahl, new_array, score, truescores)
        


def multiply(zahl: int, zahlen_array:list, score:int, truescores:list) -> list:
    
    zahlen_array = zahlen_array.copy()

    try:
        zahlen_array.pop(0)
    except IndexError:
        pass    

    if len(zahlen_array) == 0:
        if zahl == score and score not in truescores:
            truescores.append(score)
            return truescores
    else:
        new_zahl = zahl * int(zahlen_array[0])
        new_array = zahlen_array

        add(new_zahl, new_array, score, truescores)
        multiply(new_zahl, new_array, score, truescores)
        

def calculate_array(zahl: int, zahlen_array:list, key:int) -> list:
    true_scores = []
    add(zahl, zahlen_array, key, true_scores)
    multiply(zahl, zahlen_array, key, true_scores)
    
    if true_scores:
        return true_scores
     
    
    
def main():
    input = parse_input()
    scores = input.keys()
    sum = 0

    all_scores_fit = []
    for key in scores:

        array = list(input[key])
        startZahl = int(array[0])
        key = int(key)
        
        all_scores_fit.append(calculate_array(startZahl, array, key))
    
    for score in all_scores_fit:
        if score:
            sum += int(score[0])

    print(sum)

if __name__ == "__main__":
    main()
    