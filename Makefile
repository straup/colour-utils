clean:
	rm -f palettes/*-rainbow.png

wikipedia:
	python/merge-palettes.py palettes/wikipedia-blue.json palettes/wikipedia-red.json palettes/wikipedia-yellow.json palettes/wikipedia-orange.json palettes/wikipedia-green.json palettes/wikipedia-pink.json palettes/wikipedia-brown.json palettes/wikipedia-violet.json palettes/wikipedia-white.json palettes/wikipedia-grey.json > palettes/wikipedia.json

rainbows:
	python/make-rainbow.py palettes/wikipedia-blue.json palettes/wikipedia-blue-rainbow.png
	python/make-rainbow.py palettes/wikipedia-red.json palettes/wikipedia-red-rainbow.png
	python/make-rainbow.py palettes/wikipedia-yellow.json palettes/wikipedia-yellow-rainbow.png
	python/make-rainbow.py palettes/wikipedia-orange.json palettes/wikipedia-orange-rainbow.png
	python/make-rainbow.py palettes/wikipedia-green.json palettes/wikipedia-green-rainbow.png
	python/make-rainbow.py palettes/wikipedia-pink.json palettes/wikipedia-pink-rainbow.png
	python/make-rainbow.py palettes/wikipedia-brown.json palettes/wikipedia-brown-rainbow.png
	python/make-rainbow.py palettes/wikipedia-violet.json palettes/wikipedia-violet-rainbow.png
	python/make-rainbow.py palettes/wikipedia-grey.json palettes/wikipedia-grey-rainbow.png
	python/make-rainbow.py palettes/wikipedia-white.json palettes/wikipedia-white-rainbow.png
	python/make-rainbow.py palettes/crayola.json palettes/crayola-rainbow.png
	python/make-rainbow.py palettes/css3.json palettes/css3-rainbow.png
