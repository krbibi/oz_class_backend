from fastapi import FastAPI
from items import router as items_router
from users import router as users_router
from sync_async_test import router as sync_async_router

app = FastAPI()
# app대신 router 를 쓰는 이유?
app.include_router(items_router)
app.include_router(users_router)
app.include_router(sync_async_router)


# # 실행방법:
# # - uvicorn main:app --reload
# 위에 내용을 사용하기 귀찮으면 아래처럼 설정을 변경한다.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",port=8000, log_level='debug',reload=True) 
    # python main.py