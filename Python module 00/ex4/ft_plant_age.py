def ft_plant_age():
    plant = int(input("Enter plant age in days: "))
    if plant >= 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
