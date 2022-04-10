from fastapi import Depends, HTTPException, Response, status
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from db import db_user
from db.hash import Hash
from auth.oauth2 import create_access_token
from db.database import get_db
from sqlalchemy.orm.session import Session


router = APIRouter(tags=["authentication"], prefix='/auth')


@router.post('/token')
def generate_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db_user.get_by_username(db, request.username)
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid password')
    
    access_token = create_access_token({'sub': user.username})
    
    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'username': user.username,
        'user_id': user.id
    }