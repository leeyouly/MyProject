from spiderlib.data import DataStorage
import PyDB

class ImportIneMarket_Storage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_MARKET_INE_DAY'
        self.db.set_metadata(self.table_name, [
            PyDB.StringField("title"),
            PyDB.StringField("delivery_mon",is_key=True),
            PyDB.StringField("pre_settlement_price"),
            PyDB.StringField("open_price"),
            PyDB.StringField("high_price"),
            PyDB.StringField("low_price"),
            PyDB.StringField("close_price"),
            PyDB.StringField("settlement_price"),
            PyDB.StringField("rise_offset_1"),
            PyDB.StringField("rise_offset_2"),
            PyDB.StringField("trading_vol"),
            PyDB.StringField("position_vol"),
            PyDB.StringField("position_chg_vol"),
            PyDB.StringField("trading_dt",is_key=True),
            PyDB.DateField("datetime_stamp"),
            PyDB.StringField("transactions_times"),
            PyDB.DateField("create_dt"),
            PyDB.StringField("instrumentid",is_key=True),
        ])

    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item)
        self.db.commit()


class TradingCalendarStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_TRADE_CALENDAR'
        self.db.set_metadata(self.table_name, [
            PyDB.StringField('tradingcalendar', is_key=True),
            PyDB.DateField('tradingday', is_key=True),
            PyDB.IntField('flag'),
        ])