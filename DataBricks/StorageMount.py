# Access Azure Data Lake Storage using Azure Active Directory credential passthrough
# Mount Azure Data Lake Storage (bronze container) to DBFS using credential passthrough
configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",
  "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
}

dbutils.fs.mount(
  source = "abfss://bronze@awiriswdatalake.dfs.core.windows.net/",
  mount_point = "/mnt/bronze",
  extra_configs = configs)


# Mount Azure Data Lake Storage (silver container) to DBFS using credential passthrough

configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",
  "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
}

dbutils.fs.mount(
  source = "abfss://silver@awiriswdatalake.dfs.core.windows.net/",
  mount_point = "/mnt/silver",
  extra_configs = configs)


# Mount Azure Data Lake Storage (gold container) to DBFS using credential passthrough
configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",
  "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
}

dbutils.fs.mount(
  source = "abfss://gold@awiriswdatalake.dfs.core.windows.net/",
  mount_point = "/mnt/gold",
  extra_configs = configs)
