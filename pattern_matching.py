

def run_action_old(user_input: list) -> None:
    if isinstance(user_input, list) and len(user_input) == 2:
        action, value = user_input
        print(f"Action={action}, value={value}")
    else:
        print("Wrong command")


def run_action(user_input: list) -> None:
    match user_input:
        case "left", value if int(value) > 50:
            print("You fell from the battlefield!")
        case "left" | "right" | "top" | "bottom" as action, value:
            print(f"Go to {action} to {value}px")
        case "shoot", *coords:
            print(f"Shoot by coords: {coords}")
        case "quit", :    # unpacking first element from the list by "," after command "quit"
            print("Goodbye!")
        case _:
            print("Wrong command")


run_action("left 75".split())
run_action("right 100".split())
run_action("shoot 10 15 20".split())
run_action("quit".split())


# -----------------------------------------------------
user_action = {
    "id": 21,
    "action": "left",
    "value": 50,
    "timestamp": 3939020855,
    "user_group": 11,
    "cash": 5_000_000,
}

match user_action:    # check if user_action has proper action and value fields. Ignore other fields.
    case {"action": str(action), "value": int(value)}:
        print(f"{action=}, {value}")


# -----------------------------------------------------
class UserInput:
    def __init__(self, action: str, value: int):
        self.action = action
        self.value = value


def run_horizontally(user_input: UserInput | dict):    # user_input can be class instance or dictionary
    match user_input:
        case UserInput(action="left" | "right", value=value):
            print(f"Moving horizontally on {value}px.")
        case {"action": "left" | "right", "value": value}:
            print(f"Moving horizontally on {value}px.")
        case _:
            pass


input_1 = UserInput("left", 150)
input_2 = {"action": "right", "value": 200}
input_3 = UserInput("top", 20)

run_horizontally(input_1)
run_horizontally(input_2)
run_horizontally(input_3)
