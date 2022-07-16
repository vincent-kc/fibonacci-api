import asyncio

from fastapi import BackgroundTasks, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from app.database import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_fibonacci(n: int, rec_id: int):
    await asyncio.sleep(3)  # simulate processing
    db: Session = SessionLocal()
    try:
        fib_rec = db.get(models.Fibonacci, rec_id)

        n1, n2 = 0, 1
        nth = 0
        for i in range(n - 1):
            n1 = n2
            n2 = nth
            nth = n1 + n2
        fib_rec.nth = nth
        fib_rec.status = models.Status.success.value
        db.add(fib_rec)
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    else:
        db.commit()
        print("CREATED FIBONACCI!")


@app.post("/fibonacci", response_model=schemas.FibOutput, status_code=201)
async def fibonacci(
    fib: schemas.FibInput, bg_task: BackgroundTasks, db: Session = Depends(get_db)
):
    try:
        fib_item = (
            db.query(models.Fibonacci).filter(models.Fibonacci.n == fib.n).first()
        )

        if fib_item:
            return fib_item

        fib_rec = models.Fibonacci(n=fib.n)
        db.add(fib_rec)
        db.commit()
        db.refresh(fib_rec)
        bg_task.add_task(create_fibonacci, fib.n, fib_rec.id)
        return fib_rec

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
