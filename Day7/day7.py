def parse_input():
    with open ("input7small.txt", "r") as f:
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


def concatinated_arrays(array: list) -> list:
    def generate_combinations(index, current):
        """
        Rekursive Funktion, die alle möglichen Kombinationen erstellt.
        """
        if index == len(array):
            results.append(current)
            return
        
        # Fall 1: Das aktuelle Element als eigenständige Zeichenkette anhängen
        generate_combinations(index + 1, current + [array[index]])
        
        # Fall 2: Das aktuelle Element an die letzte Zeichenkette anhängen (falls vorhanden)
        if current:
            current[-1] += array[index]
            generate_combinations(index + 1, current[:])  # Kopie übergeben
            current[-1] = current[-1][:-len(array[index])]  # Rückgängig machen

    results = []
    generate_combinations(0, [])
    return results


    
    
    
       

def add(zahl: int, zahlen_array:list, score:int, truescores:list) -> list:
    
    zahlen_array = zahlen_array.copy()

    try:
        zahlen_array.pop(0)
    except IndexError:
        pass 

    if len(zahlen_array) == 0:
        if zahl == score and score not in truescores:
            truescores.append(score)
            
    else:
        new_zahl = zahl + int(zahlen_array[0])
        new_array = zahlen_array.copy()

        
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
            
    else:
        new_zahl = zahl * int(zahlen_array[0])
        new_array = zahlen_array.copy()

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

        all_possible_arrays = concatinated_arrays(array)

        for possible_array in all_possible_arrays:
                possible_array = list(possible_array)
                print(possible_array)
                if len(possible_array) > 1:
                    all_scores_fit.append(calculate_array(startZahl, possible_array, key))
                
    
        for score in all_scores_fit:
            if score:
                sum += int(score[0])

    print(sum)

if __name__ == "__main__":
    main()
    