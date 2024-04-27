import sys

sys.path.append("/dev-py-packages")
from firepup650 import inputCast, clear

clear()
print("Buckshot Roulette tracker")
while 1:
    print("Please enter the shells for this round.")
    print("How many live shells?")
    live = inputCast("> ", int)
    print("How many blank shells??")
    blank = inputCast("> ", int)
    total = blank + live
    round = 1
    known = {}
    for i in range(total):
        known[str(i + 1)] = ""
    while total:
        clear()
        if known[str(round)]:
            print(f"Known Shell! Shell is {known[str(round)]}")
        print(
            f"""Chance of live shell:	{(live/(live+blank if live+blank>0 else 1))*100}%
Chance of blank shell:	{blank/(live+blank if live+blank>0 else 1)*100}%
Shells left:		{total} ({blank}B {live}L)
Next shell is?"""
        )
        next = inputCast("> ").upper()
        if next in ["B", "L"]:
            blank = blank - 1 if next == "B" and not known[str(round)] else blank
            live = live - 1 if next == "L" and not known[str(round)] else live
            total -= 1
            round += 1
        elif "=" in next:
            num = next.split("=")[0]
            color = next.split("=")[1]
            known[num] = "live" if color.upper() == "L" else "blank"
            blank = blank - 1 if color == "B" else blank
            live = live - 1 if color == "L" else live
        elif next == "0":
            break
    print("Round End\nExit? (y|N)")
    if inputCast("> ").lower().startswith("y"):
        break
    clear()
