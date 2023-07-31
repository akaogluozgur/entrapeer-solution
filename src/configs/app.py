from datetime import timedelta


class AppConfigs:
    NAME = 'etl-startup-investments'
    DESCRIPTION = 'ETL process of startup investments'
    DATA_FOLDER = 'data/startup-investments'
    SCHEDULE_INTERVAL = timedelta(days=1)
