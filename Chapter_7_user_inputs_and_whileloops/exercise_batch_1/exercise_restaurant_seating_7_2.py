group_amount = input("\nHow many people are in your group? ")
group_amount = int(group_amount)

if group_amount >= 8:
    print("\nYou will have to wait for a table")
else:
    print("\nThe table is ready")
