## [Chinese Names Search Web App](https://chinese-names-cibfpxoeya-uc.a.run.app)

This web app is used to search Chinese Names and returning multiple features of Chinese surnames and Chinese given names
for scientific research (e.g., name uniqueness, name gender, name valence, and name warmth/competence).

More information about the R package that this web app is based on can be
found [here](https://github.com/psychbruce/ChineseNames/blob/main/README.md).

### Requirements

- Python 3.11
- Flask 2.3.3
- pandas 2.0.3
- rpy2 3.5.1
- gunicorn 21.2.0
- R 4.1.2

### Usage

```
docker build -t chinese-names-search-website .
```

```
docker run -d -p 8000:8000 chinese-names-search-website
```
