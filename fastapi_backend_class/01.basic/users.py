from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v1/users',
    tags=['users'],
    responses={
        200:{'message':'Success to get users'}, # 응답값을 정해준다. 200 떴으면 메세지
        404: {'message' :'404 Not Found'}  
        } 
)

@router.get('/{user_id}')
def get_user(user_id: int):
    return {'message':'유저 데이터'}