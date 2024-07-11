USE AdventureWorks2017
GO

-- Enable identity insert on the target table
SET IDENTITY_INSERT [SalesLT].[Customer] ON
GO

-- Insert the records into the target table
INSERT INTO [SalesLT].[Customer]
(
    [CustomerID]
    ,[NameStyle]
    ,[Title]
    ,[FirstName]
    ,[MiddleName]
    ,[LastName]
    ,[Suffix]
    ,[CompanyName]
    ,[SalesPerson]
    ,[EmailAddress]
    ,[Phone]
    ,[PasswordHash]
    ,[PasswordSalt]
    ,[rowguid]
    ,[ModifiedDate]
)
VALUES
(595959, 0, 'Mr.', 'John', 'SR', 'Max', 'Jr.', 'xyz', 'adventure-works\John', 'john@gmail.com', '13456-095-0045', 'Trade', 'Analyst', '1F54D149-9FDD-452E-BF85-BAE74C87CDB1', '2023-01-01')
,(292929, 0, 'Mr.', 'Stephen', 'BK', 'Ben', 'Jr.', 'abc', 'adventure-works\Stephen', 'stephen@gmail.com', '9876-675-8787', 'Innovate', 'Developer', 'C22A1E3A-FAA3-4365-897B-8B8F74CD1234', '2023-01-02')

GO

-- Disable identity insert on the target table
SET IDENTITY_INSERT [SalesLT].[Customer] OFF
GO
