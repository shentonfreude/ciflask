ciflask
=======

Testing out CI tools with a simple flask app

Install
=======

    virtualenv .
    source bin/activate
    pip install -r requirements.txt

Run
===

Run the little script that starts up the app:

    ./run.py

and point your browser at

    http://localhost:5000

and see "Hello World"

Test
====

We've got a minimal test for a minimal app. Run it:

  
    py.test app

    ============================= test session starts ==============================
    platform darwin -- Python 2.7.6 -- py-1.4.21 -- pytest-2.5.2
    collected 1 items

    app/test_views.py .

    =========================== 1 passed in 0.08 seconds ===========================

Current DroneIO status
----------------------

[![Build Status](https://drone.io/github.com/shentonfreude/ciflask/status.png)](https://drone.io/github.com/shentonfreude/ciflask/latest)
