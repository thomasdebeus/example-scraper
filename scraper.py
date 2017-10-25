###############################################################################
# START HERE: Tutorial 2: Basic scraping and saving to the data store.
# Follow the actions listed in BLOCK CAPITALS below.
###############################################################################
# -*- coding: utf-8 -*-
import scraperwiki
html = scraperwiki.scrape('http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm')

# -----------------------------------------------------------------------------
# 1. Parse the raw HTML to get the interesting bits - the part inside <td> tags.
# -- UNCOMMENT THE 6 LINES BELOW (i.e. delete the # at the start of the lines)
# -- CLICK THE 'RUN' BUTTON BELOW
# Check the 'Console' tab again, and you'll see how we're extracting 
# the HTML that was inside <td></td> tags.
# We use lxml, which is a Python library especially for parsing html.
# -----------------------------------------------------------------------------

import lxml.html           
root = lxml.html.fromstring(html)
for tr in root.cssselect("div[align='left'] tr"):
    tds = tr.cssselect("td")
    if len(tds)==12:
        data = {
            'country' : tds[0].text_content(),
            'years_in_school' : int(tds[4].text_content())
        }
        scraperwiki.sqlite.save(unique_keys=['country'], data=data)
        

# -----------------------------------------------------------------------------
# The datastore is a magic SQL store, one where you don't need to make a schema up front.
# Replace print data in the lxml loop with this save command (make sure you keep it indented with spaces at the start like this): 
# -----------------------------------------------------------------------------

# scraperwiki.sqlite.save(unique_keys=['country'], data=data)
    
# -----------------------------------------------------------------------------
# Go back to the Tutorials page and continue to Tutorial 3 to learn about 
# more complex scraping methods.
# -----------------------------------------------------------------------------
