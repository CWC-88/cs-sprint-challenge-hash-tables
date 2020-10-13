def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    weightDict = {}
    index1 = -1
    index2 = -1

    for (index, weight) in enumerate(weights):
        if str(weight) in weightDict:
            index1 = index

            index2 = weightDict[str(weight)]

            return (index1, index2)
        elif weight > limit:

            pass

        else:
            weightDict[str(limit - weight)] = index

    return None