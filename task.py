from enum import Enum

import mysql.connector

class Task:
    def __init__(self, assignor, assignee, description, due_date, is_Complete, level_of_responsibility):
        self.assignor = assignor
        self.assignee = assignee
        self.description = description
        self.due_date = due_date
        self.is_Complete = is_Complete
        self.level_of_responsibility = level_of_responsibility

    @classmethod
    def create_task(cls, assignor, assignee, description, due_date, is_Complete, level_of_responsibility):
        connection = mysql.connector.connect(
            host="localhost", user="root", passwd="admin", database="logindb"
        )

        cursor = connection.cursor()

        insert_query = "INSERT INTO Task (assignor, assignee, description, due_date, is_Complete, level_of_responsibility) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (assignor, assignee, description, due_date, is_Complete, level_of_responsibility))

        connection.commit()
        connection.close()

        return cls(assignor, assignee, description, due_date, is_Complete, level_of_responsibility)

    @classmethod
    def get_task(cls, task_id):
        connection = mysql.connector.connect(
            host="localhost", user="root", passwd="admin", database="logindb"
        )

        cursor = connection.cursor()

        select_query = "SELECT * FROM Task WHERE id = %s"
        cursor.execute(select_query, (task_id,))

        task = cursor.fetchone()
        connection.close()

        return cls(*task)