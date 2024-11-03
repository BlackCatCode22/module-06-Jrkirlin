#class pokemonmasters:
 #   def __int__(self):
  #      self.pokedexcount = 1
#
 #   def geetum(self):
  #      self.pokedexcount = self.pokedexcount + 1
   #     print("Dang it all. That's" , self.pokedexcount, "freakin Rattatas. bbbbbbbbbbbb")

#pokemon = pokemonmasters()

#pokemon.geetum()
#pokemon.geetum()
#pokemon.geetum()

#print("Type", type(pokemon))
#print("Dir", dir(pokemon))
#print("Type", type(pokemon.pokedexcount))
#print("Type", type(pokemon.geetum()))

class PartyAnimal:

    def __init__(self):
        self.x = 0

    def party(self):
        self.x = self.x + 1
        print("So far...", self.x)


an = PartyAnimal()

print("type is: ", type(an))
print("dir is: ", dir(an))
print("type of an.x is: ", type(an.x))

an.party()
an.party()
an.party()