# flask-human-resource
demo website create by flask, blueprint, restful, sqlachemy and sqlite3



**Bước 1**: Tạo virtual environment, cài vào các thư viện sau:
```
pip install flask
pip install flask-sqlachemy
pip install flask_restful
pip install flask_cors
```

**Bước 2**: Tạo cấu trúc website:
HR application
```
    app.py
    settings.py
    config.ini
    dbconnect package
        __init__.py
    database folder
    users package
        users_model
        users_controller
        users_api
        users_view

    departments package
    ....
```

**Bước 3: ** Xây dựng cơ chế đọc/ghi database local (sqlite3)
Đọc đường dẫn đến database HR_sqlite3.db trong settings.py

>dbconnect/___ init __.py
```Python
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

```

>app.py
```Python
import settings
from dbconnect import database


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + settings.DB_PATH
database.init_app(app)

```

**Bước 4:** Xây dựng end-point: users_api
End-point được design dưới dạng:

/hr-api/users/<user_id>

/hr-api/users/

Bao gồm các function:

get_user

get_users

put_user

post_user

delete_user

