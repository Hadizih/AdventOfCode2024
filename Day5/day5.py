import math


def parse_input() -> list:
    with open("input5.txt") as f:
        raw_list = f.read().splitlines()

        index_to_split = raw_list.index("")

        ordering_rules_raw = raw_list[:index_to_split]
        updates = raw_list[index_to_split + 1 :]

        pretty_updates = []

        for list in updates:
            list = list.split(",")
            pretty_updates.append(list)

        ordering_rules = []

        for rule in ordering_rules_raw:
            pretty_rule = rule.split("|")
            ordering_rules.append(pretty_rule)

        pages: dict = {}
        for rule in ordering_rules:
            if rule[0] not in pages:
                pages[rule[0]] = []
                pages[rule[0]].append(rule[1])
            else:
                pages[rule[0]].append(rule[1])

        return pages, pretty_updates


def get_valid_updates(pages: dict, updates: list) -> list:

    valid_updates: list = []
    invalid_updates: list = []

    # für jedes update aus der liste
    for update in updates:
        valid = True
        # für jede seite in der update
        for number in update:
            if not valid:
                break
            # holt die seiten, die hinter der aktuellen seite stehen müssen (number) aus dem dict
            if number in pages.keys():
                pages_after = pages[number]
                if pages_after:
                    for page in pages_after:
                        if page in update:
                            page_after_index = update.index(page)

                            if page_after_index < update.index(number):
                                invalid_updates.append(update)
                                valid = False
                                break

        if valid:
            valid_updates.append(update)

    return valid_updates, invalid_updates


def calculate_valid_sum(valid_updates: list) -> int:
    sum = 0
    for update in valid_updates:
        sum += int(update[math.floor(len(update) / 2)])

    return sum


def correct_updates(pages: dict, updates: list) -> list:

    corrected_updates = []

    for update in updates:
        reordered_update = update[:]
        is_not_valid = True

        while is_not_valid:
            is_not_valid = False
            for number in reordered_update:
                if number in pages.keys():
                    pages_after = pages[number]
                    if pages_after:
                        for page in pages_after:
                            if page in reordered_update:
                                page_after_index = reordered_update.index(page)
                                page_index = reordered_update.index(number)

                                if page_after_index < page_index:
                                    reordered_update.remove(page)
                                    reordered_update.insert(page_index, page)
                                    is_not_valid = True

                                    
                                    

        corrected_updates.append(reordered_update)
    return corrected_updates


def main():
    ordering_rules, updates = parse_input()
    valid_updates, invalid_updates = get_valid_updates(ordering_rules, updates)
    print(f"SUM Part1: {calculate_valid_sum(valid_updates)}")

    corrected_updates = correct_updates(ordering_rules, invalid_updates)

    print(f"Corrected updates: {calculate_valid_sum(corrected_updates)}")


if __name__ == "__main__":
    main()
