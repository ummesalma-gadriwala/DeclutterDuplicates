# change directory to intended directory
directory = test_images

# default is safe
safe: $(directory)
	mkdir $(directory).backup
	cp $(directory)/* $(directory).backup
	python src/declutterer.py $(directory)

declutter: $(directory)
	python src/declutterer.py $(directory)

restore: $(directory)
	cp $(directory).backup/* $(directory)
	rm -r $(directory).backup

clean:
	rm -f *.pyc
	rm -f -r *.backup
