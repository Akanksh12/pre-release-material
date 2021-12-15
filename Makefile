run:
	./preReleaseMaterial.py
commit:
	echo "Enter the commit message"
	read message
	git add . ; git commit -m "$message"


