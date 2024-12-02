
# read and parse the input
def read_input():
    with open('input1.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    return lines

# check if the report is valid
def is_valid_report(report):
    levels = [int(level) for level in report.split()]

# check if the levels are in ascending or descending order
    if not (ascending(levels) or descending(levels)):
       return False
    
    return check_level_validity(levels)

# count the number of valid reports
def count_valid_reports(reports):
    return sum(1 for report in reports if is_valid_report(report))

# check if the levels are in ascending order
def ascending(levels):
    return all(levels[i] <= levels[i+1] for i in range(len(levels)-1))

# check if the levels are in descending order
def descending(levels):
    return all(levels[i] >= levels[i+1] for i in range(len(levels)-1))
            
# check if the levels are valid
def check_level_validity(levels):
    return all(1 <= abs(levels[i] - levels[i+1]) <= 3 for i in range(len(levels)-1))
            

def main():
    lines = read_input()
    valid_reports = count_valid_reports(lines)
    
    print(f"Number of valid reports: {valid_reports}")
   

if __name__ == '__main__':
    main()
    