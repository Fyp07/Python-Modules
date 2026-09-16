def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def recursive(i):
        if i <= days:
            print(f"Day: {i}")
            recursive(i + 1)
        else:
            return
    recursive(1)
    print("Harvest time!")
