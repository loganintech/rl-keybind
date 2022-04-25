import os

new_lines = []

path = os.path.join(os.path.expanduser("~/Documents/My Games/Rocket League/TAGame/Config"), "TAInput.ini")
if not os.path.exists(path):
    path = os.path.join(os.path.expanduser("~/OneDrive/Documents/My Games/Rocket League/TAGame/Config"), "TAInput.ini")

with open(path) as TAInput:
    lines = TAInput.readlines()

    for line in lines:
        line = line.strip()
        if line == """GamepadBindings=( Action="RollRight" )""":
            new_lines.append("""GamepadBindings=( Action="RollRight", Key="XboxTypeS_RightShoulder" )""")
        elif line == """GamepadBindings=( Action="RollLeft" )""":
            new_lines.append("""GamepadBindings=( Action="RollLeft", Key="XboxTypeS_LeftShoulder" )""")
        elif line == """GamepadBindings=( Action="Handbrake",				Key="XboxTypeS_X", bRequired=true )""":
            new_lines.append("""GamepadBindings=( Action="Handbrake",	Key="XboxTypeS_RightShoulder", bRequired=true )""")
            new_lines.append("""GamepadBindings=( Action="Handbrake",	Key="XboxTypeS_LeftShoulder", bRequired=true )""")
        elif line == """GamepadBindings=( Action="ToggleScoreboard",		Key="XboxTypeS_LeftShoulder",	bRequired=true )""":
            new_lines.append("""GamepadBindings=( Action="ToggleScoreboard",		Key="XboxTypeS_Back",	bRequired=true )""")
        elif line == """GamepadBindings=( Action="ResetTraining",			Key="XboxTypeS_RightShoulder" )""":
            new_lines.append("""GamepadBindings=( Action="ResetTraining",			Key="XboxTypeS_X" )""")
        elif line == """GamepadBindings=( Action="FreeplayBallInFront",	Key="XboxTypeS_DPad_Down" )""":
            new_lines.append("""#GamepadBindings=( Action="FreeplayBallInFront",	Key="XboxTypeS_DPad_Down" )""")
        elif line == """GamepadBindings=( Action="FreeplayDefendShot",		Key="XboxTypeS_LeftShoulder" )""":
            new_lines.append("""GamepadBindings=( Action="FreeplayDefendShot",		Key="XboxTypeS_DPad_Down" )""")
        elif line == """GamepadBindings=( Action="NextPickup",				Key="XboxTypeS_RightShoulder" )""":
            new_lines.append("""GamepadBindings=( Action="NextPickup",				Key="XboxTypeS_X" )""")
        elif line == """GamepadBindings=( Action="ToggleRoll",				Key="XboxTypeS_LeftTrigger" )""":
            new_lines.append("""#GamepadBindings=( Action="ToggleRoll",				Key="XboxTypeS_LeftTrigger" )""")
        else:
            new_lines.append(line)

with open(path, "w") as f:
    for line in new_lines:
        f.write(line + "\n")