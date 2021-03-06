import abc


class CCommonStockApi:
    FIELD_TIME = "time_key"
    FIELD_OPEN = "open"
    FIELD_HIGH = "high"
    FIELD_LOW = "low"
    FIELD_CLOSE = "close"
    FIELD_VOLUME = "volume"
    FIELD_TURNOVER = "turnover"
    FIELD_TURNRATE = "turnover_rate"

    def __init__(self, code, k_type, begin_date, end_date, autype):
        self.code = code
        self.name = None
        self.is_stock = None
        self.k_type = k_type
        self.begin_date = begin_date
        self.end_date = end_date
        self.autype = autype
        self.SetBasciInfo()

    @abc.abstractmethod
    def get_kl_data(self):
        pass

    @abc.abstractmethod
    def SetBasciInfo(self):
        pass

    @abc.abstractmethod
    def do_init(cls):
        pass

    @abc.abstractmethod
    def do_close(cls):
        pass


TRADE_INFO_LST = [CCommonStockApi.FIELD_VOLUME, CCommonStockApi.FIELD_TURNOVER, CCommonStockApi.FIELD_TURNRATE]
