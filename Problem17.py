num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}

def main():
	total_letters = 0
	for number in xrange(1, 1000):
		if 1 <= number < 20:
			print num2words[number], number
			total_letters += len(num2words[number])
		elif 10 <= number < 100:
			if number in num2words:
				print num2words[number], number
				total_letters += len(num2words[number])
			else:
				print (num2words[(number / 10)*10] + ' ' + num2words[number % 10]), number
				total_letters += sum(len(x.strip()) for x in (num2words[(number / 10)*10] + ' ' + num2words[number % 10]).split())
		else:
			answer = ""
			answer += num2words[(number / 100)] + ' hundred'
			if str(number)[1] == '0' and str(number)[2] == '0':
				print answer
				total_letters += sum(len(x.strip()) for x in answer.split())
			else:
				number = number % 100
				if 1 <= number < 20:
					answer += ' and ' + num2words[number]
				elif len(str(number)) == 2:
					answer += ' and ' + num2words[(number / 10)*10]
					if number % 10 != 0:
						answer += ' ' + num2words[number % 10]
				print answer
				total_letters += sum(len(x.strip()) for x in answer.split())
	total_letters += sum(len(x.strip()) for x in 'One thousand'.split())
	print "One thousand"
	print total_letters
if __name__ == '__main__':
	main()