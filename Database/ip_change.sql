USE [LABVIEW]
GO

/****** Object:  Table [dbo].[IP_Changes]    Script Date: 8/10/2025 11:07:39 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[IP_Changes](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[interface_name] [nvarchar](100) NULL,
	[new_ip] [nvarchar](50) NULL,
	[time_changed] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[IP_Changes] ADD  DEFAULT (getdate()) FOR [time_changed]
GO


