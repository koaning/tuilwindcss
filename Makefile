black:
	black tuilwindcss

isort:
	isort tuilwindcss
	isort ./*.py
	isort docs/examples/*.py

clean: black isort
	rm -rf *.svg