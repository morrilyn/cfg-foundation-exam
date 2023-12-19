CREATE DATABASE foundation_exam;
USE foundation_exam;

-- A] movie_info table creation
CREATE TABLE movie_info (
    Movie_ID INT PRIMARY KEY,
    Movie_Name VARCHAR(255) NOT NULL,
    Movie_Length TIME NOT NULL, 
    Age_Rating VARCHAR(10)
);

-- B] screens table creation
CREATE TABLE screens (
    Screen_ID INT PRIMARY KEY,
    Four_K BOOLEAN NOT NULL
);

-- C] showings table creation
CREATE TABLE showings (
    Showing_ID INT PRIMARY KEY,
    Movie_ID INT,
    Screen_ID INT,
    Start_Time TIME NOT NULL,
    Available_Seats INT NOT NULL,
    FOREIGN KEY (Movie_ID) REFERENCES movie_info(Movie_ID),
    FOREIGN KEY (Screen_ID) REFERENCES screens(Screen_ID)
);

-- Inserting into movie_info
INSERT INTO movie_info (Movie_ID, Movie_Name, Movie_Length, Age_Rating) VALUES
(1, 'The Movie', '01:35:00', '12A');

-- Inserting into screens
INSERT INTO screens (Screen_ID, Four_K) VALUES
(1, FALSE);

-- Inserting into showings
INSERT INTO showings (Showing_ID, Movie_ID, Screen_ID, Start_Time, Available_Seats) VALUES
(2, 1, 1, '12:00:00', 23);

SELECT mi.Movie_Name, sh.Start_Time
FROM movie_info mi
JOIN showings sh ON mi.Movie_ID = sh.Movie_ID
WHERE sh.Start_Time > '12:00:00' AND sh.Available_Seats > 0
ORDER BY sh.Start_Time;

SELECT mi.Movie_Name, COUNT(sh.Showing_ID) AS NumberOfShowings
FROM movie_info mi
JOIN showings sh ON mi.Movie_ID = sh.Movie_ID
GROUP BY mi.Movie_ID, mi.Movie_Name
ORDER BY NumberOfShowings DESC
LIMIT 1;






