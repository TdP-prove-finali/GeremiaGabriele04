from database.DB_connect import DBConnect
from model.customer import Customer


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

    @staticmethod
    def getAllNodes(country):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from customer c 
                    where c.Country = %s
                    order by c.LastName asc """

        cursor.execute(query, (country,))

        for row in cursor:
            results.append(Customer(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllEdges(country, idMap):
        conn = DBConnect.get_connection()

        results = {}

        cursor = conn.cursor(dictionary=True)
        query = """select i2.CustomerId as customerId, i.TrackId as trackId
                    from invoiceline i , invoice i2 , customer c 
                    where i.InvoiceId = i2.InvoiceId and i2.CustomerId = c.CustomerId and c.Country = %s
                    """

        cursor.execute(query, (country,))

        for row in cursor:
            if row["customerId"] in idMap.keys():
                if row["customerId"] not in results.keys():
                    results[row["customerId"]] = []
                results[row["customerId"]].append(row["trackId"])

        cursor.close()
        conn.close()
        return results