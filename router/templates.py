from fastapi.requests import Request
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from schemas import ProductBase

templates = Jinja2Templates(directory='templates')


router = APIRouter(prefix='/templates', tags=['templates'])


@router.post('/product/{id}', response_class=HTMLResponse)
def get_product_info_template(id: int, request: Request, product: ProductBase):
    return templates.TemplateResponse('product.html', {
        "request": request,
        "id": id, 
        "product": product
    })