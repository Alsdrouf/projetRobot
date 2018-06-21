#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging
import cgi
formData = cgi.FieldStorage()
#cgi.test()
print "Content-type:text/html\r\n\r\n"

print '<html><body>'
print 'action=', formData.getvalue("action")
print '<br>'
print 'slider=', formData.getvalue("slider")
cgi.print_form(formData)
print '</body></html>'

