class Chem_Info:
    
    def __init__(self, atom_info, bond_info):
        self.atom_info = atom_info
        self.bond_info = bond_info
        
    def molar_mass(self):
        
        mw_table = {'C.':12.011, 'N.':14.007, 'O.':15.999,
                    'P.':30.974, 'S.':32.060, 'F':18.998,
                    'Cl':35.45, 'Br':79.904, 'H':1.008,
                    'I':126.90, 'Se':78.971}
        
        weight = 0
        for i in range(len(self.atom_info)):
            atom = self.atom_info[i][5][:2]
            weight += mw_table[atom]
            
        return round(weight,6)

    def HB_donor(self):
        HB_donor = 0
        
        nitro = []
        oxy = []

        for i in range(len(self.atom_info)):
            
            if 'N' in self.atom_info[i][5]:
                atom_id = self.atom_info[i][0]
                for j in range(len(self.bond_info)):
                    if atom_id == self.bond_info[j][1]:
                        nitro.append(self.bond_info[j][2])
                    elif atom_id == self.bond_info[j][2]:
                        nitro.append(self.bond_info[j][1])
                        
            elif 'O' in self.atom_info[i][5]:
                atom_id = self.atom_info[i][0]
                for j in range(len(self.bond_info)):
                    if atom_id == self.bond_info[j][1]:
                        oxy.append(self.bond_info[j][2])
                    elif atom_id == self.bond_info[j][2]:
                        oxy.append(self.bond_info[j][1])
    
        for i in range(len(self.atom_info)):
            
            for test_n in nitro:
                if test_n == self.atom_info[i][0] and 'H' in self.atom_info[i][5]:
                    HB_donor += 1
            for test_o in oxy:
                if test_o == self.atom_info[i][0] and 'H' in self.atom_info[i][5]:
                    HB_donor += 1
                        
        return HB_donor

    def HB_acceptor(self):
        
        HB_acceptor = 0
        for i in range(len(self.atom_info)):
            if 'O' in self.atom_info[i][5]:
                HB_acceptor += 1
            if 'N' in self.atom_info[i][5]:
                HB_acceptor += 1
                
        return HB_acceptor

    def net_charge(self):
        
        net_charge = 0
        for i in range(len(self.atom_info)):
            atom_charge = float(self.atom_info[i][8])
            net_charge += atom_charge
            
        return round(net_charge)
    
    def atom_count(self):
        
        c, n, o, h = 0, 0, 0, 0
        p, x, s, other = 0, 0, 0, 0
        for i in range(len(self.atom_info)):
            if self.atom_info[i][1][:1] == 'C':
                c += 1
            elif self.atom_info[i][1][:1] == 'N':
                n += 1
            elif self.atom_info[i][1][:1] == 'O':
                o += 1
            elif self.atom_info[i][1][:1] == 'P':
                p += 1
            elif self.atom_info[i][1][:1] == 'F' or self.atom_info[i][1][:1] == 'I':
                x += 1
            elif 'Br' in self.atom_info[i][1][:2] or 'Cl' in self.atom_info[i][1][:2]:
                x += 1
            elif self.atom_info[i][1][:1] == 'H':
                h += 1
            elif self.atom_info[i][1][:1] == 'S':
                s += 1
            else:
                other += 1
                
        return c, h, n, o, x, s, p, other

class Datablocks:
    
    def __init__(self, parse_list):
        self.parse_list = parse_list
        self.mol_block = []
        self.atom_block = []
        self.bond_block = []

    def mol_info(self):
        
        for i in range(len(self.parse_list)):
            if '@' in self.parse_list[i][0]:
                temp_storage = self.parse_list[i][0]
            while temp_storage == '@<TRIPOS>MOLECULE':
                self.mol_block.append(self.parse_list[i])
                break
                
        self.mol_block.pop(0)
        
        return self.mol_block

    def atom_info(self):
        
        for i in range(len(self.parse_list)):
            if '@' in self.parse_list[i][0]:
                temp_storage = self.parse_list[i][0] 
            while temp_storage == '@<TRIPOS>ATOM':
                self.atom_block.append(self.parse_list[i])
                break
        
        self.atom_block.pop(0)
        
        return self.atom_block
                
    def bond_info(self):
        
        for i in range(len(self.parse_list)):
            if '@' in self.parse_list[i][0]:
                temp_storage = self.parse_list[i][0]
            while temp_storage == '@<TRIPOS>BOND':
                self.bond_block.append(self.parse_list[i])
                break
                
        self.bond_block.pop(0)
        
        return self.bond_block
    
def parse_mol2(file_mol2):

    parse_list = []

    molecule = open(file_mol2,'r')
    dirty_list = molecule.readlines()
    molecule.close()

    for i in range(len(dirty_list)):
        parse = dirty_list[i]
        parse = parse.strip('\n')
        parse = parse.strip(' ')
        dirty_list[i] = parse
        
    dirty_list = [i for i in dirty_list if i]

    for i in range(len(dirty_list)):
        parse = dirty_list[i].split(None)
        parse_list.append(parse)
        
    return parse_list
