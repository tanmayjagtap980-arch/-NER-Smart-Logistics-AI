from database.database import get_connection


def create_delivery(
    cargo,
    source,
    destination,
    priority
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO deliveries
        (cargo, source, destination, priority)
        VALUES (?, ?, ?, ?)
        """,
        (
            cargo,
            source,
            destination,
            priority
        )
    )

    connection.commit()

    delivery_id = cursor.lastrowid

    connection.close()

    return delivery_id


def get_deliveries():

    connection = get_connection()

    rows = connection.execute(
        "SELECT * FROM deliveries ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return [dict(row) for row in rows]


def update_delivery_status(
    delivery_id,
    status
):

    connection = get_connection()

    connection.execute(
        """
        UPDATE deliveries
        SET status = ?
        WHERE id = ?
        """,
        (
            status,
            delivery_id
        )
    )

    connection.commit()

    connection.close()


def create_emergency(
    hospital,
    cargo,
    quantity
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO emergency_requests
        (hospital, cargo, quantity)
        VALUES (?, ?, ?)
        """,
        (
            hospital,
            cargo,
            quantity
        )
    )

    connection.commit()

    emergency_id = cursor.lastrowid

    connection.close()

    return emergency_id


def get_emergencies():

    connection = get_connection()

    rows = connection.execute(
        """
        SELECT *
        FROM emergency_requests
        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()

    return [dict(row) for row in rows]
def create_emergency(emergency_type, location, description):
    # Temporary version
    return {
        "type": emergency_type,
        "location": location,
        "description": description
    }