/*Query pada soal salah, jawaban yang benar query dibawah ini*/

SELECT Merek, COUNT(Model) 
FROM Ponsel 
WHERE DualSim = TRUE
GROUP BY Merek
