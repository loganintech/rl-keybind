import os
import re

new_lines = []
changes = []


def norm(s):
    return re.sub(r"\s+", " ", s.strip())


candidates = [
    os.path.expanduser(
        "~/.local/share/Steam/steamapps/compatdata/252950/pfx/drive_c/users/steamuser/Documents/My Games/Rocket League/TAGame/Config/TAInput.ini"
    ),
    os.path.expanduser("~/Documents/My Games/Rocket League/TAGame/Config/TAInput.ini"),
]

path = next((p for p in candidates if os.path.exists(p)), None)
if path is None:
    raise FileNotFoundError("Could not find TAInput.ini in any known location")

with open(path) as TAInput:
    lines = TAInput.readlines()

    for i, line in enumerate(lines, 1):
        line = line.strip()
        if norm(line) == norm('GamepadBindings=( Action="RollRight" )'):
            new_lines.append(
                'GamepadBindings=( Action="RollRight", Key="XboxTypeS_RightShoulder" )'
            )
            changes.append((i, line, new_lines[-1]))
        elif norm(line) == norm('GamepadBindings=( Action="RollLeft" )'):
            new_lines.append(
                'GamepadBindings=( Action="RollLeft", Key="XboxTypeS_LeftShoulder" )'
            )
            changes.append((i, line, new_lines[-1]))
        elif norm(line) == norm(
            'GamepadBindings=( Action="Handbrake", Key="XboxTypeS_X", bRequired=true )'
        ):
            new_lines.append(
                'GamepadBindings=( Action="Handbrake", Key="XboxTypeS_RightShoulder", bRequired=true )'
            )
            new_lines.append(
                'GamepadBindings=( Action="Handbrake", Key="XboxTypeS_LeftShoulder", bRequired=true )'
            )
            changes.append((i, line, new_lines[-2] + "\n  + " + new_lines[-1]))
        elif norm(line) == norm(
            'GamepadBindings=( Action="ToggleScoreboard", Key="XboxTypeS_LeftShoulder", bRequired=true )'
        ):
            new_lines.append(
                'GamepadBindings=( Action="ToggleScoreboard", Key="XboxTypeS_Back", bRequired=true )'
            )
            changes.append((i, line, new_lines[-1]))
        elif norm(line) == norm(
            'GamepadBindings=( Action="ResetTraining", Key="XboxTypeS_RightShoulder", PressType=BPT_Tap )'
        ):
            new_lines.append(
                'GamepadBindings=( Action="ResetTraining", Key="XboxTypeS_X", PressType=BPT_Tap )'
            )
            changes.append((i, line, new_lines[-1]))
        elif norm(line) == norm(
            'GamepadBindings=( Action="FreeplayBallInFront", Key="XboxTypeS_DPad_Down" )'
        ):
            new_lines.append(
                '#GamepadBindings=( Action="FreeplayBallInFront", Key="XboxTypeS_DPad_Down" )'
            )
            changes.append((i, line, new_lines[-1]))
        elif norm(line) == norm(
            'GamepadBindings=( Action="FreeplayDefendShot", Key="XboxTypeS_LeftShoulder" )'
        ):
            new_lines.append(
                'GamepadBindings=( Action="FreeplayDefendShot", Key="XboxTypeS_DPad_Down" )'
            )
            changes.append((i, line, new_lines[-1]))
        elif norm(line) == norm(
            'GamepadBindings=( Action="NextPickup", Key="XboxTypeS_RightShoulder" )'
        ):
            new_lines.append(
                'GamepadBindings=( Action="NextPickup", Key="XboxTypeS_X" )'
            )
            changes.append((i, line, new_lines[-1]))
        elif norm(line) == norm(
            'GamepadBindings=( Action="ToggleRoll", Key="XboxTypeS_LeftTrigger" )'
        ):
            new_lines.append(
                '#GamepadBindings=( Action="ToggleRoll", Key="XboxTypeS_LeftTrigger" )'
            )
            changes.append((i, line, new_lines[-1]))
        else:
            new_lines.append(line)

if changes:
    print(f"Modifying {path}")
    print(f"{len(changes)} change(s):\n")
    for lineno, old, new in changes:
        print(f"  Line {lineno}:")
        print(f"    - {old}")
        print(f"    + {new}")
        print()
    with open(path, "w") as f:
        for line in new_lines:
            f.write(line + "\n")
    print("Done.")
else:
    print("No changes needed (bindings already applied).")
