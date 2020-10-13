#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    table = {}
    
    route = []

    for ticket in tickets:
        table[ticket.source] = ticket.destination

    route.append(table.pop('NONE'))

    for index in range(length -1 ):
        route.append(table.get(route[index]))
        

    return route

