from whatsup.main import scheduler
from whatsup.db import engine

scheduler.add_job(
    func=lambda: print("Hello, World!"),
    trigger="interval",
    seconds=10,
    id="hello_world_job",
    replace_existing=True,
)


async def get_monitors_from_db():
    session = engine.connect()
    monitors = session.execute("SELECT * FROM monitors")
    return monitors.fetchall()


async def load_db_jobs():
    monitors = (
        get_monitors_from_db()
    )  # Implement this function to fetch jobs from your database
    for job in monitors:
        scheduler.add_job(
            func=job.func,
            trigger=job.trigger,
            args=job.args,
            kwargs=job.kwargs,
            id=job.id,
            replace_existing=True,
        )
