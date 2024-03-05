-- Crearea tabelului Angajati și inserarea datelor de exemplu
CREATE TABLE Angajati (
    Nume NVARCHAR(MAX),
    Prenume NVARCHAR(MAX),
    Varsta NVARCHAR(MAX),
    Nr_Telefon NVARCHAR(20) -- Adăugarea coloanei Nr_Telefon
);

INSERT INTO Angajati (Nume, Prenume, Varsta, Nr_Telefon) VALUES 
('Popescu, Ionescu, Dragomir', 'Ana, Andrei, Maria', '30, 35, 40', '123456789'),
('Radulescu, Stanescu, Marin', 'Ion, Mihai, George', '45, 50, 55', '987654321');

-- Interogarea pentru a face split pe cele patru coloane
SELECT 
    SPLIT_PART(Nume, ',', 1) AS Nume,
    SPLIT_PART(Prenume, ',', 1) AS Prenume,
    SPLIT_PART(Varsta, ',', 1) AS Varsta,
    Nr_Telefon
FROM 
    Angajati
UNION ALL
SELECT 
    SPLIT_PART(Nume, ',', 2) AS Nume,
    SPLIT_PART(Prenume, ',', 2) AS Prenume,
    SPLIT_PART(Varsta, ',', 2) AS Varsta,
    Nr_Telefon
FROM 
    Angajati
UNION ALL
SELECT 
    SPLIT_PART(Nume, ',', 3) AS Nume,
    SPLIT_PART(Prenume, ',', 3) AS Prenume,
    SPLIT_PART(Varsta, ',', 3) AS Varsta,
    Nr_Telefon
FROM 
    Angajati;