weight = 0.5
input = 0.5
goal_prediction = 0.8

step_amount = 0.001

for iter in range(1101):

    prediction = input * weight
    error = (prediction - goal_prediction) ** 2

    print('Error: ' + str(error) + ' Prediction: ' + str(prediction))

    up_prediction = input * (weight + step_amount)
    up_err = (up_prediction - goal_prediction) ** 2

    down_prediction = input * (weight - step_amount)
    down_err = (down_prediction - goal_prediction) ** 2

    if down_err < up_err:
        weight -= step_amount
    elif up_err < down_err:
        weight += step_amount
