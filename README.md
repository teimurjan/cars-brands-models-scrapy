#cars-brands-models-scrapy
It's a scrapy for getting json with cars' brands and models from [auto.ru](https://auto.ru/). 
Result json's format is `{"carBrand": ["carModel1", "carModel2"]}`.

## Installation
* Install python3
* Download [chromedriver](http://chromedriver.chromium.org/)
* Run
```sh
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python main.py -o result.json
```