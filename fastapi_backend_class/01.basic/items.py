from fastapi import APIRouter

# @app.get()
# @router.get()
# 기능은 같지만 app 분기처리를 하기 위해 router 사용

# item 관련 API 호출
router = APIRouter()

@router.get('/api/v1/items/{item_id}',
            status_code=200, # 성공했을때 200 내려줘
            tags= ['items','payment'],  # 관련 api를 보기위함
            summary='특정 아이템을 가져오기',
            description='Item 모델의 item_id 값을 가지고 하나의 아이템 데이터 정보를 가져옵니다.',
            response_description='아이템 세부 정보 반환' # 응답을 어떻게 줄건지
            )
def get_item(item_id:int):
    return {'items':'item'}