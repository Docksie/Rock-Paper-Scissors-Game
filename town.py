# ============================================================
# STUDENT IMPLEMENTATION FILE
# Complete each function below according to its docstring.
# Do not change the provided function names or parameters.
# ============================================================

from text import (
    MAIN_SCREEN,
    VALID_MAIN_CHOICES,
    MAIN_REPEAT_MESSAGE
)

from game_utils import Player


def display_stats(player: Player):
    """
    Display the player's current statistics and inventory.

    The function should display:
    - current gold
    - current health
    - minimum damage
    - maximum damage

    If at least one item is owned, display an INVENTORY heading
    followed by only the items whose ownership flags are True.
    If no items are owned, do not display the INVENTORY heading.
    Displaying information must not change any player attributes.

    The inventory should display each item the player currently owns:
    - Weighted Rock
    - Paper Armor
    - Sharpened Scissors
    - Crown of the Three Hands

    After displaying the player's information, pause until the
    player presses Enter.

    Args:
        player: The Player object representing the current player.
    """

    # Display the player's current stats.
    # HINT: Look at the attributes available in the Player class.
    print(f"Money:      {player.money}")
    print(f"Health:     {player.health}")
    print(f"Min Damage: {player.min_damage}")
    print(f"Max Damage: {player.max_damage}")

    # Only display INVENTORY if the player owns at least one item.
    #
    # HINT:
    # Use "or" to check the player's item attributes.
    if (player.has_crown or player.has_paper_armor or player.has_sharpened_scissors or player.has_weighted_rock):
        print("\nINVENTORY:")

        # Check each item separately.
        # If the player owns it, display its name.

        if player.has_weighted_rock:
            print("- Weighted Rock")

        if player.has_paper_armor:
            print("- Paper Armor")

        if player.has_sharpened_scissors:
            print("- Sharpened Scissors")

        if player.has_crown:
            print("- Crown of the Three Hands")

    # Pause before returning to the town menu.
    input("\nPress Enter to continue...")


def chose_what_to_do(player: Player) -> str:
    """
    Display the main town menu and ask the player what they want to do.

    The function should:
    1. Display the player's current statistics and inventory using
       display_stats().
    2. Display the main menu.
    3. Include the player's name in the main menu message.
    4. Ask the player to choose an action.
    5. Validate the player's choice.
    6. Continue asking until a valid choice is entered.
    7. Return the valid choice.

    Args:
        player: The Player object representing the current player.

    Returns:
        The validated choice as a string:
        - "1" for shopping
        - "2" for fighting
        - "3" for resting
        - "exit" for quitting
    """

    # First, display the player's stats and inventory.
    ...

    # MAIN_SCREEN contains the placeholder:
    # ~PLAYERNAME~
    #
    # Replace it with the player's actual name.
    #
    # HINT:
    # my_string.replace("old text", "new text")
    main_message = MAIN_SCREEN.replace("~PLAYERNAME~", player.name)

    # Display the menu and get the player's choice.
    game_state = input(main_message)

    # Validate the player's choice.
    while game_state not in VALID_MAIN_CHOICES:
        game_state = input(MAIN_REPEAT_MESSAGE)

    # Return the validated choice to game.py.
    return game_state