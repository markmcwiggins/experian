# experian
Experian interview code

The code common_letters.py is a standalone test; you can run it by itself.

The parsing code is a little more involved:

python -m lark.tools.standalone simplepy.g >standalone.py

Then

python3 ./transform.py lib/codesample.py

I'm enclosing a shell script to run both of them:

parseit.sh

I simplified the codesample from its original; it's been about 7 years since I used this toolkit and I've forgotten some of the details like smoothly handling Python comments and docstrings ... these are now left as an exercise for the reader.

Questions? Comments?

Email: mark@pythonsoftwarewa.com
Phone: 425-369-8286

Thanks!


