class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):

        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("add_pet requires a Pet instance")
        pet.owner = self  


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None
        Pet.all.append(self)

        if owner:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an Owner instance")
            self.owner = owner

    def __repr__(self):
        return f"<Pet: {self.name}, Type: {self.pet_type}, Owner: {self.owner.name if self.owner else 'None'}>"


def get_sorted_pets(self):
    return sorted(self.pets(), key=lambda pet: pet.name)

Owner.get_sorted_pets = get_sorted_pets
