def main():
	name = "Ujjwal Tamhankar"
	age = 27 # not a lie
	height = 84 # inches
	height_m = height * 0.0254
	weight = 195 # lbs
	weight_kg = round(weight * .453)
	eyes = "Brown"
	teeth = "White"
	hair = "Brown"

	print(f"Let's talk about {name}.")
	print(f"He's {height_m} m tall.")
	print(f"He's {weight_kg} kgs heavy.")
	print("Actually that's not too heavy.")
	print(f"He's got {eyes} eyes and {hair} hair.")
	print(f"His teeth are usually {teeth} depending on the coffee.")

	# This line is tricky, try to get it exactly right.
	total = age + height + weight
	print(f"If I add {age}, {height}, and {weight} I get {total}.")

if __name__ == "__main__":
	main()
