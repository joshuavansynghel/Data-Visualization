from plotly import colors

for key, value in colors.PLOTLY_SCALES.items():
	print(f"\nKey: {key} with values:")
	for color in value:
		print(color)