from fastapi.requests import Request
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import BackgroundTasks
from schemas import ProductBase

templates = Jinja2Templates(directory="templates")


router = APIRouter(prefix="/templates", tags=["templates"])

@router.post("/product/{id}", response_class=HTMLResponse)
def get_product_info_template(
    id: int, request: Request, product: ProductBase, bt: BackgroundTasks
):
    bt.add_task(print_request, "This is a sample log message")
    return templates.TemplateResponse(
        "product.html", {"request": request, "id": id, "product": product}
    )


def print_request(message: str):
    print(message)
