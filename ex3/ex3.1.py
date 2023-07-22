# This is to calculate the tip at the total bill at a restaurant.

def main(base, pct):
	tip = base * pct

	total_cost = base + tip

	print(f"Your base price is {base} with a {pct*100}% tip. Your total bill comes to ${total_cost}")

if __name__ == "__main__":
	base = 57.79
	pct = .2
	main(base, pct)