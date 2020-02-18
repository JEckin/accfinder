import mechanize
b = mechanize.Browser()
b._factory.is_html = True
b.set_handle_robots(False)
b.addheaders = [('User-agent','Mozilla/9.0 (X11; U; Linux i686; de-DE; rv:1.8.1.19) Gecko/20081202 Firefox (Debian-2.0.0.19-0etch1)')]
b.open("https://o1u.de/")
b.select_form(nr=0)
print b.form
#b.form['email'] = ""
#b.form['pass'] = ""
#b.method = "POST"
#submit = b.submit()
#if 'https://www.facebook.com/?sk=welcome' in submit.geturl():
#	print("Password Found")
#else :
#	print("False Login")
