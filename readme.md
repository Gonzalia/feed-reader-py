# Feed Reader (OOP Project)

### How to run
1. You need to install [Python 3.x](https://www.python.org/downloads/)

```sudo apt install python3 ```

2. Install [pip](https://pypi.org/project/pip/)

```python3 install pip```

3. Run the requirements.txt file

```pip install -r requirements.txt```

4. Run the `feed_reader_main.py` file

```python3 feed_reader_main.py```


### Project summary

* The file `src/parser/subscription_parser.py` reads the `config/subscription.json` file
* Then the `src/httpRequest/http_requester.py` downloads the xml from the link passed by parameter
* `src/parser/rss_parser.py` returns a list of articles who contains all the articles received from the http request


All classes contains a test, to run this 
```python3 class_file.py```
 