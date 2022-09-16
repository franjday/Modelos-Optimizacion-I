from collections import OrderedDict

def main():
    incompatible_pieces = {}
    pieces_by_wash_time = {}
    with open("Segundo Problema.txt", 'r') as File:
        for line in File:
            line = line.split()
            type = line[0]
            if type == 'e':
                add_to_dict(incompatible_pieces, int(line[1]), int(line[2]))
            elif type == 'n':
                add_to_dict(pieces_by_wash_time, int(line[2]), int(line[1]))
            else:
                continue
    
    wash_plan = find_solution(pieces_by_wash_time, incompatible_pieces)
    export_plan(wash_plan)


def add_to_dict(dictionary, prenda1, prenda2):
    if prenda1 in dictionary:
        dictionary[prenda1].append(prenda2)
    else:
        dictionary.setdefault(prenda1, [])
        dictionary[prenda1].append(prenda2)
        

def find_solution(pieces_by_wash_time, incompatible_pieces):
    wash_plan = {}
    washing_machine = 0
    sorted_wash_times = OrderedDict(sorted(pieces_by_wash_time.items(), key=lambda t: t[0], reverse=True))

    for pieces in sorted_wash_times:
        for piece in sorted_wash_times[pieces]:
            available_machine = check_machines(piece, wash_plan, incompatible_pieces)
            if available_machine is not None:
                wash_plan[available_machine].append(piece)
            else:
                washing_machine += 1
                wash_plan.setdefault(washing_machine, [])
                wash_plan[washing_machine].append(piece)
                
    return wash_plan


def check_machines(piece, wash_plan, incompatible_pieces):
    available_machine = None
    for key, value in wash_plan.items():
        next_machine = True
        for piece_in_wash in value:
            if piece_in_wash in incompatible_pieces.get(piece, []) or piece in incompatible_pieces.get(piece_in_wash, []):
                available_machine = None
                break
            else:
                available_machine =  key
                next_machine = False
        if not next_machine and available_machine is not None:
            break

    return available_machine


def export_plan(wash_plan):
    with open("wash_plan.txt", 'w') as file:
        for key in wash_plan:
            for value in wash_plan[key]:
                file.write(str(value) + " " + str(key) + "\n")


if __name__ == "__main__":
    main()