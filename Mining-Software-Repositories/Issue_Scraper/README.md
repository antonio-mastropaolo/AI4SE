## Environment setup

```shell
conda env create --name bug-triaging-env --file=environment.yml
conda activate bug-triaging-env
```

## Scraper

To run the scraper execute:

```shell
python3 main.py
```

To clean up the output folder run:

```shell
rm -rv out/*.json
```