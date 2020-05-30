SELECT DISTINCT(A.TEMPATTINGGAL) FROM PahlawanSuper AS A
INNER JOIN Senjata AS B ON B.PahlawanSuperID = A.ID
INNER JOIN JenisSenjata AS C ON C.ID = B.JenisSenjataID
WHERE C.JenisSenjata = 'Kapak'