USE gold_db
GO

CREATE OR ALTER PROC CreateSQLServerlessView_gold @ViewName VARCHAR(100)
AS
BEGIN

DECLARE @statement VARCHAR(MAX)

    SET @statement = N'CREATE OR ALTER VIEW ' + @ViewName + ' AS
    SELECT *
    FROM
        OPENROWSET(
            BULK ''https://iriswdatalakegen2.dfs.core.windows.net/gold-clean/SalesLT/' + @ViewName + '/'',
            FORMAT = ''PARQUET''
        ) as [result]
    '


EXEC(@statement)

END
GO
