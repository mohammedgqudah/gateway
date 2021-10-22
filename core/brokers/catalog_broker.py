from .base_broker import Broker


class CatalogBroker(Broker):
    alias = 'catalog'
    name = 'catalog'

    async def list_products(self, business_id: str, params, **kwargs):
        """list business level products
        """

        url = self.make_url('business', business_id, 'products')
        return await self.make_request(
            method='GET',
            url=url,
            params=params,
            **kwargs
        )

    async def get_product(self, business_id: str, product_id: str, params, **kwargs):
        """get business level product
        """
        url = self.make_url('business', business_id, 'products', product_id)
        return await self.make_request(
            method='GET',
            url=url,
            params=params,
            **kwargs
        )

    async def create_product(self, business_id: str, params, **kwargs):
        """create product
        """
        url = self.make_url('business', business_id, 'products')
        return await self.make_request(
            method='POST',
            url=url,
            params=params,
            **kwargs
        )

    async def update_product(self, business_id: str, product_id: str, params, **kwargs):
        """create product
        """
        url = self.make_url('business', business_id, 'products', product_id)
        return await self.make_request(
            method='PUT',
            url=url,
            params=params,
            **kwargs
        )

    async def list_available_products(self, business_id: str, channel_id: str, params, **kwargs):
        """list channel level available products
        """
        url = self.make_url('business', business_id, 'channel', channel_id, 'products')
        return await self.make_request(
            method='GET',
            url=url,
            params=params,
            **kwargs
        )

    async def get_available_product(self, business_id: str, channel_id: str, product_id: str, params, **kwargs):
        """get channel level available product
        """
        url = self.make_url('business', business_id, 'channel', channel_id, 'products', product_id)
        return await self.make_request(
            method='GET',
            url=url,
            params=params,
            **kwargs
        )
