"""Print out all the melons in our inventory."""


from melons import melon_name


def print_melon(name, price, seedless,flesh,rind,average):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if not seedless:
        have_or_have_not = 'do not have'
    print(f'{name}\nPrice:{price}\nSeedless:{have_or_have_not}\nFlesh_color{flesh}\nRind_color:{rind}\nAverage:{average}')
    


for i in melon_name:
     print_melon(melon_name[i]["name"],melon_name[i]["price"],melon_name[i]["seed"],melon_name[i]['flesh_color'],melon_name[i]['rind_color'],melon_name[i]['average_weight'])
     print("\n\n")

    
