# jede reihe ist ein report mit levels
# levels dürfen entweder aufsteigen oder absteigen
# auf-oder abstieg darf maximal 3 sein
# zählen wieviele reports valid sind


# input verarbeiten und in liste speichern
# prüfen abstand zwischen zwei levels maximal abs(3) != 0

def read_input():
    with open('input1.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    return lines

def is_valid_report(report):
    levels = [int(level) for level in report.split()]

    if not (ascending(levels) or descending(levels)):
       return False
    
    return check_level_validity(levels)

def count_valid_reports(reports):
    return sum(1 for report in reports if is_valid_report(report))

def ascending(levels):
    return all(levels[i] <= levels[i+1] for i in range(len(levels)-1))

def descending(levels):
    return all(levels[i] >= levels[i+1] for i in range(len(levels)-1))
            
def check_level_validity(levels):
    return all(1 <= abs(levels[i] - levels[i+1]) <= 3 for i in range(len(levels)-1))
            

def main():
    lines = read_input()
    valid_reports = count_valid_reports(lines)
    
    print(f"Number of valid reports: {valid_reports}")
   

if __name__ == '__main__':
    main()
    