SELECT Nama, TanggalPisah, Ranking, 
    CASE
        WHEN Ranking = 100 THEN 'bingkisan'
        WHEN Ranking < 100 THEN 'bingkisan pelipur lara'
    END AS Bingkisan
FROM (
    SELECT A.Nama, C.TanggalPisah, RANK () OVER ( 
            ORDER BY C.TanggalPisah DESC
        ) Ranking  
    FROM Penduduk AS A
    INNER JOIN Pasangan AS B ON B.PendudukID = A.ID
    INNER JOIN Perpisahan AS C ON  C.PasanganID = B.ID
) AS rank