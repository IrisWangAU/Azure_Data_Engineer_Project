USE gold_db
GO

CREATE OR ALTER PROC CreateSQLServerLessView_gold  @ViewName  NVARCHAR(100)
AS
BEGIN

DECLARE @statement VARCHAR(MAX)

    SET @statement = N'CREATE OR ALTER VIEW' + @ViewName + ' AS
    SELECT *
    FROM
        OPENROWSET(
            BULK ''https://irisdatalakegen2.dfs.core.windows.net/gold-clean/SalesLT/' + @ViewName + '/'',
            FORMAT = ''DELTA''
        ) as [result]
    '

EXEC (@statement)

END
GO
