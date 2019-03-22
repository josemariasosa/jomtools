
# Insert the _config attributes in a Class. ----->

from config import _config, db_business


class FileCreator(object):

    """ API GET Request Parameters
            'https://apisandbox.facturama.mx/cfdi/{pdf|xml|html}/{issued}/{id}'
    """

    def __init__(self, cfdi_id, order_id):

        # Config attributes.
        for key in _config:
            setattr(self, key, _config[key])

        self.slack = Slack()
        self.cfdi_id = cfdi_id
        self.order_id = order_id
        self.date = self.getCurrentDate()

        # Mongo Collections.
        self.invoiceDB = db_business['invoice']

    # ----------------------------------------------------------
