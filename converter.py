def convertNumberToEnglishText(n):
	ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
			'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	tens = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

	# negative numbers
	if n < 0:
		return f"negative {convertNumberToEnglishText(abs(n))}"

	# 1000+ numbers
	for order, word in [(10 ** 3, "thousand")]:
		if n >= order:
			thousands = convertNumberToEnglishText(n // order)
			after_thousands = convertNumberToEnglishText(n % order) if n % order else ''
			return f"{thousands} {word} {after_thousands}".strip()

	# from 100 to 999
	if n >= 100:
		if n % 100:
			return f"{convertNumberToEnglishText(n // 100)} hundred {convertNumberToEnglishText(n % 100)}"
		else:
			return f"{convertNumberToEnglishText(n // 100)} hundred"

	# from 0 to 99
	if n < 20:
		return ones[n]
	else:
		with_no_remainder = tens[n // 10]
		after_tens = convertNumberToEnglishText(n % 10) if n % 10 else ''
		return f"{with_no_remainder} {after_tens}".strip()
