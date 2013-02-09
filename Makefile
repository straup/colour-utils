clean:
	rm -f palettes/*-rainbow.png

wikipedia:
	python/merge-palettes.py palettes/wikipedia-blue.json palettes/wikipedia-red.json palettes/wikipedia-yellow.json palettes/wikipedia-orange.json palettes/wikipedia-green.json palettes/wikipedia-pink.json palettes/wikipedia-brown.json palettes/wikipedia-violet.json palettes/wikipedia-white.json palettes/wikipedia-grey.json > palettes/wikipedia.json

cooperhewitt:
	python/merge-palettes.py palettes/cooperhewitt-blue.json palettes/cooperhewitt-red.json palettes/cooperhewitt-yellow.json palettes/cooperhewitt-orange.json palettes/cooperhewitt-green.json palettes/cooperhewitt-pink.json palettes/cooperhewitt-brown.json palettes/cooperhewitt-violet.json palettes/cooperhewitt-white.json palettes/cooperhewitt-grey.json > palettes/cooperhewitt.json

rainbows:
	python/make-rainbow.py palettes/crayola.json palettes/crayola-rainbow.png
	python/make-rainbow.py palettes/css3.json palettes/css3-rainbow.png
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
	python/make-rainbow.py palettes/cooperhewitt-blue.json palettes/cooperhewitt-blue-rainbow.png
	python/make-rainbow.py palettes/cooperhewitt-red.json palettes/cooperhewitt-red-rainbow.png
	python/make-rainbow.py palettes/cooperhewitt-yellow.json palettes/cooperhewitt-yellow-rainbow.png
	python/make-rainbow.py palettes/cooperhewitt-orange.json palettes/cooperhewitt-orange-rainbow.png
	python/make-rainbow.py palettes/cooperhewitt-green.json palettes/cooperhewitt-green-rainbow.png
	python/make-rainbow.py palettes/cooperhewitt-pink.json palettes/cooperhewitt-pink-rainbow.png
	python/make-rainbow.py palettes/cooperhewitt-brown.json palettes/cooperhewitt-brown-rainbow.png
	python/make-rainbow.py palettes/cooperhewitt-violet.json palettes/cooperhewitt-violet-rainbow.png
	python/make-rainbow.py palettes/cooperhewitt-grey.json palettes/cooperhewitt-grey-rainbow.png
	python/make-rainbow.py palettes/cooperhewitt-white.json palettes/cooperhewitt-white-rainbow.png
