from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        temp = {
            "id": result[0],
            "summary": result[1],
            "description": result[2],
            "status_id": result[3],
            "active": result[4]
        }
        out.append(temp)
    return out


def scan():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task", ())
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return output_formatter(results)


def select_by_id(pk):
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task WHERE id=?", (pk,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return output_formatter(results)[0]


def insert(task_data):
    task_tuple = (
        task_data.get("summary"),
        task_data.get("description"),
        task_data.get("status_id"),
        task_data.get("active")        
    )
    statement = """
        INSERT INTO task (
            summary,
            description,
            status_id,
            active
        ) VALUES (?, ?, ?, ?)
    """
    conn = get_db()
    conn.execute(statement, task_tuple)
    conn.commit()
    conn.close()


def update(task_data, pk):
    stmt_tuple = (
        task_data.get("summary"),
        task_data.get("description"),
        task_data.get("status_id"),
        task_data.get("active"),
        pk 
    )
    statement = """
        UPDATE task
        SET summary = ?,
            description = ?,
            status_id = ?,
            active = ?
        WHERE id = ?
    """

    conn = get_db()
    conn.execute(statement, stmt_tuple)
    conn.commit()
    conn.close()

def delete(pk):
    conn = get_db()
    conn.execute("DELETE FROM task WHERE id=?", (pk,))
    conn.commit()
    conn.close()

