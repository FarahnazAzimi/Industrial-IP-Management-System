CREATE TABLE ImageLog (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    FilePath NVARCHAR(500),
    FileSizeKB INT,
    UploadTime DATETIME,
    ImageData VARBINARY(MAX)
);