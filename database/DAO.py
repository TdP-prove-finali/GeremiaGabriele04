from database.DB_connect import DBConnect

class DAO():

    @staticmethod
    def getAllCountry():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct c.Country as country
                    from customer c 
                    order by c.Country asc """

        cursor.execute(query)

        for row in cursor:
            results.append(row["country"])

        cursor.close()
        conn.close()
        return results