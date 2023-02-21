# Viable Data tech test
## Setup for running applications and tests
Activate virtual environment and install dependencies
```
source venv/bin/activate
pip3 install -r requirements.txt
```

### Run application
```
python3 manage.py runserver
```

Navigate to `http://localhost:8000/api/` to view the API schema

### Run tests
```
export DJANGO_SETTINGS_MODULE=viabledata.settings
pytest
```

## Notes
* I used DRF Spectacular which automatically generates the Open API spec and uses it to serve a working API client on a specific URL. This makes it easy to develop as you can see your changes quickly and can even play with the API. It also importantly documents the API and since it's autogenerated from the code, it's never out-of-date.
* I used `black`, `isort` and `autoflake` for linting. In a real project these would be configured using a pyproject.toml file and be a part of pre-commit hooks. The result would be that all committed code would automatically be linted in a consistent way, avoiding unimportant discussions over code formatting.
* The deserialized representation of a company is quite big and extensive. It could be simpler – for example, instead of the `tax_infos` value being an array of tax info objects which contain the id, company ID, type (NINO or SSN), value, it could simply be an array of the values. This would depend on how the API is intended to be used by the client. Also, there is no reason why we couldn't have multiple serializers for the company object which would each be used depending on the use case. This would help ensure the application is performant and doesn't waste database queries or have an unnecessarily large payload size. 
* There is a `prefetch_related` added to the company view so Django will join the relevant tables when fetching the objects from the database. This prevents the need for multiple queries which would slow down the API.

## Assumptions made

## What I would change with more time
* Add a users app and a custom users model depending on what the project requirements are.
* The application only supports updating fields on the company model (such as email address, name etc.), not any of the related models like bank accounts, trades, tax info etc. Adding support for that would involve creating DRF viewsets for each of the models so in the interest of saving time, I opted to not do this.
* Add validation to the fields. Examples:
  * Sort code should be 6 digits
  * National Insurance number should follow the rules (regex-based validation would be sufficient)
* Add a static type checker such as `mypy` to enforce type safety. I didn't add it because getting it to behave with Django takes a bit of time and I didn't want to spend extra time doing that. 
