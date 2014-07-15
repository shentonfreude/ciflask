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

  
    py.test --cov-report term-missing --cov app app
    ============================= test session starts ==============================
    platform darwin -- Python 2.7.6 -- py-1.4.21 -- pytest-2.5.2
    plugins: cov
    collected 2 items

    app/test_views.py ..
    --------------- coverage: platform darwin, python 2.7.6-final-0 ----------------
    Name             Stmts   Miss  Cover   Missing
    ----------------------------------------------
    app/__init__         3      0   100%   
    app/test_views       6      0   100%   
    app/views            6      0   100%   
    ----------------------------------------------
    TOTAL               15      0   100%   

    =========================== 2 passed in 0.11 seconds ===========================

Current DroneIO status
----------------------

[![Build Status](https://drone.io/github.com/shentonfreude/ciflask/status.png)](https://drone.io/github.com/shentonfreude/ciflask/latest)
