class DST:
    def __init__(self, elements):
        self.elements = elements
        self.belief = {element: 0 for element in elements}

    def assign_mass(self, element, mass):
        if element in self.elements:
            self.belief[element] = mass
        else:
            raise ValueError("Element not found in the frame of discernment.")

    def combine_evidence(self, *mass_functions):
        combined_belief = {element: 0 for element in self.elements}

        for element in self.elements:
            combined_mass = 1
            for mass_function in mass_functions:
                combined_mass *= 1 - mass_function[element]
            combined_mass = 1 - combined_mass

            combined_belief[element] = combined_mass

        self.belief = combined_belief

    def decision(self):
        max_belief = max(self.belief.values())
        candidates = [element for element, belief in self.belief.items() if belief == max_belief]
        return candidates

if __name__ == "__main__":
    elements = ['A', 'B', 'C', 'D']
    dst1 = DST(elements)
    dst2 = DST(elements)

    dst1.assign_mass('A', 0.6)
    dst1.assign_mass('B', 0.2)
    dst1.assign_mass('C', 0.1)
    dst1.assign_mass('D', 0.1)

    dst2.assign_mass('B', 0.5)
    dst2.assign_mass('C', 0.3)
    dst2.assign_mass('D', 0.2)

    dst1.combine_evidence(dst2.belief)
    print("Combined belief:", dst1.belief)

    decision = dst1.decision()
    print("Decision based on combined belief:", decision)
