
apellidos =         ["Perez", "Fernandez", "Gomez"] # 3
antiguedades =      [15,           5,        20   ] # 3
legajos =           [435,         250,       673  ] # 3
codigo_sector_emp = [1,            2,         1   ] # 3

id_sectores =   [    1,        2   ] # 2
sectores =      ["Sistemas", "RRHH"] # 2


print(f'{"Apellido":15}{"Antiguedad":12}{"Legajo":8}{"Sector":4}')
print("------------------------------------------")
for i in range(len(apellidos)):
    for j in range(len(sectores)): 
            if codigo_sector_emp[i] == id_sectores[j]:
                print(f"{apellidos[i]:10}{antiguedades[i]:12}{legajos[i]:10}   {sectores[j]:8}")