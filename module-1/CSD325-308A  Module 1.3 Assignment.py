"""
Assignment: On the Wall + Flowchart(s)
Implements the "N Bottles of Beer on the Wall" countdown song, 
handling singular and plural bottle counts.
"""

def get_bottle_phrase(count):
    """
    Returns the appropriate phrase for the number of bottles.

    Args:
        count (int): The current number of bottles.

    Returns:
        str: The complete phrase (e.g., "1 bottle", "5 bottles", "no more bottles").
    """
    if count == 1:
        return "1 bottle of beer"
    elif count > 1:
        return f"{count} bottles of beer"
    else: # count == 0
        return "no more bottles of beer"

def countdown_song(start_bottles):
    """
    Manages the countdown song from the starting number down to 1.

    Args:
        start_bottles (int): The initial number of bottles.
    """
    bottles_on_wall = start_bottles

    # Loop while there are still bottles to sing about
    while bottles_on_wall > 0:

        # Determine the phrase for the start of the verse (N)
        current_bottles_phrase = get_bottle_phrase(bottles_on_wall)

        # --- Verse Part 1 ---
        print(f"{current_bottles_phrase} on the wall, {current_bottles_phrase.lower().replace('on the wall, ', '')}.")

        # Decrement for the next step
        bottles_on_wall -= 1

        # Determine the phrase for the end of the verse (N-1)
        next_bottles_phrase = get_bottle_phrase(bottles_on_wall)

        # --- Verse Part 2 ---
        if bottles_on_wall > 0:
            # Standard verse continuation (N-1 is 1 or more)
            print(f"Take one down and pass it around, {next_bottles_phrase.lower()} on the wall.")
            print("-" * 30)
        else:
            # Final verse conclusion (N-1 is 0)
            print(f"Take one down and pass it around, {next_bottles_phrase.lower()} on the wall.")

    # Final, unique ending verse when the count hits zero
    print("\nNo more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall!")


# --- Main Program ---
if __name__ == "__main__":

    print("--- Bottles of Beer Countdown ---")

    try:
        # 1. Ask the user for the starting number of bottles
        user_input = input("How many bottles of beer are on the wall? ")
        initial_count = int(user_input)

        # Input validation
        if initial_count <= 0:
            print("Please enter a positive number of bottles to start the song.")
        else:
            # 2. Pass that input to a function that manages the countdown
            countdown_song(initial_count)

            # 6. Get back to the main program and remind the user to buy more beer
            # (This part is handled by the final lines printed in countdown_song, 
            # but we can add a final, clear main-program message)
            print("\n--- Program Complete ---")
            print("Don't forget to buy more beer!")

    except ValueError:
        print("Invalid input. Please enter a whole number for the number of bottles.")
