
test:
	pylint -E build_site.py

site: clean
	mkdir pub
	python build_site.py

clean:
	rm -fR pub
