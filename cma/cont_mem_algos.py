def first_fit(memory: list, requirement: int, index: int):

    n = len(memory)
    for i, bloque in enumerate(memory[index:] + memory[:index]):
        if bloque[1] >= requirement:
            indice_original = (i + index) % n

            base = memory[indice_original][0]
            limit = memory[indice_original][1]
            memory.pop(indice_original)

            if limit - requirement > 0:
                new_pos = (base + requirement, limit - requirement)
                memory.insert(indice_original, new_pos)
                return (memory, base, requirement, indice_original)
            else:
                if indice_original >= len(memory):
                    indice_original = 0

                return (memory, base, requirement, indice_original)

    return None
