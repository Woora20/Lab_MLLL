def fire(fbond, fcombust):
    # Get bond-energy information
    bond_energy = {}
    with open(fbond, 'r') as f:
        for line in f:
            key, val = line.split()
            bond_energy[key] = int(val)

    # Get combustion information
    with open(fcombust, 'r+') as f:
        f.readline()  # read out the header

        # Reactants
        reactant = f.readline().rstrip()  # read the reactant line (2nd line)
        reactant = reactant.split('+')

        E1 = 0  # Initialize activation energy
        for b in reactant:
            num_bonds, bond_symbol = b.strip().split()
            energy = bond_energy[bond_symbol]
            E1 += energy * float(num_bonds)

        # Products
        product = f.readline().rstrip()  # read the product line (3rd line)
        product = product.split('+')

        E2 = 0  # Initialize releasing energy
        for p in product:
            num_bonds, bond_symbol = p.strip().split()
            energy = bond_energy[bond_symbol]
            E2 += energy * float(num_bonds)

        # Calculate total energy
        total_E = E1 - E2
        msg = '\nEa = {:,.1f} kJ, Er = {:,.1f} kJ, E = {:,.1f} kJ'.format(E1, E2, total_E)

        # Write the message to the file
        f.write(msg)

if __name__ == '__main__':
    fire('bond_energy.txt', 'methane.txt')
