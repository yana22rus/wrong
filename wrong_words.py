import enchant
import requests
import re

def main():

	dictionary = enchant.Dict("ru_RU")

	with open("stop.txt") as f:
		
		f = set(f.read().split())

	lll = []
	d = {}
	link = input("Введите ссылку: ")

	number = int(''.join(x for x in list(link) if x.isdigit()))
	req_link = link[:-len(str(number))]

	for i in range(number,0,-1):
		r = requests.get(f"{req_link}{i}")


		if r.status_code == requests.codes.ok:
			
			r = ' '.join(r.text.split())
			text = re.sub('<[^<]+?>', '', r)
			text = re.sub('[^а-яёА-ЯЁ]', ' ', text).split()
			
			l = [x for x in text if len(x) > 4 and x.islower()]
			
			ll = [x for x in l if dictionary.check(x) == False]

			s = set(' '.join(set(ll)).split())
			
			sf = s-f
			
			if sf != set():

				d.update({f"{req_link}{i}": sf})

				print(*d.values())

	count = 0
	f = ""

	for x in list(link[8:]):
		if x == ".":
			count += 1
		if count == 2:
			break
		f += x



	with open(f + ".txt","a") as f:
		for key, value in d.items():
			print(key,*value,file=f,sep="\t")


if __name__ == '__main__':
	main()
