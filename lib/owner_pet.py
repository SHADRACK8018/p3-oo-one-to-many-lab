class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        
        self.pet_type = pet_type
        self.owner = owner
        
        # Add this pet to the owner's pet list if an owner is provided
        if self.owner:
            self.owner.add_pet(self)

        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        # Return the list of pets owned by this owner
        return self._pets

    def add_pet(self, pet):
        # Check if the pet is an instance of the Pet class
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        
        # If the pet's owner is not already set (in case it's a new pet),
        # assign this owner to the pet and add the pet to the owner's list.
        if pet.owner is None:
            pet.owner = self
        
        # Add the pet to the owner's list of pets
        self._pets.append(pet)

    def get_sorted_pets(self):
        # Return the pets sorted by their names
        return sorted(self._pets, key=lambda pet: pet.name)
