# Contributing to the Gateway

Welcome! this document contains details on all you need to know
about contributing to the gateway.

# Code Styling
We use Flake8 to lint the code, make sure your code doesn't trigger
errors or warnings from flake8.

You can use flake8 cli to check a file, or a directory for styling
mistakes

```
$ flake8 file.py
```

You should also use Black for formatting your code
```
$ black file.py
```

# Multi-line expressions for better readability 
Sometimes we split part of the code into multi lines for better
readability even when it fits the screen, Black by default will
automatically convert it to one line, for example

```python
employee = get_employee_by_email(
    session=session,
    sub_domain=credentials.sub_domain,
    email=credentials.email
)
# will be
employee = get_employee_by_email(session=session, sub_domain=credentials.sub_domain, email=credentials.email)
```
To make Black understand that we intentionally split it,
simply add a `,` at the end.
```python
email=credentials.email,
```