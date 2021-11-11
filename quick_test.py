from models.base_model import BaseModel

if __name__ == "__main__":
    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)
    with open(file="file.json", encoding="utf-8", mode="w") as fd:
        fd.write(my_model.to_json(my_model.to_dict()))
