"""

For this example to work we need to have installed selenium, to do this just

     pip install selenium

If you have firefox instaled and want to debug, you dont need to do anithing else.  but if you have installed
http://phantomjs.org/ you can do this headless.

#########################################################################################
# TO USE THIS EXAMPLE  YOU HAVE TO ADD YOUR USERNAME, PASSWORD AND CHECKID FOR THE RUM
#########################################################################################

Simple usage


PINGDOM_USERNAME='xxx@yyy.com' PINGDOM_PASSWORD='p4ssword' PINGDOM_CHECKID='5778' python examples/with_pingdomdriver.py

"""


import os
import time

from pyngdom import PyngdomDriver

PINGDOM_USERNAME = os.getenv('PINGDOM_USERNAME', None)
PINGDOM_PASSWORD = os.getenv('PINGDOM_PASSWORD', None)
PINGDOM_CHECKID = os.getenv('PINGDOM_CHECKID', None)


with PyngdomDriver(username=PINGDOM_USERNAME, password=PINGDOM_PASSWORD) as pingdom:

    print "Getting TODAY's data"

    today = pingdom.today_rum(PINGDOM_CHECKID)

    print "today's average RUM is %(average)s ms (%(count)s views)" % today['total']
    print

    print "Getting REALTIME data"

    # getting 120 seconds realtime (the default is 60)
    realtime = pingdom.realtime_rum(PINGDOM_CHECKID, sample_interval=120)

    print "you're 2 minutes average RUM is %(average)s ms (%(count)s views)" % realtime['total']

    print "Getting five 15 second interval REALTIME rum"

    t0 = time.time()
    for n, result in enumerate(pingdom.iter_realtime_rum(PINGDOM_CHECKID, sample_interval=15, iterations=5)):
        print "%s (%.1f) : %s ms (%s views) " % (
            n, time.time() - t0, result['total']['average'], result['total']['count']
        )
