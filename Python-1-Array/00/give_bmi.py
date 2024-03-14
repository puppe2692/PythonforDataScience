def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    '''Return a list of BMI calculated from the height and weight received'''
    try:
        len(height) == len(weight)
    except ValueError:
        print("ArgumentError: List sizes are not matching")
    try:
        isinstance(height, list[int | float])
        isinstance(weight, list[int | float])
    except ValueError:
        print("ArgumentError: not the right type")

    bmi_list = []
    for i, item in enumerate(height):
        new_value = weight[i] / item ** 2
        bmi_list.append(new_value)

    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''Return a list of boolean that represent
        if the BMI is over the limit received'''
    try:
        if (not isinstance(bmi, list[int | float])
                or not isinstance(limit, int)):
            raise ValueError("ArgumentError: not the right type")
    except ValueError as e:
        print(e)

    boolean_list = []
    for item in bmi:
        if item <= limit:
            boolean_list.append(False)
        else:
            boolean_list.append(True)

    return (boolean_list)
