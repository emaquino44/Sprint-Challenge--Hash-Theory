def reconstruct_trip(tickets):
  ticket_dict = {}
  route = [''] * (len(tickets)-1)
  for ticket in tickets:
    ticket_dict[ticket[0]] = ticket[1]
    if ticket[0] == None:
      route[0] = ticket[1]
  for i in range(1, len(route)):
    if route[i-1] in ticket_dict:
      route[i] = ticket_dict[route[i-1]]
    else:
      return []
  return route


if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass
