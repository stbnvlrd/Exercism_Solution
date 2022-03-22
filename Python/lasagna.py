EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
   """
   Return bake time remaining.

   This function takes one numbers representing the time in minutes the lasagna have been in the oven and
   calculates the remaining cooking time in minutes.
   """ 
   time_remaining = int(EXPECTED_BAKE_TIME) - int(elapsed_bake_time)
   print(time_remaining)
   return(time_remaining);

PREPARATION_TIME = 2

def preparation_time_in_minutes(number_of_layers):
    """
    Return final preparation time.

    This function takes one numbers representing the number of layers and calculates the preparation
    time in minutes for the lasagna.
    """
    final_prep_time = int(number_of_layers)*int(PREPARATION_TIME)
    print(final_prep_time)
    return(final_prep_time);

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    final_prep_time = number_of_layers*PREPARATION_TIME
    time_remaining = elapsed_bake_time + final_prep_time
    print(time_remaining)
    return(time_remaining);

    
    


