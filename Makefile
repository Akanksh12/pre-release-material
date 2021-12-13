run:
	python *.py
commit:
	echo "Enter the commit message\n"
	read message
	git add . ; git commit -m "$message"


