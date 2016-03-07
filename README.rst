etao
====
.. image:: https://travis-ci.org/jamchamb/etao.svg?branch=master
    :target: https://travis-ci.org/jamchamb/etao
.. image:: https://badge.fury.io/py/etao.svg
    :target: https://badge.fury.io/py/etao

etao is a simple Python library that assists in the creation
of cryptanalysis tools.

Installation
------------
Install with pip::

    pip install etao

Example Application
-------------------
The following is a Caesar cipher solving tool that uses etao's frequency
analysis functions and built-in ciphers.

.. code:: python

 #!/usr/bin/env python
 # Caesar cipher solver
 import argparse
 import etao


 def main():
     parser = argparse.ArgumentParser(description="Caesar cipher solver")
     parser.add_argument('ciphertext', type=str, help='text to decipher')

     args = parser.parse_args()

     # Get every Caesar shift of the ciphertext
     shifts = map(lambda x: etao.caesar_shift(args.ciphertext, x), range(26))

     # Score each shift according to English character frequency.
     # Get tuples that pair the score with the text.
     scored_shifts = map(lambda x: (etao.score_text(x), x), shifts)

     # Sort by score, descending order
     scored_shifts.sort(reverse=True)

     # Print the top 3 results
     for result in scored_shifts[0:3]:
         print '"%s" (%02d%%)' % (result[1], int(result[0] * 100))

 if __name__ == "__main__":
     main()

Here's what it looks like in action:

.. code-block:: console

    $ ./caesar_solver.py "O GQFSOAWBU QCASG OQFCGG HVS GYM. WH VOG VODDSBSR PSTCFS, \
    PIH HVSFS WG BCHVWBU HC QCADOFS WH HC BCK."
    "A SCREAMING COMES ACROSS THE SKY. IT HAS HAPPENED BEFORE, BUT THERE IS NOTHING
    TO COMPARE IT TO NOW." (95%)
    "L DNCPLXTYR NZXPD LNCZDD ESP DVJ. TE SLD SLAAPYPO MPQZCP, MFE ESPCP TD YZESTYR
    EZ NZXALCP TE EZ YZH." (65%)
    "P HRGTPBXCV RDBTH PRGDHH IWT HZN. XI WPH WPEETCTS QTUDGT, QJI IWTGT XH CDIWXCV
    ID RDBEPGT XI ID CDL." (65%)
