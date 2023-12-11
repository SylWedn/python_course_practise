
def kmi(weight, height):
    if not (21 <= weight <= 200) or not (0.5 <= height <= 2.5):
        raise ValueError("Invalid weight or height value.")

    return round(weight / (height ** 2), 14)


if __name__ == '__main__':
    print(kmi(78, 1.82))
    print(kmi(50, 1.56))
    print(kmi(100, 1.90))
    print(kmi(20, 1.40))
    print(kmi(240, 1.40))
    print(kmi(80, 0.40))
    print(kmi(80, 3.40))
