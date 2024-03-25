def conv_time(text, flags):
    temp = [0, 0]
    current_value = text.split(":")
    sec = int(current_value[1])
    if (sec >= 60):
        temp[0] += 1
        current_sec = sec - 60
        temp[1] += current_sec
        if( current_sec < 10 ):
          flags.append(True)
          temp[1] = 0
          temp.append(current_sec)
    else:
        if( sec < 10 ):
          flags.append(True)
          temp[1] = 0
          temp.append(sec)
        else:
          temp[1] = sec

    result = []
    
    result.append(str(temp[0]))
    if(flags[(len(flags)-1)]):
      str_sec = ""
      str_sec += str(temp[1]) + str(temp[2])
      result.append(str_sec)
    else:
      result.append(str(temp[1]))

    return result