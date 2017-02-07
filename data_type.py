def data_type(d):
  if type(d) == str:
    return len(d)
  elif type(d) == bool:
    return d
  elif type(d) == int:
    if d > 100:
      return "more than 100"
    if d == 100:
      return "equal to 100"
    else:
      return "less than 100"
  elif type(d) == list:
    if len(d)<3:
      return None
    else:
      return d[2]
  else:
    return "no value"
