from database.DB_connect import DBConnect
from model.customer import Customer
from model.employee import Employee
from model.track import Track


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

    @staticmethod
    def getAllTotali(country):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select t.CustomerId as customerId, sum(t.Total) as totale
                    from (select c.CustomerId, i.InvoiceId , i2.Total 
                            from invoiceline i , invoice i2 , customer c 
                            where i.InvoiceId = i2.InvoiceId and i2.CustomerId = c.CustomerId and c.Country = %s
                            group by c.CustomerId , i.InvoiceId, i2.Total
                            order by c.CustomerId, i.InvoiceId  asc) as t
                    group by t.CustomerId
                    order by sum(t.Total) desc """

        cursor.execute(query, (country,))

        for row in cursor:
            results.append((row["customerId"], row["totale"]))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllTracks(country):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from track t 
                    where t.TrackId in (select distinct(t.TrackId)
                                        from invoiceline i , invoice i2 , customer c, track t 
                                        where i.InvoiceId = i2.InvoiceId 
                                        and i2.CustomerId = c.CustomerId 
                                        and i.TrackId = t.TrackId 
                                        and c.Country = %s
                                        order by t.TrackId asc)
                    order by t.TrackId asc"""

        cursor.execute(query, (country,))

        for row in cursor:
            results.append(Track(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllAcquisti(country):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select i.TrackId as idTrack, count(*) as numAcquisti
                    from invoiceline i , invoice i2 , customer c, track t 
                    where i.InvoiceId = i2.InvoiceId and i2.CustomerId = c.CustomerId and i.TrackId = t.TrackId and c.Country = %s
                    group by i.TrackId
                    order by count(*) desc, t.Name asc"""

        cursor.execute(query, (country,))

        for row in cursor:
            results.append((row["idTrack"], row["numAcquisti"]))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllArtistAlbumGenre(country):
        conn = DBConnect.get_connection()

        results = {}

        cursor = conn.cursor(dictionary=True)
        query = """select t.TrackId as idTrack, a2.Name as artista, a.Title as titoloAlbum, g.Name as genere
                    from track t, album a , genre g, artist a2  
                    where t.TrackId in (select distinct(t.TrackId)
                                        from invoiceline i , invoice i2 , customer c, track t 
                                        where i.InvoiceId = i2.InvoiceId 
                                        and i2.CustomerId = c.CustomerId 
                                        and i.TrackId = t.TrackId 
                                        and c.Country = %s
                                        order by t.TrackId asc)
                    and t.AlbumId = a.AlbumId 
                    and t.GenreId = g.GenreId
                    and a.ArtistId = a2.ArtistId 
                    order by t.TrackId asc"""

        cursor.execute(query, (country,))

        for row in cursor:
            results[row["idTrack"]] = []
            results[row["idTrack"]].append(row["artista"])
            results[row["idTrack"]].append(row["titoloAlbum"])
            results[row["idTrack"]].append(row["genere"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllEmployees(country):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from employee e 
                    where e.EmployeeId in (select distinct e.EmployeeId 
                                            from invoice i , customer c , employee e 
                                            where i.CustomerId = c.CustomerId 
                                            and c.SupportRepId = e.EmployeeId
                                            and c.Country = %s)"""

        cursor.execute(query, (country,))

        for row in cursor:
            results.append(Employee(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllEmpStats(country):
        conn = DBConnect.get_connection()

        results = {}

        cursor = conn.cursor(dictionary=True)
        query = """select t.SupportRepId as employeeId, count(distinct(t.CustomerId)) as numClienti, sum(t.Total) as ricavo, sum(t.numTracce) as numTracce
                    from (select c.SupportRepId, c.CustomerId, i.InvoiceId, i2.Total, count(*) as numTracce 
                            from invoiceline i , invoice i2 , customer c 
                            where i.InvoiceId = i2.InvoiceId and i2.CustomerId = c.CustomerId and c.Country = %s
                            group by c.SupportRepId, c.CustomerId, i.InvoiceId, i2.Total) as t
                    group by employeeId
                    order by ricavo desc """

        cursor.execute(query, (country,))

        for row in cursor:
            results[row["employeeId"]] = []
            results[row["employeeId"]].append(row["numClienti"])
            results[row["employeeId"]].append(row["numTracce"])
            results[row["employeeId"]].append(row["ricavo"])

        cursor.close()
        conn.close()
        return results