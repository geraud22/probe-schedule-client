Use client.py to conveniently authenticate with, and query endpoints of the [Probe Schedule South Africa API](https://probeschedule.co.za/).
- Positional Arguments available:
    - login
    - farmlist
    - blocklist
    - devicelist
    - devicestatus
    - devicedata

As with any Python project, it is recommended to run this tool in a Virtual Environment.
Requires [Python](https://www.python.org/downloads/) to be installed locally.
- Create Virtual Environment (venv)
    ```
    python -m venv venv
    ```
- Activate Virtual Environment
    ```
    venv/Scripts/activate
    ```


1. Install package dependencies
```
pip install -r requirements.txt
```
2. Run client.py using any defined positional argument. For example:
```
python client.py -h
```