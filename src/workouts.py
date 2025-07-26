def ctsTest():
    return """
--- CTS Test:

Warm up
- 5' @ Z1
- 5' @ Z2

Spin ups
- 1' @ Z3
- 3' @ Z1
- 1' @ Z4
- 3' @ Z1
- 1' @ Z5

Recovery
- 5' @ Z1

First test interval
- First test interval 8' @ Z4-Z5

Recovery
- 10' @ Z1

Second test interval
- Second test interval 8' @ Z4-Z5

Cool down
- 10' @ Z1
"""