from .base_broker import Broker


class CatalogBroker(Broker):
    alias = 'catalog'
    name = 'catalog'

    def list_products(self, business_id: str, params, **kwargs):
        """list business level products
        """

        url = self.make_url('business', business_id, 'products')
        return self.make_request(
            method='GET',
            url=url,
            params=params,
            **kwargs
        )

    def get_product(self, business_id: str, product_id: str, params, **kwargs):
        """get business level product
        """
        url = self.make_url('business', business_id, 'products', product_id)
        return self.make_request(
            method='GET',
            url=url,
            params=params,
            **kwargs
        )

    def create_product(self, business_id: str, params, **kwargs):
        """create product
        """
        url = self.make_url('business', business_id, 'products')
        return self.make_request(
            method='POST',
            url=url,
            params=params,
            **kwargs
        )

    def list_available_products(self, business_id: str, channel_id: str, params, **kwargs):
        """list channel level available products
        """
        url = self.make_url('business', business_id, 'channel', channel_id, 'products')
        return self.make_request(
            method='GET',
            url=url,
            params=params,
            **kwargs
        )

    def get_available_product(self, business_id: str, channel_id: str, product_id: str, params, **kwargs):
        """get channel level available product
        """
        url = self.make_url('business', business_id, 'channel', channel_id, 'products', product_id)
        return self.make_request(
            method='GET',
            url=url,
            params=params,
            **kwargs
        )
