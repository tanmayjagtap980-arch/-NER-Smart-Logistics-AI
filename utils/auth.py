import hashlib

from database.database import get_connection


def hash_password(
    password
):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def register_user(
    name,
    email,
    password
):

    connection = get_connection()

    try:

        connection.execute(
            """
            INSERT INTO users
            (name, email, password_hash)
            VALUES (?, ?, ?)
            """,
            (
                name,
                email,
                hash_password(password)
            )
        )

        connection.commit()

        return True

    except Exception:

        return False

    finally:

        connection.close()


def login_user(
    email,
    password
):

    connection = get_connection()

    row = connection.execute(
        """
        SELECT *
        FROM users
        WHERE email = ?
        AND password_hash = ?
        """,
        (
            email,
            hash_password(password)
        )
    ).fetchone()

    connection.close()

    if row:

        return dict(row)

    return None