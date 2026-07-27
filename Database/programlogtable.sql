CREATE TABLE ProgramLog (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    ProgramName NVARCHAR(100),
    Username NVARCHAR(100),
    LaunchTime DATETIME,           
    DurationSeconds INT            
);