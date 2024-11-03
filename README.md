# Django REST API Project

Một REST API đơn giản được xây dựng với Django REST Framework để quản lý sản phẩm (Products).

## Tính năng

- CRUD Operations cho Products
- REST API Endpoints
- Django Admin Interface
- API Documentation
- Sample Data và Fixtures
- Browsable API Interface

## Yêu cầu hệ thống

- Python 3.8+
- Django 4.2+
- Django REST Framework 3.14+
- pip (Python package installer)

## Cài đặt

1. Clone repository
```bash
git clone 
cd django_api_demo
```

2. Tạo và kích hoạt môi trường ảo
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python -m venv .venv
source .venv/bin/activate
```

3. Cài đặt các dependencies
```bash
pip install -r requirements.txt
```

4. Thực hiện migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Tạo superuser
```bash
python manage.py createsuperuser
```

6. Load dữ liệu mẫu (optional)
```bash
python manage.py loaddata products
```

7. Chạy development server
```bash
python manage.py runserver
```

## Cấu trúc Project

```
django_api_demo/
│
├── api/                    # Main application directory
│   ├── migrations/        # Database migrations
│   ├── fixtures/         # Sample data
│   ├── __init__.py
│   ├── admin.py          # Admin configuration
│   ├── apps.py
│   ├── models.py         # Database models
│   ├── serializers.py    # DRF serializers
│   ├── urls.py           # URL configurations
│   └── views.py          # API views
│
├── django_api_demo/       # Project directory
│   ├── __init__.py
│   ├── settings.py       # Project settings
│   ├── urls.py           # Main URL routing
│   └── wsgi.py
│
├── .venv/                 # Virtual environment (không được commit)
├── .gitignore
├── manage.py
├── requirements.txt       # Project dependencies
└── README.md
```

## API Endpoints

### Products API

|
 Method 
|
 Endpoint 
|
 Description 
|
|
--------
|
----------
|
-------------
|
|
 GET 
|
`/api/products/`
|
 Lấy danh sách sản phẩm 
|
|
 POST 
|
`/api/products/`
|
 Tạo sản phẩm mới 
|
|
 GET 
|
`/api/products/{id}/`
|
 Lấy chi tiết sản phẩm 
|
|
 PUT 
|
`/api/products/{id}/`
|
 Cập nhật toàn bộ sản phẩm 
|
|
 PATCH 
|
`/api/products/{id}/`
|
 Cập nhật một phần sản phẩm 
|
|
 DELETE 
|
`/api/products/{id}/`
|
 Xóa sản phẩm 
|

## Sử dụng API

### Sử dụng cURL

```bash
# Lấy danh sách sản phẩm
curl http://127.0.0.1:8000/api/products/

# Tạo sản phẩm mới
curl -X POST http://127.0.0.1:8000/api/products/ \
     -H "Content-Type: application/json" \
     -d '{"name":"Test Product","description":"Test Description","price":"99.99"}'

# Cập nhật sản phẩm
curl -X PUT http://127.0.0.1:8000/api/products/1/ \
     -H "Content-Type: application/json" \
     -d '{"name":"Updated Product","description":"Updated Description","price":"149.99"}'

# Xóa sản phẩm
curl -X DELETE http://127.0.0.1:8000/api/products/1/
```

### Sử dụng Python Requests

```python
import requests

# Lấy danh sách sản phẩm
response = requests.get('http://127.0.0.1:8000/api/products/')
print(response.json())

# Tạo sản phẩm mới
data = {
    "name": "Test Product",
    "description": "Test Description",
    "price": "99.99"
}
response = requests.post('http://127.0.0.1:8000/api/products/', json=data)
print(response.json())
```

## Development

### Chạy Tests
```bash
python manage.py test
```

### Code Style
Project này tuân theo PEP 8 coding style. Sử dụng flake8 để kiểm tra:
```bash
flake8
```

## Admin Interface

Truy cập Django Admin Interface tại:
```
http://127.0.0.1:8000/admin/
```

## API Documentation

Browsable API documentation có sẵn tại:
```
http://127.0.0.1:8000/api/
```

## Lưu ý quan trọng

1. Trailing Slashes
   - Django yêu cầu trailing slash (/) ở cuối URL
   - Ví dụ: Sử dụng `/api/products/` thay vì `/api/products`

2. Content-Type Header
   - Luôn set `Content-Type: application/json` cho POST/PUT requests

3. Authentication (nếu được cấu hình)
   - Thêm token vào header: `Authorization: Bearer <your-token>`

## Troubleshooting

### Common Issues

1. Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

2. Database Issues
```bash
python manage.py flush  # Reset database
python manage.py loaddata products  # Reload sample data
```

3. Permission Issues
- Đảm bảo user có quyền truy cập admin interface
- Kiểm tra file permissions

## Contributing

1. Fork repository
2. Tạo feature branch
3. Commit changes
4. Push to branch
5. Tạo Pull Request

## License

[MIT License](LICENSE)

## Contact

Your Name - [lch.ryu2001@gmail.com](mailto:lch.ryu2001@gmail.com)

Project Link: [https://github.com/lchryu/django_api_demo](https://github.com/lchryu/django_api_demo)